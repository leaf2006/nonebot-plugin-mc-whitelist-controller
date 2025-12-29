import json
import os
from nonebot import on_command   # type: ignore
from nonebot.adapters.onebot.v11 import Message, MessageSegment   # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from .config import Config
from nonebot import get_plugin_config
from nonebot.adapters.onebot.v11 import Event
from nonebot.params import CommandArg  # type: ignore
from nonebot.rule import to_me  # type: ignore
from .registration_checker import check_profile_exists,get_player_in_profile

plugin_config = get_plugin_config(Config)

unregister_id = on_command("注销", aliases={"unregister"}, priority=5, block=True)

def remove_from_whitelist(player_name: str) -> bool:
    """从whitelist.json中移除指定玩家"""
    whitelist_path = plugin_config.whitelist_path
    try:
        with open(whitelist_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            return False

        # 过滤掉要删除的玩家
        original_length = len(data)
        data = [item for item in data if not (isinstance(item, dict) and item.get('name') == player_name)]

        # 如果没有找到要删除的玩家，长度不会改变
        if len(data) == original_length:
            return False

        with open(whitelist_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        return True
    except FileNotFoundError:
        return False
    except json.JSONDecodeError:
        return False

def remove_from_profile(player_name: str) -> bool:
    """从profile.json中移除指定玩家"""
    profile_path = plugin_config.profile_path
    try:
        with open(profile_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            return False

        # 过滤掉要删除的玩家
        original_length = len(data)
        data = [item for item in data if not (isinstance(item, dict) and item.get('name') == player_name)]

        # 如果没有找到要删除的玩家，长度不会改变
        if len(data) == original_length:
            return False

        with open(profile_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        return True
    except FileNotFoundError:
        return False
    except json.JSONDecodeError:
        return False
@unregister_id.handle()
async def handle_unregister_id(args: Message = CommandArg() , event: Event = None):
    if input_id := args.extract_plain_text():

        qq_number = event.get_user_id()
        duplicate_registration_status = check_profile_exists(input_id)
        
        if duplicate_registration_status == True:
            player_profile = get_player_in_profile(input_id)
            if qq_number != player_profile.get('qq'):
                await unregister_id.finish("您没有权限注销此玩家，只能注销自己的玩家id！")
            
            else:
                profile_Unregister_result = remove_from_profile(input_id)
                whitelist_Unregister_result = remove_from_whitelist(input_id)
                if profile_Unregister_result == True and whitelist_Unregister_result == True:
                    await unregister_id.finish(f"玩家{input_id}注销成功！")
                else:
                    await unregister_id.finish("出现错误，请联系服务器维护者！")

        else:
            await unregister_id.finish(f"玩家名{input_id}未在白名单中注册，无法注销！")
    
    else:
        await unregister_id.finish("请输入需要注销的玩家id！")