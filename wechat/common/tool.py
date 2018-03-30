import requests
import time,datetime
from wechat.common import dealConfig
import json

conf = dealConfig.getConfig()


def get_token():
    appID = conf.getConfig("wx", "appID")
    appsecret = conf.getConfig("wx", "appsecret")
    token = conf.getConfig("wx", "access_token")
    timestamp = int(time.time())
    expire_time = int(conf.getConfig("wx", "expires_time"))  # 配置文件中记录的过期时间

    if expire_time <= timestamp:  # 如果token过期修改配置文件中过期时间，token等值
        res = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appID + "&secret=" + appsecret)
        response = json.loads(res.text)
        token = response.get("access_token")
        expire_in = response.get("expires_in")
        expire_time = expire_in + timestamp
        print("下次过期时间："+ str(expire_time))
        conf.setConfig("wx", "expire_time", str(expire_time))
        conf.setConfig("wx", "access_token", token)
        conf.setConfig("wx", "expires_in", str(expire_in))
    return token


def getXmlElement(xmldata,elementname):
    try:
        element = xmldata.find(elementname)
        if element is not None :
            return element.text
        else:
            return element
    except Exception as Argment:
        return Argment

if __name__ == "__main__":
    print(get_token())