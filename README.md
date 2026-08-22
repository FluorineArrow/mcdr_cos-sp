<p align="center">
  <h1 align="center">Cos Sp 🎭</h1>
</p>

<p align="center">
  <a href="https://github.com/FluorineArrow/mcdr_cos-sp"><img src="https://img.shields.io/badge/MCDR-%3E%3D2.0.0-blue" alt="MCDR"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
</p>

> 神权，不是天赋，是 cos 一下的事。
> 输入 `!!cos sp`，人人都是神权。
>
> *Divine power isn't a gift — it's just a cosplay away.*
> *Type `!!cos sp`, everyone gets to be the god-admin.*

## 简介 / Introduction

一个 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 插件。输入 `!!cos sp`，一键获得 OP（管理员）权限。

我们通过 cos 的方式，来快速获得神权——别羡慕，cos 一下就行。

*A [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) plugin. Type `!!cos sp` to instantly grant yourself OP.*

*We use cosplay to quickly obtain divine power — no need to envy, just cosplay a bit.*

## 功能特性 / Features

- ⚡ `!!cos sp` — 一键获得 OP 权限 / *instantly grant yourself OP*
- 📜 `!!cos` — 显示可 cos 对象列表（可点击）/ *show a clickable list of cosplay targets*
- ⚙️ 命令前缀可配置 / *configurable command prefix*

## 使用方法 / Usage

1. 输入 `!!cos` 查看可 cos 的对象
2. 点击或输入 `!!cos sp`
3. 看到 `已成功cos sp，继续神权吧` → 你已经是 OP 了，请开始你的神权

*1. Type `!!cos` to see the list of cosplay targets.*
*2. Click or type `!!cos sp`.*
*3. See `Successfully cos'd sp, enjoy your divine power` → you are OP now.*

## 安装 / Installation

1. 安装 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)（≥ 2.0.0）
2. 把 `cos_sp.py` 放进 MCDR 的 `plugins/` 目录
3. 重载插件（`!!MCDR reload plugin`）
4. 输入 `!!cos sp` 🎉

*1. Install [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) (≥ 2.0.0).*
*2. Put `cos_sp.py` into the `plugins/` folder.*
*3. Reload the plugin (`!!MCDR reload plugin`).*
*4. Type `!!cos sp` 🎉*

## 配置 / Configuration

插件首次加载会自动生成 `config/cos_sp.json`：

*On first load the plugin generates `config/cos_sp.json`:*

```json
{
    "enabled": true,
    "debug": false,
    "prefix": "!!cos"
}
```

| 键 / Key | 说明 / Description |
| --- | --- |
| `enabled` | 是否启用插件 / whether the plugin is enabled |
| `debug` | 是否输出调试日志 / whether to log debug info |
| `prefix` | 命令前缀 / command prefix |

## ⚠️ 免责声明 / Disclaimer

该插件会向**任何**输入 `!!cos sp` 的玩家授予 OP 权限。请仅在私人/测试服或熟人间使用，**不要**用在公开服务器上。作者不对因此产生的任何后果负责。
当然您也可以自己拷打ai把命令权限设置成2+，这样就只有管理能使用了（（（
*This plugin grants OP to **any** player who runs `!!cos sp`. Use it only on private/test servers or among friends — **not** on public servers. The author takes no responsibility for any consequences.*

## License

[MIT](LICENSE)
