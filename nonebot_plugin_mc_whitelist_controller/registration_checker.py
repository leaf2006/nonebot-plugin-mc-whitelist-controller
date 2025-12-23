import json
from .config import Config
from nonebot import get_plugin_config

plugin_config = get_plugin_config(Config)
def check_username_exists(username: str) -> str:
    """
    检查玩家名是否已经被注册过
    """

    try:
        # path = 'nonebot_plugin_mc_whitelist_controller/data/profile.json'
        path = plugin_config.whitelist_path
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        # 检查数据结构
        if isinstance(data, list):
            # 如果是列表，检查每个元素
            for item in data:
                if isinstance(item, dict) and item.get('name') == username:
                    return True
        elif isinstance(data, dict):
            # 如果是字典，检查键值
            if username in data.values():
                return True
            
        return False
        
    except FileNotFoundError:
        # 文件不存在，默认返回no
        return False
    except json.JSONDecodeError:
        # JSON格式错误，可以考虑抛出异常或返回默认值
        return False
