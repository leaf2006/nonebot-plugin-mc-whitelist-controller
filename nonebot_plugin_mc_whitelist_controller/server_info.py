import os
import json
from mcstatus import JavaServer # mcstatus查询服务器情况
from nonebot import on_command   # type: ignore
from nonebot.adapters.onebot.v11 import Message, MessageSegment   # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from nonebot.adapters.onebot.v11 import Event
from nonebot.params import CommandArg  # type: ignore
from .data_source import user_config as uc
from nonebot.rule import to_me  # type: ignore

server_info = on_command("服务器信息", aliases={"server_info"}, priority=5, block=True)
@server_info.handle()
async def handle_server_info(args: Message = CommandArg(),event: Event = None):
    address = uc.address # 服务器ip地址（外网）
    address_intranet = uc.address_intranet
    if address == "" or address_intranet == "":
        await server_info.finish("❌请填写address_intranet与address字段！")
    else:            
        java_server = JavaServer.lookup(address_intranet)
        try:
            server_query = java_server.query()
            player_list = server_query.players.list # 玩家列表
            player_count = f"{server_query.players.online}/{server_query.players.max}" # 玩家数量/最大容纳量
            server_version = server_query.software.version # 服务器游戏版本

            player_output = ""
            for players in player_list:
                player_output += f"{players}\n"
            if player_output == "":
                player_output = "游戏内暂无玩家\n"

            server_info_output = Message ([
                f"服务器IP地址：{address}\n",
                f"服务器游戏版本：{server_version}\n",
                f"玩家数量：{player_count}\n\n",
                "----------玩家列表----------\n",
                player_output,
                "------------------------------\n",
                "新玩家请输入“/注册 + [玩家id]”向白名单注册，方可进入服务器"
            ])
            await server_info.finish(server_info_output)

        except TimeoutError:
            error_msg = Message ([
                "❌无法查询到服务器信息！可能因为以下原因导致：\n",
                "------------------------------\n",
                "1.服务器可能未开启\n",
                "2.address_intranet配置项可能填写错误\n",
                "------------------------------\n"
                "请联系服务器管理员进行排查"
            ])
            await server_info.finish(error_msg)