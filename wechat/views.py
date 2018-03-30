from django.shortcuts import render

# Create your views here.
import hashlib, json
import requests, _thread
import xml.etree.ElementTree as ET
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from wechat.common.tool import getXmlElement, get_token
from wechat.common import msg,customerservice

# django默认开启csrf防护，这里使用@csrf_exempt去掉防护

@csrf_exempt
def weixin_main(request):
    print("已经进入访问")
    if request.method == "GET":
        # 接收微信服务器get请求发过来的参数
        signature = str(request.GET.get('signature', None))
        timestamp = str(request.GET.get('timestamp', None))
        nonce = str(request.GET.get('nonce', None))
        echostr = str(request.GET.get('echostr', None))
        print("echostr: "+echostr)
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
        webdata = request.body
        xmldata = ET.fromstring(webdata)
        msg_type = xmldata.find('MsgType').text
        ToUserName = xmldata.find('ToUserName').text
        FromUserName = xmldata.find('FromUserName').text
        toUser = FromUserName
        fromUser = ToUserName
        if msg_type == 'text':
            try:
                _thread.start_new_thread(customerservice.customerService(xmldata),("replay"+toUser, ))   #异步回复消息
            except Exception as e:
                print(e)
            return ""

        elif msg_type == 'text':
            print(toUser)
            content = "您好!"
            replyMsg = msg.TextMsg(toUser, fromUser, content)
            return replyMsg.send()

        elif msg_type == 'event':
            print("******接收到event事件*************")
            #return doEventReply(requestDic)
            return ""

    except Exception as Argment:
        return Argment

def doEventReply(requestDic):
    print(requestDic.get("Event"))
    if requestDic.get("Event")=='CLICK':
        if requestDic.get("EventKey")=='V1001_test_perfomance':
            content = "性能测试页面正在维护中，真的非常抱歉！"
            replyMsg = msg.TextMsg(requestDic.get('FromUserName'), requestDic.get('ToUserName'), content)
            return replyMsg.send()


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
    customerservice.customerService(xmldata)
    print(getXmlElement(xmldata, "Mspe"))




