import json

from nonebot import get_bot
from nonebot.log import logger
from typing import Union
import random
import httpx

bot = get_bot()
config = bot.config


class Request:
    def __init__(self):
        self.headers = {"User-Agent": f"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50/{list(config.SUPERUSERS)[0]}"}

    async def post(self, url: str, data: dict = None, headers: dict = None, timeout: int = 10) -> str:
        headers = headers if headers else self.headers
        try:
            async with httpx.AsyncClient() as client:
                result = await client.post(url=url, data=data, headers=headers, timeout=timeout)
                return await self.result(result.text)
        except Exception as e:
            logger.error(f"连接网页 {url} 出问题惹！{e}")

    async def get(self, url: str, params: dict = None, headers: dict = None, timeout: int = 10) -> str:
        headers = headers if headers else self.headers
        try:
            async with httpx.AsyncClient() as client:
                result = await client.get(url=url, params=params, headers=headers, timeout=timeout)
                return await self.result(result.text)
        except Exception as e:
            logger.error(f"连接网页 {url} 出问题惹！{e}")

    async def result(self, data: str) -> str:
        try:
            result = json.loads(data)
        except (json.decoder.JSONDecodeError, TypeError):
            return data
        return result
