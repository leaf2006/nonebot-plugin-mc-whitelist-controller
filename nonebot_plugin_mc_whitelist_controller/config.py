from pydantic import BaseModel
from nonebot import get_driver

class Config(BaseModel):
    """Plugin Config Here"""
    whitelist_path: str="" # 白名单地址
    profile_path:str="profile.json"
    server_status: str="offline" # 切换正版验证/离线模式
    administrator_id:int="0" # 管理员QQid

