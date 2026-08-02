<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-mc-whitelist-controller

![GitHub License](https://img.shields.io/github/license/leaf2006/nonebot-plugin-mc-whitelist-controller?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/leaf2006/nonebot-plugin-mc-whitelist-controller?style=flat-square)
![PyPI - Version](https://img.shields.io/pypi/v/nonebot-plugin-mc-whitelist-controller?style=flat-square)

✨一个通过 QQ 管理 Minecraft 服务器白名单的 NoneBot2 插件✨

</div>

## 📖 简介

将 Minecraft 玩家 ID 与 QQ 号绑定，在 QQ 中完成白名单注册与注销，并实现对服务器内玩家的追根溯源。支持正版（online）与离线（offline）服务器，注册记录会持久化到本地 JSON 文件，供管理员随时查看。

> [!IMPORTANT]
> 使用前请务必阅读「使用前配置」与「Bot 配置」两部分内容。插件正常工作需要你对 MC 服务器做少量配置，并为 Bot 填写必要的配置项。

## 功能特性

- 在 QQ 中注册 / 注销玩家白名单，自动绑定发送者的 QQ 号
- 自动生成并维护玩家 ID 与 QQ 号的绑定文件
- 支持正版（online）与离线（offline）服务器
- 管理员可查看全部已注册玩家的 ID 与 QQ 信息
- 查询服务器实时状态与在线玩家列表

## 🔨 依赖

- Python >= 3.9
- nonebot2 + nonebot-adapter-onebot
- httpx >= 0.22.0
- nonebot-plugin-localstore >= 0.7.4

本插件涉及到修改MC服务端的文件，因此MC服务端与Nonebot必须在同一机器内运行

## 💿 安装

**方式一：pip 安装**

在 nonebot2 项目目录下执行：

```bash
pip install nonebot-plugin-mc-whitelist-controller
```

**方式二：git clone 安装**

克隆到已建好的 NoneBot 项目目录，并在 `pyproject.toml` 中配置插件安装路径：

```bash
git clone https://github.com/leaf2006/nonebot-plugin-mc-whitelist-controller.git
```

## ⚠️ 使用前配置

白名单文件更新后不会立即生效，需要在服务器中执行 `/whitelist reload` 才会重新加载。请选择以下任一方式让服务器自动重载白名单：

- **定时任务（推荐）**：大多数控制面板 / 面板服都支持定时任务。添加一个每 900 秒（15 分钟）执行一次 `/whitelist reload` 的任务即可。

  ![server-timer](https://raw.githubusercontent.com/leaf2006/image/master/img/server-timer.png)

- **白名单监听 Mod（试验性）**：作者维护的 [Minecraft Whitelist Watcher](https://github.com/leaf2006/minecraft-whitelist-watcher-mod) Fabric Mod 会在白名单文件变动时自动重载，目前支持的 MC 版本较少，仍在持续更新。

## ⚙️ Bot 配置

插件基于 [nonebot-plugin-localstore](https://github.com/nonebot/plugin-localstore) 存储配置文件 `config.json`，默认位置：

- Windows：`C:\Users\<username>\AppData\Roaming\nonebot2\nonebot_plugin_mc_whitelist_controller`
- Linux：`~/.config/nonebot2/nonebot_plugin_mc_whitelist_controller`

不确定位置时，可在 Bot 根目录执行 `nb localstore` 查看。

首次运行 Bot 后，插件会自动在上述目录生成 `config.json` 模板；若未生成，可手动创建并按以下字段填写：

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| whitelist_path | 是 | 无 | 服务器 whitelist.json 的绝对路径 |
| profile_path | 否 | 无 | 玩家 ID 与 QQ 绑定文件路径（不存在会自动创建），留空时使用 localstore 默认目录 |
| server_status | 否 | offline | 服务器类型：online（正版）/ offline（离线） |
| administrator_id | 否 | [] | 管理员 QQ 号，可配置多个，用于「玩家列表」等管理指令 |
| address_intranet | 否 | 127.0.0.1:25565 | 服务器内网地址，用于在「服务器信息」中查询 |
| address | 否 | 无 | 服务器地址，用于在「服务器信息」中展示

```json
{
    "whitelist_path": "C:\\Users\\Minecraft\\whitelist.json",
    "profile_path": "",
    "server_status": "offline",
    "administrator_id": [1111111111, 2222222222],
    "address_intranet": "127.0.0.1:25565",
    "address": "example.org"
}
```

> [!IMPORTANT]
> 填写文件路径时请使用 `/` 或 `\\` 作为分隔符，不要使用单个 `\`，避免解析出错。
> profile_path 的路径末尾必须包含文件名（即使该文件尚未创建）。

## 🚀 使用

### 指令列表

| 指令 | 权限 | 需要 @ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| /注册 或 /register + [玩家id] | 群员 | 否 | 群聊 | 注册玩家并绑定当前 QQ 号 |
| /注销 或 /unregister + [玩家id] | 群员 | 否 | 群聊 | 注销玩家，仅限本人或管理员 |
| /指令列表 | 群员 | 否 | 群聊 | 查看帮助信息 |
| /服务器信息 或 /server_info | 群员 | 否 | 群聊 | 查看服务器状态与在线玩家 |
| /玩家列表 或 /list | 管理员 | 是 | 私聊 / 群聊 | 查看全部已注册玩家的 ID 与 QQ |

### 使用效果

注册玩家 `leaf2006`：

```
🤵：/注册 leaf2006
🤖：成功注册玩家leaf2006到白名单！
```

注册后，whitelist.json 会新增该玩家条目：

```json
[
    {
        "uuid": "dbc89c79-8236-36b0-b2cf-7dd0b9989b27",
        "name": "leaf2006"
    }
]
```

同时 profile.json 会记录玩家 ID 与 QQ 号的绑定关系：

```json
[
    {
        "name": "leaf2006",
        "qq": "此处为该玩家 QQ 号"
    }
]
```

> [!IMPORTANT]
> 首次使用本插件，或切换过 server_status 配置后，请先手动将 whitelist.json 清空为 `[]`，避免数据异常。
>
> 以上示例为离线服务器场景。

## 📦 旧版本

历史版本请前往 [PyPI](https://pypi.org/project/nonebot-plugin-mc-whitelist-controller/#history) 查看。

<div align="center">

Copyright © Leaf developer 2023-2026，遵循 MIT 开源协议

</div>
