"""
create by  gaowenfeng on  2018/6/1
"""
import requests
__author__ = "gaowenfeng"


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        """
        发送get请求
        :param url: 请求路径
        :param return_json: 是否返回json格式的结果
        :return:
        """
        # r 是对这次HTTP请求调用结果的一个封装，并不是我们直接想要的结果，而是想要返回的内容
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
