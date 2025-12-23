import json
from nonebot import on_command   # type: ignore
from nonebot.adapters.onebot.v11 import Message, MessageSegment   # type: ignore
from nonebot.plugin import PluginMetadata  # type: ignore
from .config import Config
from nonebot import get_plugin_config
from nonebot.adapters.onebot.v11 import Event
from nonebot.params import CommandArg  # type: ignore
from nonebot.rule import to_me  # type: ignore
from .get_uuid import get_offline_uuid,get_online_uuid
from .registration_checker import check_username_exists

plugin_config = get_plugin_config(Config)

register_id = on_command("注册" , aliases={"register"} , priority=5 , block=True)

@register_id.handle()
async def handle_register_id(args: Message = CommandArg(),event: Event = None):
    if input_id := args.extract_plain_text():

        server_status = plugin_config.server_status

        qq_number = event.get_user_id()
        duplicate_registration_status = check_username_exists(input_id) # 检查用户名是否被注册。被注册：True；未被注册：False

        # 警告
        JsonFormaterror_alert = "JSON文件结构不正确，应该是一个数组。请联系服务器维护者"
        JSONDecodeError_alert = "JSON 格式错误，请确保文件是有效的 JSON 格式"

        
        if duplicate_registration_status == False:
            
            if server_status == "offline": # 离线模式
                # 获取玩家name与uuid并编入json
                player_uuid = get_offline_uuid(input_id)

            elif server_status == "online":
                player_uuid = await get_online_uuid(input_id)
                if player_uuid == False:
                    await register_id.finish("所输入的玩家名不存在，请检查输入是否正确或该玩家名是否为正版账号")

            whitelist_New_entry = { # 写入whitelist.json
                "uuid": player_uuid,
                "name": input_id  
            }

            profile_New_entry = { # 写入profile.json
                "name": input_id,
                "qq": qq_number
            }

            # 写入whitelist.json
            whitelist_path = plugin_config.whitelist_path
            profile_path = 'nonebot_plugin_mc_whitelist_controller/data/profile.json'
            qq_number = event.get_user_id()
            try:
                with open(whitelist_path, 'r', encoding='utf-8') as whitelist:
                    data = json.load(whitelist)

                if isinstance(data,list):
                    data.append(whitelist_New_entry)
                    write_status = True
                else:
                    await register_id.finish(JsonFormaterror_alert)
                
                with open(whitelist_path, 'w',encoding='utf-8') as whitelist:
                    json.dump(data, whitelist, indent=2)

                await register_id.send(f"成功注册玩家{input_id}到白名单！")
            
            except FileNotFoundError:
                await register_id.finish("未找到白名单，请检查是否在.env中添加了正确的whitelist.json文件路径！")
            except json.JSONDecodeError:
                await register_id.finish(JSONDecodeError_alert)

            # 如果write_status(写入状态)为True，代表玩家名已经成功写入whitelist.json，那么就接着将玩家名和QQ号写入profile.json；若没有成功写入，则不进行上述步骤    
            if write_status == True:

                try:
                    with open(profile_path, 'r', encoding='utf-8') as profile:
                        profile_detail = json.load(profile)
                    
                    if isinstance(profile_detail,list):
                        profile_detail.append(profile_New_entry)
                    else:
                        await register_id.finish(JsonFormaterror_alert)
                    
                    with open(profile_path, 'w',encoding='utf-8') as profile:
                        json.dump(profile_detail,profile,indent=2)
                    
                except FileNotFoundError:
                    await register_id.finish("无法向profile.json中添加数据，请检查是否误删插件目录中nonebot_plugin_mc_whitelist_controller/data/profile.json文件！")
                except json.JSONDecodeError:
                    await register_id.finish(JSONDecodeError_alert)
            
            else:
                pass
                  
        else:
            await register_id.finish(f"玩家名{input_id}已被注册！请换个名字重新注册")

    else:
        await register_id.finish("请输入需要注册的玩家名")
        