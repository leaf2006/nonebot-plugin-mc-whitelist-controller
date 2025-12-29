from nonebot import get_plugin_config
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.plugin import PluginMetadata
from .register import register_id
from .unregister import unregister_id
from .profile import profile_list
from .config import Config
from nonebot import logger

__plugin_meta__ = PluginMetadata(
    name="mc服务器白名单在线注册器",
    description="这是一个控制管理Minecraft服务器白名单的机器人插件，将mc服务器中的玩家id与QQ号绑定，实现对服务器内所有玩家的追根溯源",
    usage="""
    /注册 + [玩家id] - 向服务器白名单注册玩家信息（会自动获取发消息者的QQ号进行绑定）
    /注销 + [玩家id] - 注销已注册的玩家信息
    /指令列表：查看帮助信息
    /玩家列表：管理员专用指令，查看已注册玩家信息
    """,
    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="https://github.com/leaf2006/nonebot-plugin-mc-whitelist-controller",
    # 发布必填。

    config=Config,
    # 插件配置项类，如无需配置可不填写。

    supported_adapters={"~onebot.v11"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
    extra={
        "author": "leaf2006",
        "version": "1.0.0",
    },
)

information_helper = on_command("指令列表",priority=5,block=True)

@information_helper.handle()
async def handle_information_helper():
    info_Helper_message = Message([
        "✨这是一个控制管理Minecraft服务器白名单的机器人插件，将mc服务器中的玩家id与QQ号绑定，实现对服务器内所有玩家的追根溯源，支持正版服务器和离线服务器。本插件可以在QQ中将玩家id注册入服务器白名单，同时会生成一个包含每个玩家id与其绑定的QQ号信息的json文件，供服务器管理员参看。✨\n \n",
        "✍指令列表：✍ \n",
        "① /注册 或 /register + [玩家id]：向服务器白名单注册玩家信息（会自动获取发消息者的QQ号进行绑定） \n",
        "② /注销 或 /unregister + [玩家id]：注销已注册的玩家信息，注销后将无法进入服务器，直至再次注册",
        "③ /指令列表：查看帮助信息 \n",
        "④ /玩家列表：管理员专用指令，查看已注册玩家信息 \n \n",
        "Powered by Nonebot2\n",
        "Copyright © Leaf developer 2023-2026"
    ]) #type:ignore

    await information_helper.finish(info_Helper_message)

# 警告，启动时会显示一遍
warning_info = """
****************************************************************
在首次使用本插件前，或切换过SERVER_STATUS参数后，请务必手动清除whitelist.json中除"[]"号外的所有内容，防止出现错误！
**************************************************************** 
"""

logger.warning(warning_info)

