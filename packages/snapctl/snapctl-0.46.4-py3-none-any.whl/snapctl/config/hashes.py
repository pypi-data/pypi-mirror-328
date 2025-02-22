'''
This file contains the hashes / list constants
'''
from typing import Dict, List

CLIENT_SDK_TYPES: Dict[str, Dict[str, str]] = {
    'unity': {
        'type': 'csharp',
        'subtype': 'unity',
    },
    'unreal': {
        'type': 'cpp-ue4',
        'subtype': 'unreal',
    },
    'roblox': {
        'type': 'lua',
        'subtype': 'roblox',
    },
    'godot-csharp': {
        'type': 'csharp',
        'subtype': 'godot',
    },
    'godot-cpp': {
        'type': 'cpp-restsdk',
        'subtype': 'godot',
    },
    'cocos': {
        'type': 'cpp-restsdk',
        'subtype': 'cocos',
    },
    'ios-objc': {
        'type': 'objc',
        'subtype': 'ios',
    },
    'ios-swift': {
        'type': 'swift5',
        'subtype': 'ios',
    },
    'android-java': {
        'type': 'android',
        'subtype': 'android',
    },
    'android-kotlin': {
        'type': 'android',
        'subtype': 'android',
    },
    'web-ts': {
        'type': 'typescript-axios',
        'subtype': 'web',
    },
    'web-js': {
        'type': 'javascript',
        'subtype': 'web',
    },
}

SERVER_SDK_TYPES: Dict[str, Dict[str, str]] = {
    'csharp': {
        'type': 'csharp',
        'subtype': '',
    },
    'cpp': {
        'type': 'cpp-restsdk',
        'subtype': '',
    },
    'lua': {
        'type': 'lua',
        'subtype': '',
    },
    'ts': {
        'type': 'typescript-axios',
        'subtype': '',
    },
    'go': {
        'type': 'go',
        'subtype': '',
    },
    'python': {
        'type': 'python',
        'subtype': '',
    },
    'kotlin': {
        'type': 'kotlin',
        'subtype': '',
    },
    'java': {
        'type': 'java',
        'subtype': '',
    },
    'c': {
        'type': 'c',
        'subtype': '',
    },
    'node': {
        'type': 'typescript-node',
        'subtype': '',
    },
    'js': {
        'type': 'javascript',
        'subtype': '',
    },
    'perl': {
        'type': 'perl',
        'subtype': '',
    },
    'php': {
        'type': 'php',
        'subtype': '',
    },
    'clojure': {
        'type': 'clojure',
        'subtype': '',
    },
    'ruby': {
        'type': 'ruby',
        'subtype': '',
    },
    'rust': {
        'type': 'rust',
        'subtype': '',
    },
}

SDK_TYPES: Dict[str, Dict[str, str]] = {**CLIENT_SDK_TYPES, **SERVER_SDK_TYPES}

PROTOS_TYPES: Dict[str, Dict[str, str]] = {
    'cpp': {
        'type': 'cpp',
        'subtype': '',
    },
    'csharp': {
        'type': 'csharp',
        'subtype': '',
    },
    'go': {
        'type': 'go',
        'subtype': '',
    },
    'raw': {
        'type': 'raw',
        'subtype': '',
    },
}

SNAPEND_MANIFEST_TYPES: Dict[str, Dict[str, str]] = {
    'json': {
        'type': 'json',
        'subtype': '',
    },
    'yaml': {
        'type': 'yaml',
        'subtype': '',
    },
}

SERVICE_IDS: List[str] = [
    'analytics', 'auth', 'client-logs', 'events', 'experiments', 'gdpr', 'guilds', 'hades', 'iap',
    'inventory', 'leaderboards', 'matchmaking', 'notifications', 'parties', 'profiles', 'quests',
    'relay', 'remote-config', 'scheduler', 'sequencer', 'social-graph', 'statistics', 'storage',
    'trackables', 'xp'
]

SDK_ACCESS_AUTH_TYPE_LOOKUP: Dict[str, Dict[str, str]] = {
    'user': {
        'access_type': 'external',
        'auth_type': 'user'
    },
    'server': {
        'access_type': 'external',
        'auth_type': 'api-key'
    },
    'internal': {
        'access_type': 'internal',
    },
    'app': {
        'access_type': 'external',
        'auth_type': 'app'
    },
}

DEFAULT_BYOSNAP_DEV_TEMPLATE: Dict[str, object] = {
    'cpu': 100,
    'memory': 0.125,
    'min_replicas': 1,
    'cmd': '',
    'args': [],
    'env_params': [{'key': "SNAPSER_ENVIRONMENT", 'value': "DEVELOPMENT"}]
}

DEFAULT_BYOSNAP_STAGE_TEMPLATE: Dict[str, object] = {
    'cpu': 100,
    'memory': 0.125,
    'min_replicas': 1,
    'cmd': '',
    'args': [],
    'env_params': [{'key': "SNAPSER_ENVIRONMENT", 'value': "STAGING"}]
}

DEFAULT_BYOSNAP_PROD_TEMPLATE: Dict[str, object] = {
    'cpu': 100,
    'memory': 0.125,
    'min_replicas': 2,
    'cmd': '',
    'args': [],
    'env_params': [{'key': "SNAPSER_ENVIRONMENT", 'value': "PRODUCTION"}]
}

ARCHITECTURE_MAPPING: Dict[str, str] = {
    'x86_64': 'amd64',
    'arm64': 'arm64',
    'aarch64': 'arm64',
    'amd64': 'amd64'
}
