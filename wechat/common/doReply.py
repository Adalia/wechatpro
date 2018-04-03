import json
import requests
from wechat.common.tool import getxmlElement, get_token
from wechat.common.requestxml import *
import threading


import time
def doEventReply(xmldata):
    event = MenuEventxml(xmldata)
    eventreply = {
        "V1001_test":"性能测试页面正在维护中，真的非常抱歉！",
        "V1002_test":"自动化测试页面正在维护中，真的非常抱歉！",
        "V1003_test":"接口测试页面正在维护中，真的非常抱歉！",
        "others":"sorry！"
    }
    if event.event =='CLICK':
        print(event.eventkey)
        if event.eventkey == 'V1001_test':
            content = eventreply.get("V1001_test")
        elif event.eventkey == 'V1002_test':
            content = eventreply.get("V1002_test")
        elif event.eventkey == 'V1003_test':
            content = eventreply.get("V1003_test")
        else:
            content = eventreply.get("others")
    #print(content)
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


def doSubscribeReply(xmldata):
    pass

def doTextReply(xmldata):
    print("************客服消息********************")
    content = getxmlElement(xmldata, "Content")
    fromuser = getxmlElement(xmldata,"FromUserName")
    if content =="hello" or content =="你好":
        replycontent = "你好，请问有什么可以帮您？"
    else:
        replycontent = "请输入:你好！"
    data = {"touser":fromuser,
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


def doHistoryReply(xmldata):
    print("************历史消息********************")
    fromuser = getxmlElement(xmldata,"FromUserName")
    replycontent = "历史消息正在准备中"
    data={
        "touser": fromuser,
        "msgtype": "news",
        "news": {
            "articles": [
                {
                    "title": "Happy Day",
                    "description": "Is Really A Happy Day",
                    "url": "URL",
                    "picurl": "PIC_URL"
                },
                {
                    "title": "Happy Day",
                    "description": "Is Really A Happy Day",
                    "url": "http://192.144.138.251/wx/html",
                    "picurl": "PIC_URL"
                }
            ]
        }
    }
    jsondata = json.dumps(data,ensure_ascii=False).encode('utf-8')
    ACCESS_TOKEN = get_token()
    url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=" + ACCESS_TOKEN
    requests.post(url,data=jsondata)


if __name__ =="__main__":
    data = "<xml><ToUserName><![CDATA[gh_92df4b2446a2]]></ToUserName>\
        <FromUserName><![CDATA[ok_Qa0xAEqcgJvymDdkB5D7mrdrE]]></FromUserName>\
        <CreateTime>1522314098</CreateTime>\
        <MsgType><![CDATA[event]]></MsgType>\
        <Content><![CDATA[hello]]></Content>\
        <Event><![CDATA[CLICK]]></Event>\
        <EventKey><![CDATA[V1003_test]]></EventKey>\
        </xml>"
    xmldata = ET.fromstring(data)
    doEventReply(xmldata)