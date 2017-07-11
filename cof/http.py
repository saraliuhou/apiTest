import requests
import json


class Http():
    """
    对http的常用请求方法进行封装
    """
    def __init__(self):
        self.host = ""
        self.port = ""
        # 默认的header，内容遵循restful接口规范要求
        self.header = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def get(self, url, dictData):
        response = requests.get(self.host+url, params=dictData)
        res = dict()
        res["request"] = "methon=get" + "  " + self.host + ":" + self.port + url + "  " + "body = " + json.dumps(dictData)
        res["code"] = response.status_code
        res["data"] = response.text
        return res

    def getById(self, url):
        response = requests.get(self.host+url)
        res = dict()
        res["request"] = "methon=get" + "  " + self.host + ":" + self.port + url + "  "
        res["code"] = response.status_code
        res["data"] = response.text
        return res

    def post(self, url, dictData):
        response = requests.post(self.host+url, data=json.dumps(dictData), headers=self.header)
        res = dict()
        res["request"] = "methon=post" + "  " + self.host + ":" + self.port + url + "  " + "body = " + json.dumps(dictData)
        res["code"] = response.status_code
        res["data"] = response.text
        return res

    def put(self, url, dictData):
        response = requests.put(self.host+url, data=dictData)
        res = dict()
        res["request"] = "methon=put" + "  " + self.host + ":" + self.port + url + "  " + "body = "
        res["code"] = response.status_code
        res["data"] = response.text
        return res

    def patch(self, url, dictData):
        response = requests.patch(self.host+url, data=json.dumps(dictData), headers=self.header)
        res = dict()
        res["request"] = "methon=patch" + "  " + self.host + ":" + self.port + url + "  " + "body = "
        res["code"] = response.status_code
        res["data"] = response.text
        return res

    def delete(self, url, dictData):
        response = requests.delete(self.host+url, params=dictData)
        res = dict()
        res["request"] = "methon=delete" + "  " + self.host + ":" + self.port + url
        res["code"] = response.status_code
        res["data"] = response.text
        return res

