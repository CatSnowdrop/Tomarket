import asyncio
from datetime import datetime
from random import randint, choices
from time import time
from urllib.parse import unquote, quote

import aiohttp
from aiohttp_proxy import ProxyConnector
from better_proxy import Proxy
from pyrogram import Client
from pyrogram.errors import Unauthorized, UserDeactivated, AuthKeyUnregistered, FloodWait
from pyrogram.raw.functions.messages import RequestAppWebView
from pyrogram.raw.types import InputBotAppShortName

from typing import Callable
import functools
from tzlocal import get_localzone
from bot.config import settings
from bot.exceptions import InvalidSession
from bot.utils import logger
from .agents import generate_random_user_agent
from .headers import headers

def error_handler(func: Callable):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            await asyncio.sleep(1)
    return wrapper

def convert_to_local_and_unix(iso_time):
    dt = datetime.fromisoformat(iso_time.replace('Z', '+00:00'))
    local_dt = dt.astimezone(get_localzone())
    unix_time = int(local_dt.timestamp())
    return unix_time

class Tapper:
    def __init__(self, tg_client: Client, proxy: str | None):
        self.session_name = tg_client.name
        self.tg_client = tg_client
        self.proxy = proxy

    async def get_tg_web_data(self) -> str:
        
        if self.proxy:
            proxy = Proxy.from_str(self.proxy)
            proxy_dict = dict(
                scheme=proxy.protocol,
                hostname=proxy.host,
                port=proxy.port,
                username=proxy.login,
                password=proxy.password
            )
        else:
            proxy_dict = None

        self.tg_client.proxy = proxy_dict

        try:
            if not self.tg_client.is_connected:
                try:
                    await self.tg_client.connect()

                except (Unauthorized, UserDeactivated, AuthKeyUnregistered):
                    raise InvalidSession(self.session_name)
            
            while True:
                try:
                    peer = await self.tg_client.resolve_peer('Tomarket_ai_bot')
                    break
                except FloodWait as fl:
                    fls = fl.value

                    logger.warning(f"{self.session_name} | FloodWait {fl}")
                    logger.info(f"{self.session_name} | Sleep {fls}s")
                    await asyncio.sleep(fls + 3)
            
            ref_id = choices([settings.REF_ID, "0000yBC8"], weights=[75, 25], k=1)[0]
            web_view = await self.tg_client.invoke(RequestAppWebView(
                peer=peer,
                app=InputBotAppShortName(bot_id=peer, short_name="app"),
                platform='android',
                write_allowed=True,
                start_param=ref_id
            ))

            auth_url = web_view.url
            tg_web_data = unquote(
                string=unquote(string=auth_url.split('tgWebAppData=')[1].split('&tgWebAppVersion')[0]))
            tg_web_data_parts = tg_web_data.split('&')

            user_data = quote(tg_web_data_parts[0].split('=')[1])
            chat_instance = tg_web_data_parts[1].split('=')[1]
            chat_type = tg_web_data_parts[2].split('=')[1]
            auth_date = tg_web_data_parts[4].split('=')[1]
            hash_value = tg_web_data_parts[5].split('=')[1]

            init_data = (f"user={user_data}&chat_instance={chat_instance}&chat_type={chat_type}&start_param={ref_id}&auth_date={auth_date}&hash={hash_value}")
            
            if self.tg_client.is_connected:
                await self.tg_client.disconnect()

            return ref_id, init_data

        except Exception as error:
            logger.error(f"{self.session_name} | Unknown error: {error}")
            await asyncio.sleep(delay=3)
            return None, None

    @error_handler
    async def make_request(self, http_client, method, endpoint=None, url=None, **kwargs):
        full_url = url or f"https://api-web.tomarket.ai/tomarket-game/v1{endpoint or ''}"
        response = await http_client.request(method, full_url, **kwargs)
        
        return await response.json()
        
    @error_handler
    async def login(self, http_client, tg_web_data: str, ref_id: str) -> tuple[str, str]:
        response = await self.make_request(http_client, "POST", "/user/login", json={"init_data": tg_web_data, "invite_code": ref_id})
        return response.get('data', {}).get('access_token', None)

    @error_handler
    async def check_proxy(self, http_client: aiohttp.ClientSession) -> None:
        response = await self.make_request(http_client, 'GET', url='https://httpbin.org/ip', timeout=aiohttp.ClientTimeout(5))
        ip = response.get('origin')
        logger.info(f"{self.session_name} | Proxy IP: {ip}")

    @error_handler
    async def get_balance(self, http_client):
        return await self.make_request(http_client, "POST", "/user/balance")

    @error_handler
    async def get_ticket_spin(self, http_client):
        return await self.make_request(http_client, "POST", "/user/tickets")

    @error_handler
    async def play_game_spin(self, http_client):
        return await self.make_request(http_client, "POST", "/spin/raffle", json={"category": "ticket_spin_1"})

    @error_handler
    async def get_unusedStars(self, http_client):
        return await self.make_request(http_client, "POST", "/rank/data")

    @error_handler
    async def upgrade_rank(self, http_client, stars):
        return await self.make_request(http_client, "POST", "/spin/raffle", json={"stars": int(stars)})

    @error_handler
    async def claim_daily(self, http_client):
        return await self.make_request(http_client, "POST", "/daily/claim", json={"game_id": "fa873d13-d831-4d6f-8aee-9cff7a1d0db1"})

    @error_handler
    async def start_farming(self, http_client):
        return await self.make_request(http_client, "POST", "/farm/start", json={"game_id": "53b22103-c7ff-413d-bc63-20f6fb806a07"})

    @error_handler
    async def claim_farming(self, http_client):
        return await self.make_request(http_client, "POST", "/farm/claim", json={"game_id": "53b22103-c7ff-413d-bc63-20f6fb806a07"})

    @error_handler
    async def play_game(self, http_client):
        return await self.make_request(http_client, "POST", "/game/play", json={"game_id": "59bcd12e-04e2-404c-a172-311a0084587d"})

    @error_handler
    async def claim_game(self, http_client, points=None):
        return await self.make_request(http_client, "POST", "/game/claim", json={"game_id": "59bcd12e-04e2-404c-a172-311a0084587d", "points": points})

    @error_handler
    async def start_task(self, http_client, data):
        return await self.make_request(http_client, "POST", "/tasks/start", json=data)

    @error_handler
    async def check_task(self, http_client, data):
        return await self.make_request(http_client, "POST", "/tasks/check", json=data)

    @error_handler
    async def claim_task(self, http_client, data):
        return await self.make_request(http_client, "POST", "/tasks/claim", json=data)

    @error_handler
    async def get_combo(self, http_client):
        return await self.make_request(http_client, "POST", "/tasks/hidden")

    @error_handler
    async def get_stars(self, http_client):
        return await self.make_request(http_client, "POST", "/tasks/classmateTask")

    @error_handler
    async def start_stars_claim(self, http_client, data):
        return await self.make_request(http_client, "POST", "/tasks/classmateStars", json=data)

    @error_handler
    async def get_tasks(self, http_client):
        return await self.make_request(http_client, "POST", "/tasks/list", json={'language_code': 'en'})

    
    async def run(self) -> None:

        if settings.USE_RANDOM_DELAY_IN_RUN:
            random_delay = randint(settings.RANDOM_DELAY_IN_RUN[0], settings.RANDOM_DELAY_IN_RUN[1])
            logger.info(f"{self.tg_client.name} | Bot will start in <light-red>{random_delay}s</light-red>")
            await asyncio.sleep(delay=random_delay)
        
        proxy_conn = ProxyConnector().from_url(self.proxy) if self.proxy else None
        http_client = aiohttp.ClientSession(headers=headers, connector=proxy_conn)
        if self.proxy:
            await self.check_proxy(http_client=http_client)
        
        if settings.FAKE_USERAGENT:            
            http_client.headers['User-Agent'] = generate_random_user_agent(device_type='android', browser_type='chrome')

        ref_id, init_data = await self.get_tg_web_data()

        # ``
        # Наши переменные
        # ``
        end_farming_dt = 0
        tickets = 0
        next_stars_check = 0
        next_combo_check = 0
        while True:
            if http_client.closed:
                if proxy_conn:
                    if not proxy_conn.closed:
                        proxy_conn.close()

                proxy_conn = ProxyConnector().from_url(self.proxy) if self.proxy else None
                http_client = aiohttp.ClientSession(headers=headers, connector=proxy_conn)
            access_token = await self.login(http_client=http_client, tg_web_data=init_data, ref_id=ref_id)
            if not access_token:
                logger.info(f"{self.session_name} | Failed login")
                logger.info(f"{self.session_name} | Sleep <light-red>3600s</light-red>")
                await asyncio.sleep(delay=3600)
                return
            else:
                logger.info(f"{self.session_name} | <light-red>🍅 Login successful</light-red>")
                http_client.headers["Authorization"] = f"{access_token}"
            await asyncio.sleep(delay=1)

            balance = await self.get_balance(http_client=http_client)
            available_balance = balance['data']['available_balance']
            logger.info(f"{self.session_name} | Current balance: <light-red>{available_balance}</light-red>")


            if settings.AUTO_GET_STASHED_TOMATO:
                tasks = await self.get_tasks(http_client=http_client)
                if 'free_tomato' in tasks['data']:
                    free_tomato_task_id = tasks['data']['free_tomato'][0]['taskId']
                    free_tomato_score = tasks['data']['free_tomato'][0]['score']
                    await asyncio.sleep(3)
                    starttask = await self.start_task(http_client=http_client, data={'task_id': free_tomato_task_id})
                    if starttask.get('status') == 0:
                        if starttask['data']['status'] == 2:
                            claim = await self.claim_task(http_client=http_client, data={'task_id': free_tomato_task_id})
                            if claim['status'] == 0:
                                logger.info(f"{self.session_name} | Get free <light-red>{free_tomato_score}</light-red> tomato! 🍅")
                                await asyncio.sleep(2)


            if settings.AUTO_PLAY_SPIN:
                ticket_spin = await self.get_ticket_spin(http_client=http_client)
                available_ticket_spin = ticket_spin['data']['ticket_spin_1']
                logger.info(f"{self.session_name} | Free ticket spin: <light-red>{available_ticket_spin}</light-red>")
                await asyncio.sleep(5)
                while available_ticket_spin > 0:
                    logger.info(f"{self.session_name} | Start spin game...")
                    spin_game = await self.play_game_spin(http_client=http_client)
                    if spin_game.get('status') == 0:
                        result_amount = spin_game['data']['results'][0]['amount']
                        result_type = spin_game['data']['results'][0]['type']
                        logger.info(f"{self.session_name} | Spin game finish! Reward: <light-red>{result_amount} {result_type}</light-red>")
                        available_ticket_spin -= 1
                        await asyncio.sleep(4)


            if settings.AUTO_UPGRADE_RANK:
                unusedStars = await self.get_unusedStars(http_client=http_client)
                available_unusedStars = unusedStars['data']['unusedStars']
                logger.info(f"{self.session_name} | Available unused stars: <light-red>{available_unusedStars}</light-red>")
                if available_unusedStars > 0:
                    upgrade_rank = await self.upgrade_rank(http_client=http_client, stars=available_unusedStars)
                    if upgrade_rank.get('status') == 0:
                        currentRank = upgrade_rank['data']['currentRank']['name']
                        logger.info(f"{self.session_name} | Rank upgrade! Rank: <light-red>{currentRank}</light-red>")


            if 'farming' in balance['data']:
                end_farm_time = balance['data']['farming']['end_at']
                if end_farm_time > time():
                    end_farming_dt = end_farm_time + 240
                    logger.info(f"{self.session_name} | Farming in progress, next claim in <light-red>{round((end_farming_dt - time()) / 60)}m.</light-red>")

            if time() > end_farming_dt:
                claim_farming = await self.claim_farming(http_client=http_client)
                if claim_farming['status'] == 500:
                    start_farming = await self.start_farming(http_client=http_client)
                    logger.info(f"{self.session_name} | Farm started.. 🍅")
                    end_farming_dt = start_farming['data']['end_at'] + 240
                    logger.info(f"{self.session_name} | Next farming claim in <light-red>{round((end_farming_dt - time()) / 60)}m.</light-red>")
                else:
                    farm_points = claim_farming['data']['claim_this_time']
                    logger.info(f"{self.session_name} | Success claim farm. Reward: <light-red>{farm_points}</light-red> 🍅")
                    start_farming = await self.start_farming(http_client=http_client)
                    logger.info(f"{self.session_name} | Farm started.. 🍅")
                    end_farming_dt = start_farming['data']['end_at'] + 240
                    logger.info(f"{self.session_name} | Next farming claim in <light-red>{round((end_farming_dt - time()) / 60)}m.</light-red>")
                await asyncio.sleep(1.5)

            if settings.AUTO_CLAIM_STARS and next_stars_check < time():
                get_stars = await self.get_stars(http_client)
                data_stars = get_stars.get('data', {})
                if get_stars.get('status', -1) == 0 and data_stars:
                    
                    if data_stars.get('status') > 2:
                        logger.info(f"{self.session_name} | Stars already claimed | Skipping....")

                    elif data_stars.get('status') < 3 and datetime.fromisoformat(data_stars.get('endTime')) > datetime.now():
                        start_stars_claim = await self.start_stars_claim(http_client=http_client, data={'task_id': data_stars.get('taskId')})
                        claim_stars = await self.claim_task(http_client=http_client, data={'task_id': data_stars.get('taskId')})
                        if claim_stars is not None and claim_stars.get('status') == 0 and start_stars_claim is not None and start_stars_claim.get('status') == 0:
                            logger.info(f"{self.session_name} | Claimed stars | Stars: <light-red>+{start_stars_claim['data'].get('stars', 0)}</light-red>")
                    
                    next_stars_check = int(datetime.fromisoformat(get_stars['data'].get('endTime')).timestamp())

            await asyncio.sleep(1.5)

            if settings.AUTO_CLAIM_COMBO and next_combo_check < time():
                combo_info = await self.get_combo(http_client)
                combo_info_data = combo_info.get('data', [])[0] if combo_info.get('data') else []

                if combo_info is not None and combo_info.get('status') == 0 and combo_info_data:
                    if combo_info_data.get('status') > 0:
                        logger.info(f"{self.session_name} | Combo already claimed | Skipping....")
                    elif combo_info_data.get('status') == 0 and datetime.fromisoformat(
                            combo_info_data.get('end')) > datetime.now():
                        claim_combo = await self.claim_task(http_client, data = { 'task_id': combo_info_data.get('taskId') })

                        if claim_combo is not None and claim_combo.get('status') == 0:
                            logger.info(
                                f"{self.session_name} | Claimed combo | Points: <light-red>+{combo_info_data.get('score')}</light-red> | Combo code: <light-red>{combo_info_data.get('code')}</light-red>")
                    
                    next_combo_check = int(datetime.fromisoformat(combo_info_data.get('end')).timestamp())

            await asyncio.sleep(1.5)


            if settings.AUTO_DAILY_REWARD:
                claim_daily = await self.claim_daily(http_client=http_client)
                if claim_daily.get("status", 400) != 400:
                    logger.info(f"{self.session_name} | Daily: <light-red>{claim_daily['data']['today_game']}</light-red> reward: <light-red>{claim_daily['data']['today_points']}</light-red>")

            await asyncio.sleep(1.5)

            if settings.AUTO_PLAY_GAME:
                available_tickets = balance.get('data').get('play_passes')
                tickets = available_tickets

                logger.info(f"{self.session_name} | Tickets: <light-red>{available_tickets}</light-red>")

                await asyncio.sleep(1.5)

                while tickets > 0:
                    logger.info(f"{self.session_name} | Start game...")
                    play_game = await self.play_game(http_client=http_client)
                    if play_game.get('status') == 0:
                        logger.info(f"{self.session_name} | Game in progress...")

                        await asyncio.sleep(30)
                        claim_game = await self.claim_game(http_client=http_client, points=randint(400, 600))

                        if claim_game.get('status') == 0:
                            logger.info(f"{self.session_name} | Game finish! Claimed points: <light-red>{claim_game.get('data').get('points')}</light-red>")
                            tickets -= 1
                            await asyncio.sleep(1.5)

            if settings.AUTO_TASK:
                logger.info(f"{self.session_name} | Start checking tasks.")
                tasks = await self.get_tasks(http_client=http_client)

                tasks_list = []
                if tasks is not None and tasks.get("status", 500) == 0:
                    for values in tasks["data"].values():
                        for task in values:
                            if task.get('enable'):
                                if task.get('startTime') and task.get('endTime'):
                                    task_start = convert_to_local_and_unix(task['startTime'])
                                    task_end = convert_to_local_and_unix(task['endTime'])
                                    if task_start <= time() <= task_end:
                                        tasks_list.append(task)
                                elif task.get('type') != 'wallet':
                                    tasks_list.append(task)
                
                for task in tasks_list:
                    wait_second = task.get('waitSecond', 0)
                    starttask = await self.start_task(http_client=http_client, data={'task_id': task['taskId']})
                    if starttask is not None and starttask.get('data') and starttask.get('data', {}).get('status', 3) != 3:
                        logger.info(f"{self.session_name} | Start task <light-red>{task['name']}.</light-red> Wait {wait_second}s 🍅")
                        await asyncio.sleep(wait_second)
                        await self.check_task(http_client=http_client, data={'task_id': task['taskId']})                    
                        claim = await self.claim_task(http_client=http_client, data={'task_id': task['taskId']})
                        if claim['status'] == 0:
                            logger.info(f"{self.session_name} | Task <light-red>{task['name']}</light-red> claimed! 🍅")
                            await asyncio.sleep(2)
                        else:
                            logger.info(f"{self.session_name} | Task <light-red>{task['name']}</light-red>not claimed! 🍅")
                            await asyncio.sleep(2)
                
            if http_client and not http_client.closed:
                await http_client.close()
                if proxy_conn and not proxy_conn.closed:
                        proxy_conn.close()
                        
            sleep_time = end_farming_dt - time()
            logger.info(f'{self.session_name} | Sleep <light-red>{round(sleep_time / 60, 2)}m.</light-red>')
            await asyncio.sleep(sleep_time)
                


async def run_tapper(tg_client: Client, proxy: str | None):
    try:
        await Tapper(tg_client=tg_client, proxy=proxy).run()
    except InvalidSession:
        logger.error(f"{tg_client.name} | Invalid Session")
