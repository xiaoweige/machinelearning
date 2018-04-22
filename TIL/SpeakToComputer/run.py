#coding=gb2312
import os
import webbrowser

import requests
from record_wav import record_wave

apiKey = "64T7K8nz5HNsWOAwFSMxWt2W"
secretKey = "4c562f3d67e33944ff526011c2823a03"
auth_url = "http://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey
api_url = "http://vop.baidu.com/server_api?lan=zh&cuid=abcdtest&token="

url_dict = {
    u'baidu': "https://www.baidu.com",
    u'百度': "http://www.baidu.com",
    u'谷歌': "http://www.google.com",
    u'牛': "https://www.nowcoder.com"
}
#录音并保存到文件
wavfile = record_wave()

#获取token
access_token = requests.post(auth_url).json()['access_token']
res = None
with open(wavfile,'rb') as f:
    r = requests.post(api_url+access_token, headers={'Content-Type': "audio/wav;rate=8000"}, data=f)
    
    res = r.json()
    if res['err_no'] != 0: #识别错误
        res = None

if not res:
    print ("识别错误")
    exit()
open_url = None
for k in url_dict:
    if k in res['result'][0]:
        open_url = url_dict[k]

print ("识别结果: ",res['result'][0])

if not open_url:
    print ("没有对应的命令.")
    exit()
#调用系统命令,打开浏览器

#webbrowser.open(open_url)
webbrowser.open_new(open_url)
