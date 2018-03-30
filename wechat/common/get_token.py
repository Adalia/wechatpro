import requests
import time,datetime
from wechat.common import getConfig
import json

conf = getConfig.getConfig()


def get_token():
    appID = conf.getConfig("wx", "appID")
    appsecret = conf.getConfig("wx", "appsecret")
    token = conf.getConfig("wx", "access_token")

    timestamp = int(time.time())
    print("当前时间："+str(timestamp))
    expire_time = int(conf.getConfig("wx", "expires_time"))  # 配置文件中记录的过期时间
    print("过期时间："+ str(expire_time) )

    if expire_time <= timestamp:  # 如果token过期修改配置文件中过期时间，token等值
        print("token过期")
        res = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appID + "&secret=" + appsecret)
        response = json.loads(res.text)
        print(type(response))
        token = response.get("access_token")
        expire_in = response.get("expires_in")
        expire_time = expire_in + timestamp
        print("下次过期时间："+ str(expire_time))
        conf.setConfig("wx", "expire_time", str(expire_time))
        conf.setConfig("wx", "access_token", token)
        conf.setConfig("wx", "expires_in", str(expire_in))
    print(token)
    return token


if __name__ == "__main__":
    print(get_token())