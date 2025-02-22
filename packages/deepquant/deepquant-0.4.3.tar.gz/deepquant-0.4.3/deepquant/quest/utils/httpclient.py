import re
import aiohttp
import asyncio
import logging
import requests

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        """发送 GET 请求"""
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, params=params)
            return response
        except Exception as e:
            logging.getLogger("httpclient").info(e)
            return None

    def post(self, endpoint, data=None, json=None, need_convert=False):
        """发送 POST 请求"""
        try:
            url = f"{self.base_url}/{endpoint}"
            print(json)
            if json and need_convert:
                # 转换请求数据的字段名(Java服务api接口字段是驼峰命名，需要转化)
                json = self.convert_dict_keys(json, self.snake_to_camel)
            response = requests.post(url, data=data, json=json)
            print(response)
            return response
        except Exception as e:
            print(e)
            logging.getLogger("httpclient").info(e)
            return None

    async def async_post(self, endpoint, data=None, json=None, need_convert=False):
        """异步发送 POST 请求"""
        try:
            url = f"{self.base_url}/{endpoint}"
            if json and need_convert:
                # 转换请求数据的字段名（Java服务API接口字段是驼峰命名，需要转化）
                json = self.convert_dict_keys(json, self.snake_to_camel)
            async with aiohttp.ClientSession() as session:
                async with session.post(url, data=data, json=json) as response:
                    return await response.json()
        except Exception as e:
            logging.getLogger("httpclient").info(e)
            return None


    @staticmethod
    def convert_dict_keys(data, conversion_func):
        """
        递归转换字典的键
        :param data: 原始字典
        :param conversion_func: 转换函数，例如 snake_to_camel 或 camel_to_snake
        :return: 转换后的字典
        """
        if isinstance(data, dict):
            return {conversion_func(k): HttpClient.convert_dict_keys(v, conversion_func) for k, v in data.items()}
        elif isinstance(data, list):
            return [HttpClient.convert_dict_keys(item, conversion_func) for item in data]
        else:
            return data

    @staticmethod
    def camel_to_snake(name):
        """
        驼峰命名转蛇形命名
        """
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

    @staticmethod
    def snake_to_camel(name):
        """
        蛇形命名转驼峰命名
        """
        components = name.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])