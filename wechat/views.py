from django.shortcuts import render

# Create your views here.
import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import xml.etree.ElementTree as ET

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
        xmlData = ET.fromstring(webData)

        msg_type = xmlData.find('MsgType').text
        print("1")
        ToUserName = xmlData.find('ToUserName').text
        print("2")
        FromUserName = xmlData.find('FromUserName').text
        print("3")
        CreateTime = xmlData.find('CreateTime').text
        print("4")
        MsgType = xmlData.find('MsgType').text
        print("5")

        Event = xmlData.find('Event').text
        print("7")
        EventKey = xmlData.find('EventKey').text
        print("8")

        toUser = FromUserName
        fromUser = ToUserName
        requestDic = {'MsgType':msg_type,'ToUserName':ToUserName, 'FromUserName':FromUserName, 'CreateTime':CreateTime,'MsgType':MsgType,'Event':Event,'EventKey':EventKey  }
        print(requestDic)
        if msg_type == 'text':
            print(toUser)
            content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
            replyMsg = TextMsg(toUser, fromUser, content)
            print("成功了!!!!!!!!!!!!!!!!!!!")
            print
            replyMsg
            return replyMsg.send()

        elif msg_type == 'image':
            content = "图片已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()

        elif msg_type == 'voice':
            content = "语音已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)

            return replyMsg.send()
        elif msg_type == 'video':
            content = "视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()

        elif msg_type == 'shortvideo':
            content = "小视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()

        elif msg_type == 'location':
            content = "位置已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()

        elif msg_type == 'link':
            content = "链接已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()

        elif msg_type == 'event':
            print("******接收到event事件*************")
            return doEventReply(requestDic)

    except Exception as Argment:
        return Argment

def doEventReply(requestDic):
    print(requestDic.get("Event"))
    if requestDic.get("Event")=='CLICK':
        if requestDic.get("EventKey")=='V1001_test_perfomance':
            content = "性能测试页面正在维护中，真的非常抱歉！"
            replyMsg = TextMsg(requestDic.get('FromUserName'), requestDic.get('ToUserName'), content)
            return replyMsg.send()
			
def getXmlElement(request,elementname):
	try:
        webData = request.body
        print("=============================================")
        print(webData)
        print("=============================================")
        xmlData = ET.fromstring(webData)
		element = xmlData.find(elementname)
		if element is not NULL :
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
    pass



'''
=============================================
<xml><ToUserName><![CDATA[gh_92df4b2446a2]]></ToUserName>
<FromUserName><![CDATA[ok_Qa0xAEqcgJvymDdkB5D7mrdrE]]></FromUserName>
<CreateTime>1522314098</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[CLICK]]></Event>
<EventKey><![CDATA[V1001_test_perfomance]]></EventKey>
</xml>
=============================================
'''
