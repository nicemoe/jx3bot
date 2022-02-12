from nonebot.default_config import *

HOST = '0.0.0.0'  # NoneBot 的 HTTP 和 WebSocket 服务端监听的 IP／主机名。
PORT = 8080  # NoneBot 的 HTTP 和 WebSocket 服务端监听的端口。
DEBUG = False  # 是否以调试模式运行，生产环境需要设置为 False 以提高性能。
SUPERUSERS = {22282320}  # 超级用户的 QQ 号，用于命令的权限检查。
NICKNAME = {'萌萌'}  # 机器人的昵称，用于辨别用户是否在和机器人说话。
COMMAND_START = {'', '/', '!', '／', '！'}  # 命令的起始标记，用于判断一条消息是不是命令。
ACCESS_TOKEN = ''  # 需要和 CQ HTTP 插件的配置中的 access_token 相同。
COMMAND_SEP = {'.'}  # 命令的分隔标记，用于将文本形式的命令切分为元组（实际的命令名）。

MYSQL_CONFIG = {
    'host': 'localhost',  # 连接主机名。
    'user': 'root',  # 用户账号
    'password': '',  # 用户密码
    'db': 'nonebot',  # 数据库名
    'port': 3306,  # 连接端口
    'charset': 'utf8',  # 数据编码
    'minsize': 12,  # 连接池最小值
    'maxsize': 96,  # 连接池最大值
    'autocommit': True,  # 自动提交模式
}
