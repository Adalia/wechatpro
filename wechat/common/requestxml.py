# coding:utf-8
from wechat.common.tool import getXmlElement
import xml.etree.ElementTree as ET
class Requestxml(object):
    def __init__(self,xmldata):
        self.fromuser = getXmlElement(xmldata,"FromUserName")
        self.touser = getXmlElement(xmldata,"ToUserName")
        self.msg_type = getXmlElement(xmldata,"MsgType")
        self.createtime = getXmlElement(xmldata,"CreateTime")

class Textxml(Requestxml):
    def __init__(self,xmldata):
        Requestxml.__init__(self,xmldata)
        self.content = getXmlElement(xmldata,"Content")
        self.msgid = getXmlElement(xmldata,"MsgId")


class MenuEventxml(Requestxml):
    def __init__(self,xmldata):
        Requestxml.__init__(self,xmldata)
        self.event = getXmlElement(xmldata,"Event")
        self.eventkey = getXmlElement(xmldata,"EventKey")




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