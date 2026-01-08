import json
from .data_source import user_config as uc

def check_username_exists(username: str) -> str:
    """
    检查玩家名是否已经被注册过，注册过则返回True，反则返回False
    """

    try:
        path = uc.whitelist_path
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

def check_profile_exists(username: str) -> str:
    """
    检查玩家档案是否已经被注册过，注册过则返回True，反则返回False
    """

    try:
        path = uc.profile_path
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

def get_player_in_profile(player_name: str):
    """在profile.json中查找玩家数据"""
    profile_path = uc.profile_path
    try:
        with open(profile_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            return None

        for item in data:
            if isinstance(item, dict) and item.get('name') == player_name:
                return item

        return None
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None