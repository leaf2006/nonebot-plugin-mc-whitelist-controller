import json
from nonebot import on_command   # type: ignore
from nonebot.adapters.onebot.v11 import Message, MessageSegment   # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from .config import Config
from nonebot import get_plugin_config
from nonebot.adapters.onebot.v11 import Event
from nonebot.params import CommandArg  # type: ignore
from nonebot.rule import to_me  # type: ignore

plugin_config = get_plugin_config(Config)

profile_list = on_command("玩家列表" , aliases={"list"} , priority=5 , block=True , rule=to_me())

@profile_list.handle()
async def handle_profile_list(args: Message = CommandArg(),event: Event = None):
    qq_number = event.get_user_id()
    administrator_id = plugin_config.administrator_id
    
    if administrator_id == [0]:
        await profile_list.finish("你还未启用“查询玩家列表”功能，请去.env配置页面给“ADMINISTRATOR_ID”配置项填写管理员的QQ号，随后方可使用！")
    
    elif int(qq_number) in administrator_id:

        profile_path = plugin_config.profile_path

        with open(profile_path, "r" ,encoding="utf-8") as file:
            parsed_profile = json.load(file)

        profile_output = ""  # 使用新变量名
        count = 1
        for player in parsed_profile:
            name = player['name']
            qq = player['qq']
            profile_output += f"【{str(count)}】玩家id：{name}\nQQ号：{qq}\n"  # 使用新变量名并添加换行
            count += 1

        profile_result = Message([
            "📚️当前服务器白名单已注册玩家\n",
            "------------------------------ \n",
            profile_output,    # 使用新变量名
            "------------------------------",
        ])
        await profile_list.finish(profile_result)
    
    else:
        await profile_list.finish("你没有权限使用“查询玩家列表”功能！")
