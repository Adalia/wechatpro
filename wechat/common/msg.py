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

    def send(self):
        print("send")
        Content = "你好，欢迎使用我的公众号！请回复'历史消息'或者'h'查看近期消息!"
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

