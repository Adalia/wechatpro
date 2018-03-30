import json
import requests
from wechat.common.tool import getXmlElement, get_token


def customerService(xmldata):

    print("************异步回复客户请求********************")
    content = getXmlElement(xmldata, "Content")
    if content =="hello" or content =="你好":
        replycontent = "你好，请问有什么可以帮您？"
    else:
        replycontent = "请输入:你好！"

    data = {"touser":xmldata.find('FromUserName').text,
            "msgtype":"text",
            "text":{
                "content":replycontent
            }
    }
    print(replycontent)
    jsondata = json.dumps(data,ensure_ascii=False).encode('utf-8')
    ACCESS_TOKEN = get_token()
    url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=" + ACCESS_TOKEN
    requests.post(url,data=jsondata)
