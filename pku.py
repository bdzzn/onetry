import requests
from http import cookiejar
import sys
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#访问不到时使用IP访问
headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",\
	"Host":"iaaa.pku.edu.cn",\
	#"Host":"162.105.67.57",
	"Referer":"https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=portal&appName=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97%A8%E6%88%B7&redirectUrl=http://portal.pku.edu.cn/portal2013/login.jsp/../ssoLogin.do"
}
global response
global name
name=""
session=requests.session()

def login(username,password):
	global response
	data={
		"appid":"portal",
		"userName":username,
		"password":password,
		"randCode":"验证码",
		"smsCode":"短信验证码",
		"otpCode":"动态口令",
		"redirUrl":"http://portal.pku.edu.cn/portal2013/login.jsp/../ssoLogin.do"
	}
	#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	response=session.post("https://iaaa.pku.edu.cn/iaaa/oauthlogin.do",data=data,headers=headers)
	#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#	print(response.json())

def catch(token):
	url="http://portal.pku.edu.cn/portal2013/ssoLogin.do?"+"token="+token
#	print(url)
	headers={
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",\
	"Accept-Encoding":"gzip, deflate",\
	"Accept-Language":"zh-CN,zh;q=0.8",\
	"Connection":"keep-alive",\
#	"Cookie":"JSESSIONID=415967E76A2B0E4DDAE95A9BBAEE27E4; PKU_HPC_NAMING_STOP=true; portalBannerHeight=92; UM_distinctid=15e7647f33054f-0190110a18f452-e313761-e1000-15e7647f334ce6",\
	"Host":"portal.pku.edu.cn",\
	"Upgrade-Insecure-Requests":"1",\
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",\
#	"Cookie":"JSESSIONID=044A13725DF19F014D3D8EF170B59078; PKU_HPC_NAMING_STOP=true; portalBannerHeight=92; UM_distinctid=15e7647f33054f-0190110a18f452-e313761-e1000-15e7647f334ce6"
	}

	hhh=session.post(url,headers=headers,verify=False)
#	print(hhh.headers)
#	print(hhh.text)
	url="https://portal.pku.edu.cn/portal2013/ssoLogin.do?"+"token="+token
	hhh=session.post(url,headers=headers)
	#print(hhh.text)
#	print(hhh.headers)
	#print(hhh.text)
	#hhh=session.post("https://portal.pku.edu.cn/portal2013/ssoLogin.do?",headers=headers)
	url="https://portal.pku.edu.cn/portal2013/account/getUserMenus.do?_dc=1507989202805"
	hhh=session.post(url,headers=headers)
#	print(dir(hhh.text))
#	print(hhh.text)
	flag=0
	name=""
	for i in hhh.text[0:50]:
		if(flag==1 and i!="\""):
			name+=i
		if(i=="\""):
			if(flag==0):
				flag=1
				continue
			if(flag==1):
				flag=0
	print(name)
#	for i in hhh.text.split:
#		print(i)

	#	hhh=session.post("https://portal.pku.edu.cn/portal2013/portal.jsp",headers=headers)
	#print(hhh.text)


if __name__=='__main__':
	#username="sxkxxy"
	#password="sxkxxy@2020"
	username="xlyrzkxxy"
	password="xlyrzkxxy@890"
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	login(username,password)
	#print(response.json())
	if(response.json()['success']):
		token=response.json()['token']
	#print(token)
	#print(token)
		catch(token)
	else:
		print("你上的怕不是假北大.....")
	#a=eval(response.text)
	#print(type(a))
#	url="https://portal.pku.edu.cn/portal2013/index.jsp"

#	headers={
#	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",\
#	"Accept-Encoding":"gzip, deflate",\
#	"Host":"portal.pku.edu.cn",\
#	"Origin":"https://iaaa.pku.edu.cn",\
#	"Referer":"https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=portal&appName=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97%A8%E6%88%B7&redirectUrl=http://portal.pku.edu.cn/portal2013/login.jsp/../ssoLogin.do",\
#	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",\
#	"Cookie":"JSESSIONID=044A13725DF19F014D3D8EF170B59078; PKU_HPC_NAMING_STOP=true; portalBannerHeight=92; UM_distinctid=15e7647f33054f-0190110a18f452-e313761-e1000-15e7647f334ce6"
#	"X-Requested-With":"XMLHttpRequest"
#	}

#	tempcookie=response.cookies
	#print(tempcookie)
	#print(session.cookies)
	#html=session.post("https://portal.pku.edu.cn/portal2013/index.jsp",verify=False,headers=headers)
	#print(html.url)
	#print(html.text)

#	a={"2":"hjk","3":"hhh"}
#	print(a['2'])