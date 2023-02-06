import os

import nonebot
from nonebot.adapters import onebot

nonebot.init()
nonebot.load_from_toml("pyproject.toml")
nonebot.load_builtin_plugin("echo")
app = nonebot.get_asgi()
driver = nonebot.get_driver()
driver.register_adapter(onebot.V11Adapter)
#nonebot.load_plugins(os.path.join(os.path.dirname(__file__), "KQN_Bot\plugins"))

nonebot.run()