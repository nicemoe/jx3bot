from os import path
import nonebot
import config

nonebot.init(config)
nonebot.load_plugins(
    path.join(path.dirname(__file__), 'plugin'),
    'plugin'
)
bot = nonebot.get_bot()
app = bot.asgi

if __name__ == '__main__':
    nonebot.run()
