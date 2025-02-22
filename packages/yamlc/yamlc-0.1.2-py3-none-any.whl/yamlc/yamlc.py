import yaml
import os
from threading import Lock

class Yamlc:
    _config = None
    _lock = Lock()
    _config_file = "config.yaml"
    @classmethod
    def _load_config(cls):
        with cls._lock:
            if cls._config is None:
                # print("加载配置文件...")
                if not os.path.exists(cls._config_file):
                    raise FileNotFoundError(f"{cls._config_file} not found")

                try:
                    with open(cls._config_file, 'r',encoding="utf-8") as f:
                        cls._config = yaml.safe_load(f) or {}
                except yaml.YAMLError as e:
                    raise ValueError(f"YAML 解析错误: {e}")

    @classmethod
    def get(cls, path, default=None):
        if cls._config is None:
            cls._load_config()  # 确保配置文件已加载
        keys = path.split('.')
        value = cls._config
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key, default)
            else:
                return default
        return value

    @classmethod
    def reload(cls):
        with cls._lock:
            cls._config = None
            cls._load_config()

    @classmethod
    def set_config_file_path(cls, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"配置文件路径 {path} 不存在")
        cls._config_file = path