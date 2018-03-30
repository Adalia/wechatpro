import requests

def post_wx():
    data="<xml><ToUserName><![CDATA[gh_92df4b2446a2]]></ToUserName>\
<FromUserName><![CDATA[ok_Qa0xAEqcgJvymDdkB5D7mrdrE]]></FromUserName>\
<CreateTime>1522314098</CreateTime>\
<MsgType><![CDATA[event]]></MsgType>\
<Event><![CDATA[CLICK]]></Event>\
<EventKey><![CDATA[V1001_test_perfomance]]></EventKey>\
</xml>"
    datatext="<xml>  <ToUserName>< ![CDATA[gh_92df4b2446a2]] ]></ToUserName>  <FromUserName>< ![CDATA[ok_Qa0xAEqcgJvymDdkB5D7mrdrE]]></FromUserName> \
              <CreateTime>1348831860</CreateTime>  <MsgType>< ![CDATA[text] ]></MsgType>  <Content>< ![CDATA[hello] ]></Content>  <MsgId>1234567890123456</MsgId>  </xml>"
    headers = {'content-type': 'charset=utf-8'}
    datatext.encode('utf-8')
    res=requests.post("http://127.0.0.1:8000/wx/",data=datatext,headers=headers)
    print(res.text)

if __name__ =="__main__":
    post_wx()
