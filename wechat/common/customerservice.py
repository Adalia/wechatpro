import json
import requests
from wechat.common.tool import getXmlElement, get_token
from wechat.common.requestxml import *


def doTextReply(xmldata):

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

def doEventReply(xmldata):
    event = MenuEventxml(xmldata)
    print(event.event)
    print(event.eventkey)
    content = '1111111'
    if event.event =='CLICK':
        if event.eventkey == 'V1001_test':
            content = "性能测试页面正在维护中，真的非常抱歉！"

        elif event.eventkey == 'V1002_test':
            content = "自动化测试页面正在维护中，真的非常抱歉！"
        else:
            content = "接口测试页面正在维护中，真的非常抱歉！"

    print(content)
    data = {"touser": xmldata.find('FromUserName').text,
            "msgtype": "text",
            "text": {
                "content": content
            }
    }
    jsondata = json.dumps(data, ensure_ascii=False).encode('utf-8')
    ACCESS_TOKEN = get_token()
    url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=" + ACCESS_TOKEN
    requests.post(url, data=jsondata)


if __name__ =="__main__":
    data = "<xml><ToUserName><![CDATA[gh_92df4b2446a2]]></ToUserName>\
        <FromUserName><![CDATA[ok_Qa0xAEqcgJvymDdkB5D7mrdrE]]></FromUserName>\
        <CreateTime>1522314098</CreateTime>\
        <MsgType><![CDATA[event]]></MsgType>\
        <Content><![CDATA[hello]]></Content>\
        <Event><![CDATA[CLICK]]></Event>\
        <EventKey><![CDATA[V1001_test]]></EventKey>\
        </xml>"
    xmldata = ET.fromstring(data)
    doEventReply(xmldata)