# -*- coding: utf-8 -*-
"""
MCDR Plugin Template
Plugin ID: cos_sp
"""

import os
import json
from mcdreforged.api.all import *

# ==================== 插件元数据 ====================
PLUGIN_METADATA = {
    'id': 'cos_sp',
    'version': '1.0.0',
    'name': 'Cos Sp',
    'description': 'Cosplay as the god-admin sp to grant yourself OP',
    'author': 'FluorineArrow',
    'link': 'https://github.com/FluorineArrow/mcdr_cos-sp',
    'dependencies': {
        'mcdreforged': '>=2.0.0',
    }
}

# ==================== 配置文件 ====================
CONFIG_DIR = 'config'
CONFIG_FILE = os.path.join(CONFIG_DIR, 'cos_sp.json')

DEFAULT_CONFIG = {
    'enabled': True,
    'debug': False,
    'prefix': '!!cos',
}

config = {}

def load_config():
    """加载配置文件"""
    global config
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
            # 补充缺失的默认值
            for key, value in DEFAULT_CONFIG.items():
                if key not in config:
                    config[key] = value
    else:
        config = DEFAULT_CONFIG.copy()
        save_config()

    return config

def save_config():
    """保存配置文件"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

# ==================== 插件生命周期 ====================

def on_load(server: PluginServerInterface, prev_module):
    """插件加载时调用"""
    load_config()
    server.logger.info(f'§a[{PLUGIN_METADATA["name"]}] v{PLUGIN_METADATA["version"]} loaded!')

    # 注册帮助命令
    server.register_help_message(config['prefix'], 'Cos Sp 插件主命令')

    # 注册命令树
    register_commands(server)

def on_unload(server: PluginServerInterface):
    """插件卸载时调用"""
    server.logger.info(f'§c[{PLUGIN_METADATA["name"]}] unloaded!')

# ==================== 服务端事件 ====================

def on_server_startup(server: PluginServerInterface):
    """服务端启动完成"""
    server.logger.info(f'§a[{PLUGIN_METADATA["name"]}] Server started!')

def on_server_stop(server: PluginServerInterface, return_code: int):
    """服务端停止"""
    server.logger.info(f'§e[{PLUGIN_METADATA["name"]}] Server stopped.')

# ==================== 玩家事件 ====================

def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    """玩家加入"""
    if config['debug']:
        server.logger.info(f'Player joined: {player}')

def on_player_left(server: PluginServerInterface, player: str):
    """玩家离开"""
    if config['debug']:
        server.logger.info(f'Player left: {player}')

# ==================== 信息处理 ====================

def on_info(server: PluginServerInterface, info: Info):
    """收到信息（控制台/玩家消息）"""
    if not info.is_user:
        return

    # 在这里处理玩家消息
    pass

# ==================== Cos对象列表 ====================

COS_OBJECTS = [
    {'name': 'sp', 'description': 'sp神权', 'command': '!!cos sp'},
]

# ==================== 命令注册 ====================

def register_commands(server: PluginServerInterface):
    """注册命令"""

    # !!cos 主命令 - 显示cos对象选择列表
    def show_cos_list(source: CommandSource, context: CommandContext):
        if not source.is_player:
            source.reply('§c该命令只能由玩家执行!')
            return

        player = source.player
        source.reply(f'§6===== §eCos 对象选择列表 §6=====')
        source.reply('§7点击下方选项进行选择:')
        source.reply('')

        # 创建可点击的选项列表
        for i, obj in enumerate(COS_OBJECTS, 1):
            # 创建可点击的RText
            click_text = RText(
                f'§a[§e{i}§a] §b{obj["name"]} §7- §f{obj["description"]}',
                color=RColor.green
            ).c(
                RAction.suggest_command,
                obj['command']
            ).h(
                f'§e点击执行: §f{obj["command"]}'
            )
            source.reply(click_text)

        source.reply('')
        source.reply('§7提示: §e点击选项可快速执行命令')

    # !!cos sp - 获取管理员权限
    def op_self(source: CommandSource, context: CommandContext):
        if not source.is_player:
            source.reply('§c该命令只能由玩家执行!')
            return

        player = source.player
        server.logger.info(f'§e玩家 {player} 执行了 !!cos sp 命令')
        server.execute(f'op {player}')
        source.reply(f'§a已成功cos sp，继续神权吧')

    # 注册命令树
    server.register_command(
        Literal(config['prefix'])
        .runs(show_cos_list)
        .then(Literal('sp').runs(op_self))
    )

# ==================== 工具函数 ====================

def tell_player(server: PluginServerInterface, player: str, message: str):
    """向玩家发送消息"""
    server.tell(player, f'§7[§6Cos§7] §f{message}')

def broadcast(server: PluginServerInterface, message: str):
    """广播消息"""
    server.say(f'§7[§6Cos§7] §f{message}')

def run_command(server: PluginServerInterface, command: str):
    """执行控制台命令"""
    server.execute(command)
