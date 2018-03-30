import time
from wechat.common.tool import getxmlElement
class Msg(object):
    def __init__(self, xmldata):
        self.ToUserName = getxmlElement(xmldata,'ToUserName')
        self.FromUserName = getxmlElement(xmldata,'FromUserName')
        self.CreateTime = getxmlElement(xmldata,'CreateTime')
        self.MsgType = getxmlElement(xmldata,'MsgType')
        self.MsgId = getxmlElement(xmldata,'MsgId')
        self.content = getxmlElement(xmldata,'Content')

class TextMsg(Msg):
    def __init__(self, xmldata):
        Msg.__init__(self, xmldata)
        self.__dict = dict()
        self.__dict['ToUserName'] = self.FromUserName
        self.__dict['FromUserName'] = self.ToUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = ""

    def set_content(self):
        if self.content in msgMap.keys():
            self.__dict['Content'] = msgMap.get(self.content)
        else:
            self.__dict['Content'] = "Sorry,i cannot understand!"

    def send(self):
        self.set_content()
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

msgMap={
        "hello":"hello",
        "你好":"你好",
    }