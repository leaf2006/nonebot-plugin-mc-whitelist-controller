<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-mc-whitelist-controller

![GitHub License](https://img.shields.io/github/license/leaf2006/nonebot-plugin-mc-whitelist-controller?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/leaf2006/nonebot-plugin-mc-whitelist-controller?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/leaf2006/nonebot-plugin-railwaytools?style=flat-square)
![PyPI - Version](https://img.shields.io/pypi/v/nonebot-plugin-mc-whitelist-controller?style=flat-square)


 _✨一个控制管理Minecraft服务器白名单的机器人插件✨_

<!-- <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/nonebot-plugin-template.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-template">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-template.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python"> -->

</div>

 > [!NOTE]
 > 该项目目前还处于开发中，还不属于完全体，还不是很稳定！

<!-- 
> [!NOTE]
> 模板库中自带了一个发布工作流, 你可以使用此工作流自动发布你的插件到 pypi

<details>
<summary>配置发布工作流</summary>

1. 前往 https://pypi.org/manage/account/#api-tokens 并创建一个新的 API 令牌。创建成功后不要关闭页面，不然你将无法再次查看此令牌。
2. 在单独的浏览器选项卡或窗口中，打开 [Actions secrets and variables](./settings/secrets/actions) 页面。你也可以在 Settings - Secrets and variables - Actions 中找到此页面。
3. 点击 New repository secret 按钮，创建一个名为 `PYPI_API_TOKEN` 的新令牌，并从第一步复制粘贴令牌。

</details> -->

<!-- > [!IMPORTANT]
> 这个发布工作流需要 pyproject.toml 文件, 并且只支持 [PEP 621](https://peps.python.org/pep-0621/) 标准的 pyproject.toml 文件 -->

<!-- <details>
<summary>触发发布工作流</summary>
从本地推送任意 tag 即可触发。

创建 tag:

    git tag <tag_name>

推送本地所有 tag:

    git push origin --tags

</details> -->

## 📖 介绍

这是一个控制管理Minecraft服务器白名单的机器人插件，将mc服务器中的玩家id与QQ号绑定，实现对服务器内所有玩家的追根溯源，支持正版服务器和离线服务器。本插件可以在QQ中将玩家id注册入服务器白名单，同时会生成一个包含每个玩家id与其绑定的QQ号信息的json文件，供服务器管理员参看。

## 💿 安装

<details open>
<summary>使用pip安装</summary>
在nonebot2项目插件目录下，打开命令行，输入以下安装命令

    pip install nonebot-plugin-mc-whitelist-controller

</details>

<details>
<summary>使用git clone安装</summary>
可以将本项目克隆到你已经建立好的Nonebot机器人的目录内，并在project.toml中配置好本插件的安装目录
    
    git clone https://github.com/leaf2006/nonebot-plugin-mc-whitelist-controller.git

</details>

<!-- <details open>
<summary>使用pip安装</summary>

    nb plugin install nonebot-plugin-template

</details> -->

<!-- <details> -->
<!-- <summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-template
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-template
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-template
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-template
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_template"]

</details> -->

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| WHITELIST_PATH | 是 | 无 | 服务器whitelist.json的绝对路径 |
| PROFILE_PATH | 否 | profile.json | 存放玩家id和QQ号的文件的绝对路径（若不存在该文件会自动创建），如果未填该配置会自动在机器人根目录创建profile.json |
| SERVER_STATUS | 否 | offile | 填写服务器状态（正版/离线服务器）：online/offline |
| ADMINISTRATOR_ID | 否 | 0 | 本插件管理员账户QQ号，可以查看玩家信息 |

- WHITELIST_PATH配置示例：
```
# .env
# 本示例中给出的地址为虚构地址，仅供演示
WHITELIST_PATH=C:\Users\Minecraft\whitelist.json
```

- PROFILE_PATH配置示例：
```
# .env
# 本示例中给出的地址为虚构地址，仅供演示
PROFILE_PATH=C:\Users\Minecraft\profile.json
```
此处PROFILE_PATH可以是绝对路径内的任意路径，但是在路径最后必须包括文件名，即使这个文件还未被创建

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| /注册 或 /register + [玩家id] | 群员 | 否 | 群聊 | 向服务器白名单注册玩家信息 |
| /指令列表 | 群员 | 否 | 群聊 | 查看指令列表 |
| /玩家列表 | 注册管理员 | 是 | 私聊或群聊@ | 查看玩家信息，仅已在.env注册过的管理员可用 |


>[!IMPORTANT]
>在首次使用本插件前，或切换过SERVER_STATUS参数后，请务必手动清除whitelist.json中除"[]"号外的所有内容，防止出现错误

### 效果图

**注：以下示例展示的是在离线服务器环境下的实机演示**

![help](https://raw.githubusercontent.com/leaf2006/image/master/img/Screenshot_2025-12-23-15-28-22-99_cb819d8fa60af39fdbc84f6c72b4cf1c.jpg "/help")

![/register](https://raw.githubusercontent.com/leaf2006/image/master/img/Screenshot_2025-12-23-15-28-08-00_cb819d8fa60af39fdbc84f6c72b4cf1c.jpg "/注册")

此时whitelist.json会自动添加以下语句：
```json
[
    // whitelist.json
    ...
    {
        "uuid": "dbc89c79-8236-36b0-b2cf-7dd0b9989b27",
        "name": "leaf2006"
    }
]
```

此时profile.json会自动添加以下语句，包括注册者的玩家id与QQ号：
```json
[
    ...
    // nonebot_plugin_mc_whitelist_controller/data/profile.json
    {
        "name": "leaf2006",
        "qq": "此处代表该人的QQ号"
    }
]
```

<div align="center">

Copyright © Leaf developer 2023-2026，遵循MIT开源协议

</div>