import requests

def post_wx():
    data = "<xml><ToUserName><![CDATA[gh_92df4b2446a2]]></ToUserName>\
       <FromUserName><![CDATA[ok_Qa0xAEqcgJvymDdkB5D7mrdrE]]></FromUserName>\
       <CreateTime>1522314098</CreateTime>\
       <MsgType><![CDATA[event]]></MsgType>\
       <Content><![CDATA[你好]]></Content>\
       <Event><![CDATA[CLICK]]></Event>\
       <EventKey><![CDATA[V1001_test]]></EventKey>\
       </xml>"
    headers = {'content-type': 'text/xml'}
    res=requests.post("http://127.0.0.1:8000/wx/",data=data.encode('utf-8'),headers=headers)
    print(res.text)

if __name__ =="__main__":
    post_wx()
