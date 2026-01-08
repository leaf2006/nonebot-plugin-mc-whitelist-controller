from nonebot import require
import json
import os
from pathlib import Path

import nonebot_plugin_localstore as store

class user_config:
    config_dir = store.get_plugin_config_dir() # 插件配置文件存储位置
    config_file_path = Path(store.get_config_file(config_dir, "config.json"))  # 将字符串转换为Path对象

    data_dir = store.get_plugin_data_dir() # 插件生成的玩家profile存储位置
    data_file_path = Path(store.get_data_file(data_dir, "profile.json"))

    if not config_file_path.exists():
        default_data = {
            "whitelist_path": "",
            "profile_path": "",
            "server_status": "offline",
            "administrator_id": []
        }
        config_file_path.write_text(json.dumps(default_data, ensure_ascii=False, indent=4), encoding="utf-8")
    else:
        pass

    content = config_file_path.read_text(encoding='utf-8')
    config_file = json.loads(content)

    whitelist_path = config_file['whitelist_path']

    profile_path_config = config_file['profile_path']
    if not profile_path_config or (isinstance(profile_path_config, str) and profile_path_config.strip() == ""):
        profile_path = str(data_file_path) # 转换为字符串
        
    else:
        profile_path = str(profile_path_config)

    server_status = config_file['server_status']
    administrator_id = config_file['administrator_id']
    

