import hashlib
import httpx
import json
import asyncio
from typing import Optional
import uuid

def get_offline_uuid(username):
    """
    同步获取玩家UUID
    """
    # Minecraft离线UUID使用"OfflinePlayer:"前缀加用户名计算
    input_string = f"OfflinePlayer:{username}"

    # 使用MD5哈希
    hash_bytes = hashlib.md5(input_string.encode('utf-8')).digest()

    # 设置版本位(第13个字节设为3表示版本3)
    hash_bytes = bytearray(hash_bytes)
    hash_bytes[6] = (hash_bytes[6] & 0x0f) | 0x30  # 版本3
    hash_bytes[8] = (hash_bytes[8] & 0x3f) | 0x80  # variant

    # 转换为UUID字符串
    offline_uuid = str(uuid.UUID(bytes=bytes(hash_bytes)))
    return offline_uuid

async def get_online_uuid(username: str) -> Optional[str]:
    """
    异步获取玩家UUID
    """
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                raw_uuid = data.get("id")
                get_online_uuid = raw_uuid[:8] + '-' + raw_uuid[8:12] + '-' + raw_uuid[12:16] + '-' + raw_uuid[16:20] + '-' + raw_uuid[20:]
                return get_online_uuid
            return False
    except Exception:
        return False


