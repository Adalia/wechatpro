# coding:utf-8
import hashlib, json
import requests, _thread
import xml.etree.ElementTree as ET
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import threading

from wechat.common.tool import getxmlElement, get_token
from wechat.common import msg,doReply
from wechat.common import msg

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
        token = 'haihui1001'
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
import time
def autoreply(request):
    try:
        webdata = request.body
        xmldata = ET.fromstring(webdata)
        #webdata=request
        #xmldata = ET.fromstring(webdata)
        msg_type = getxmlElement(xmldata,'MsgType')
        content = getxmlElement(xmldata,'Content')
        toUser = getxmlElement(xmldata,'FromUserName')
        print(msg_type)
        if msg_type == 'text':
            if content=="历史消息" or  content=="h":
                print(content+"1111111111111111111111")
                try:
                    #_thread.start_new_thread(customerservice.doTextReply(xmldata),("replay"+toUser, ))   #异步回复消息
                    threading.Thread(target=doReply.doHistoryReply, args=(xmldata,), name="replay" + toUser).start()
                except Exception as e:
                    print(e)
                return ""

            else:
                print(content)
                return msg.TextMsg(xmldata).send()


        elif msg_type == 'event':
            print("******接收到event事件*************")
            event = getxmlElement(xmldata,"Event")
            toUser = getxmlElement(xmldata,"FromUserName")
            if event=="CLICK":
                #_thread.start_new_thread(customerservice.doEventReply(xmldata), ("replay" + toUser,))  #
                threading.Thread(target=doReply.doEventReply, args=(xmldata,), name="replay" + toUser).start()
            return ""

    except Exception as Argment:
        return Argment



if __name__=="__main__":
    data = "<xml><ToUserName><![CDATA[gh_92df4b2446a2]]></ToUserName>\
    <FromUserName><![CDATA[ok_Qa0xAEqcgJvymDdkB5D7mrdrE]]></FromUserName>\
    <CreateTime>1522314098</CreateTime>\
    <MsgType><![CDATA[text]]></MsgType>\
    <Content><![CDATA[hello]]></Content>\
    <Event><![CDATA[CLICK]]></Event>\
    <EventKey><![CDATA[V1002_test]]></EventKey>\
    </xml>"
    autoreply(data)
    #xmldata = ET.fromstring(data)
    #customerservice.customerService(xmldata)
   # print(getxmlElement(xmldata, "Mspe"))




