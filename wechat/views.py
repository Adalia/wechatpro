from django.shortcuts import render

# Create your views here.
import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import xml.etree.ElementTree as ET
from wechat.common import get_token
import requests
import _thread

#django默认开启csrf防护，这里使用@csrf_exempt去掉防护
@csrf_exempt
def weixin_main(request):
    print("已经进入访问")
    if request.method == "GET":
        # 接收微信服务器get请求发过来的参数
        signature = str(request.GET.get('signature', None))
        timestamp = str(request.GET.get('timestamp', None))
        nonce = str(request.GET.get('nonce', None))
        echostr = str(request.GET.get('echostr', None))
        # 服务器配置中的token
        token = 'haihui1215'
        # 把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        print(hashlist)
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        # 通过python标准库中的sha1加密算法，处理上面的字符串，形成新的字符串。
        hashstr = hashlib.sha1(hashstr.encode(encoding='utf-8')).hexdigest()
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("field")
    else:
        othercontent = autoreply(request)
        return HttpResponse(othercontent)

# 微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法

def autoreply(request):
    try:
        webData = request.body
        print("=============================================")
        print(webData)
        print("=============================================")
        print("1------------------------------------")
        xmlData = ET.fromstring(webData)
        print("2------------------------------------")
        msg_type = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text

        print("3---------"+msg_type)
        toUser = FromUserName
        fromUser = ToUserName
        print("4---------" + msg_type)
        if msg_type == 'text':

            '''
            print(toUser)
            content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
            replyMsg = TextMsg(toUser, fromUser, content)
            print("成功了!!!!!!!!!!!!!!!!!!!")
            print
            replyMsg
            return replyMsg.send()
            '''
            print("5---------" + msg_type)

            _thread.start_new_thread(customerService(xmlData))
            return "success"


        elif msg_type == 'event':
            print("******接收到event事件*************")
           # return doEventReply(requestDic)
            return ""

    except Exception as Argment:
        return Argment

def doEventReply(requestDic):
    print(requestDic.get("Event"))
    if requestDic.get("Event")=='CLICK':
        if requestDic.get("EventKey")=='V1001_test_perfomance':
            content = "性能测试页面正在维护中，真的非常抱歉！"
            replyMsg = TextMsg(requestDic.get('FromUserName'), requestDic.get('ToUserName'), content)
            return replyMsg.send()

def customerService(xmlData):

    print("************异步回复客户请求********************")
    replyContent = ""
    if xmlData.find('Content').text =="hello" or xmlData.find('Content').text =="你好":
        replyContent = "你好，请问有什么可以帮您？"
    else:
        replyContent = "请输入:你好！"

    data = {"touser":xmlData.find('FromUserName').text,
            "msgtype":"text",
            "text":{
                "content":replyContent
            }
            }
    jsondata=json.dumps(data,ensure_ascii=False).encode('utf-8')
    print(replyContent)

    ACCESS_TOKEN = get_token.get_token()
    print("get_token+++++++++++++++++++++++")
    url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=" + ACCESS_TOKEN
    print(url)
    requests.post(url,data=jsondata)

def getXmlElement(xmldata,elementname):
    print("*****request body:"+xmldata)
    try:
        element = xmldata.find(elementname)
        if element is not None :
            return element.text
        else:
            return element

    except Exception as Argment:
        return Argment

class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text


import time

import re
class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
            <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{Content}]]></Content>
            </xml>
            """
        return XmlForm.format(**self.__dict)

if __name__=="__main__":
    data = "<xml><ToUserName><![CDATA[gh_92df4b2446a2]]></ToUserName>\
    <FromUserName><![CDATA[ok_Qa0xAEqcgJvymDdkB5D7mrdrE]]></FromUserName>\
    <CreateTime>1522314098</CreateTime>\
    <MsgType><![CDATA[event]]></MsgType>\
    <Content><![CDATA[hello]]></Content>\
    <Event><![CDATA[CLICK]]></Event>\
    <EventKey><![CDATA[V1001_test_perfomance]]></EventKey>\
    </xml>"
    xmldata = ET.fromstring(data)
    customerService(xmldata)




