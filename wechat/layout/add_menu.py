# coding:utf-8
import requests
from wechat.common import tool
import json


def baseMenu():
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + tool.get_token()
    print(url)
    data = {
         "button":[
                {
                 "name":"测试笔记",
                 "sub_button":[
                     {
                         "type": "click",
                         "name": "性能测试",
                         "key": "V1001_test"
                     },
                     {
                         "type": "click",
                         "name": "自动化测试",
                         "key": "V1002_test"
                     },
                     {
                         "type": "click",
                         "name": "接口测试",
                         "key": "V1003_test"
                     }
                 ]
                },
                {
                   "name":"轻松一下",
                   "sub_button":[
                    {
                       "type":"view",
                       "name":"笑话",
                       "url":"http://www.soso.com/"
                    },
                    {
                         "type":"view",
                         "name":"歌曲",
                         "url":"http://mp.weixin.qq.com",
                    },
                    ]
               },
            {
                 "name": "others",
                 "sub_button": [
                     {
                         "type": "view",
                         "name": "1",
                         "url": "http://www.soso.com/"
                     },
                     {
                         "type": "view",
                         "name": "2",
                         "url": "http://mp.weixin.qq.com",
                     },
                 ]
             }
         ]
     }
    print(type(data))
    jsondata = json.dumps(data,ensure_ascii=False).encode("utf-8")
    print(jsondata)
    print(type(jsondata))
    request = requests
    headers = {'content-type': 'charset=utf-8'}
    res = requests.post(url, data=jsondata)
    return res

if __name__ == "__main__":
    print(baseMenu().text)