import requests

def post_wx():
    data="<xml><ToUserName><![CDATA[gh_92df4b2446a2]]></ToUserName>\
<FromUserName><![CDATA[ok_Qa0xAEqcgJvymDdkB5D7mrdrE]]></FromUserName>\
<CreateTime>1522314098</CreateTime>\
<MsgType><![CDATA[event]]></MsgType>\
<Event><![CDATA[CLICK]]></Event>\
<EventKey><![CDATA[V1001_test_perfomance]]></EventKey>\
</xml>"
    headers = {'content-type': 'charset=utf-8'}
    res=requests.post("http://127.0.0.1:8000/wx",data=data,headers=headers)
    print(res.text)

if __name__ =="__main__":
    post_wx()
#2:8_Gy-OSqDSoUxjdVF1yEuYnAUFFfzGlk8rfFWV2iMSMDoFwKlKTi6gI4tsY1W84e6hXa9VP5heJuI_f2bsoM3fktJmH-yhMnYqAO9roruMKZF0hjf6mADaFmQBagDewo6elsIuiOqEAAwBQQS8LYEiAGAGTZ