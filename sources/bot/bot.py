from telethon import TelegramClient
import asyncio


class BotFather():

    def __init__(
        self: 'BotFather',
        session_name: str,
        api_id: int,
        api_hash: str
    ) -> None:
        """Init settings of object."""
        self._api_id = api_id
        self._api_hash = api_hash
        self._session_name = session_name

    async def _serve_forever(self: 'BotFather'):
        async with await TelegramClient(
            self._session_name,
            self._api_id,
            self._api_hash
        ).start() as client:
            info = await client.get_me()
            print(info)

    def start(self: 'BotFather'):
        asyncio.run(self._serve_forever())
