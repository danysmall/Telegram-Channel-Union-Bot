from telethon import TelegramClient
import asyncio
import typing


class BotFather():

    def __init__(
        self: 'BotFather',
        settings_file: str,
        divider: str = '='
    ) -> None:
        """Init settings of object."""
        self._settings_set = (
            'API_ID',
            'API_HASH',
            'BOT_TOKEN',
            'SESSION_NAME'
        )

        self._settings_file = settings_file
        self._divider = divider

        self._settings = self._get_settings()
        if self._settings is None:
            raise SystemExit
        elif not self._check_settings_for_valid():
            raise SystemExit()

    def _get_settings(self: 'BotFather') -> typing.Union[dict, None]:
        """Get settings from file."""
        # Try to read settings file if it exists
        try:
            with open(self._settings_file, 'r') as file:
                result = dict()

                for line in file:
                    print(line)
                    try:
                        key, value = line.split(self._divider)
                        result[key] = value.strip()
                    except ValueError as error:
                        self._send_logs('error', error)
                        return None

                # If everything is ok
                return result

        # If we got exception
        except FileNotFoundError as error:
            self._send_logs('error', error)
            return None

    def _check_settings_for_valid(self: 'BotFather') -> bool:
        try:
            for key in self._settings:
                if key not in self._settings_set:
                    return False
        except NameError as error:
            self._send_logs('error', error)
            return False

        return True

    def _send_logs(self: 'BotFather', message_id: str, message: str) -> None:
        if message_id == 'error':
            print(message)

    async def _serve_forever(self: 'BotFather'):
        async with await TelegramClient(
            self._settings['SESSION_NAME'],
            self._settings['API_ID'],
            self._settings['API_HASH']
        ).start() as client:
            info = await client.get_me()
            print(info)

    def start(self: 'BotFather'):
        asyncio.run(self._serve_forever())
