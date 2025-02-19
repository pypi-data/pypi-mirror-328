# coding=utf-8
import json
import os
import random
from typing import List, Dict, Optional


class Input:
    @staticmethod
    def get_request_list(name: str, default: Optional[List] = None) -> List:
        """
        获取环境变量并解析为列表
        :param name: 环境变量名称
        :param default: 默认值
        :return: 列表
        """
        value = os.getenv(name.upper())
        if value is None:
            return default if default is not None else []
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return default if default is not None else []

    @staticmethod
    def get_bool(name: str, default: bool = False) -> bool:
        """
        获取环境变量并解析为布尔值
        :param name: 环境变量名称
        :param default: 默认值
        :return: 布尔值
        """
        value = os.getenv(name.upper())
        if value is None:
            return default
        return value.lower() == 'true'

    @staticmethod
    def get_int(name: str, default: int = 0) -> int:
        """
        获取环境变量并解析为整数
        :param name: 环境变量名称
        :param default: 默认值
        :return: 整数
        """
        value = os.getenv(name.upper())
        if value is None:
            return default
        try:
            return int(value)
        except ValueError:
            return default

    @staticmethod
    def get_float(name: str, default: float = 0.0) -> float:
        """
        获取环境变量并解析为浮点数
        :param name: 环境变量名称
        :param default: 默认值
        :return: 浮点数
        """
        value = os.getenv(name.upper())
        if value is None:
            return default
        try:
            return float(value)
        except ValueError:
            return default

    @staticmethod
    def get_string(name: str, default: str = "") -> str:
        """
        获取环境变量并解析为字符串
        :param name: 环境变量名称
        :param default: 默认值
        :return: 字符串
        """
        value = os.getenv(name.upper())
        if value is None:
            return default
        return value

    @staticmethod
    def get_list(name: str, default: Optional[List] = None) -> List:
        """
        获取环境变量并解析为列表
        :param name: 环境变量名称
        :param default: 默认值
        :return: 列表
        """
        value = os.getenv(name.upper())
        if value is None:
            return default if default is not None else []
        try:
            return [i.get('url') for i in json.loads(value)]
        except (json.JSONDecodeError, AttributeError):
            return default if default is not None else []

    @staticmethod
    def get_dict(name: str, default: Optional[Dict] = None) -> Dict:
        """
        获取环境变量并解析为字典
        :param name: 环境变量名称
        :param default: 默认值
        :return: 字典
        """
        value = os.getenv(name.upper())
        if value is None:
            return default if default is not None else {}
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return default if default is not None else {}

    @staticmethod
    def get_proxies(default: Optional[List[str]] = None) -> List[str]:
        """
        获取代理列表
        :param default: 默认值
        :return: 代理列表
        """
        proxy_url = os.getenv('PROXY_URL')
        if proxy_url:
            return proxy_url.split(',')
        return default if default is not None else []

    @staticmethod
    def get_random_proxy(default: Optional[str] = None) -> Optional[str]:
        """
        随机获取一个代理
        :param default: 默认值
        :return: 随机代理
        """
        proxy_list = Input.get_proxies()
        if proxy_list:
            return random.choice(proxy_list)
        return default

    @staticmethod
    def is_free_user(default: bool = True) -> bool:
        """
        判断是否为免费用户
        :param default: 默认值
        :return: 是否为免费用户
        """
        user_plan = os.getenv('USER_PLAN')
        if user_plan == 'IS_OWNER':
            return False
        return user_plan == 'FREE' if user_plan else default