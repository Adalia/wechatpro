# coding:utf-8
from wechat.common.tool import getxmlElement
import xml.etree.ElementTree as ET
class Requestxml(object):
    def __init__(self,xmldata):
        self.fromuser =getxmlElement(xmldata,"FromUserName")
        self.touser = getxmlElement(xmldata,"ToUserName")
        self.msg_type = getxmlElement(xmldata,"MsgType")
        self.createtime = getxmlElement(xmldata,"CreateTime")

class Textxml(Requestxml):
    def __init__(self,xmldata):
        Requestxml.__init__(self,xmldata)
        self.content = getxmlElement(xmldata,"Content")
        self.msgid = getxmlElement(xmldata,"MsgId")


class MenuEventxml(Requestxml):
    def __init__(self,xmldata):
        Requestxml.__init__(self,xmldata)
        self.event = getxmlElement(xmldata,"Event")
        self.eventkey = getxmlElement(xmldata,"EventKey")

if __name__=="__main__":
    data = "<xml><ToUserName><![CDATA[gh_92df4b2446a2]]></ToUserName>\
           <FromUserName><![CDATA[ok_Qa0xAEqcgJvymDdkB5D7mrdrE]]></FromUserName>\
           <CreateTime>1522314098</CreateTime>\
           <MsgType><![CDATA[text]]></MsgType>\
           <Content><![CDATA[你好]]></Content>\
           <Event><![CDATA[CLICK]]></Event>\
           <EventKey><![CDATA[V1001_test_perfomance]]></EventKey>\
           </xml>"
    xmldata = xmldata = ET.fromstring(data)
    textxml = Textxml(xmldata)