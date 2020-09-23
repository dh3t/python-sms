#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Administrator'

import requests
import json
import hashlib
"""
python3封装json数据包
"""

class smsClient(object):
    def __init__(self):
        """
        实例化请求实体
        :param headers: 请求头字典形式
        """
        self.headers={'Content-Type':'application/json'}
       
    def dopost(self,url,data):
        res=requests.post(url,json.dumps(data),headers=self.headers,timeout=5)
        return res.status_code,res.text

    def md5(self,pwd):
        m=hashlib.md5()
        m.update(bytes(pwd,encoding='utf-8'))
        return m.hexdigest()


if  __name__ == "__main__":
    smsClient=smsClient()
    #短信下发接口
    url1="http://www.dh3t.com/json/sms/Submit"
    data1={
    "account":"dhlftest",                           #账号，需要在大汉运营平台开通
    "password":smsClient.md5("123.com"),            #密码，需采用MD5加密(32位小写)
    "msgid":"2c92825934837c4d0134837dcba00150",     #该批短信编号(32位UUID)，需保证唯一，选填，不填的话响应里会给一个系统生成的
    "phones":"18621803633",                         #接收手机号码，多个手机号码用英文逗号分隔，最多1000个，必填，国际号码格式为+国别号手机号，如：+85255441234（国际手机号前如果带0会去0后下发）
    "content":"您好，您的手机验证码为：430237。",      #短信内容，最多1000个汉字
    "sign":"【大汉三通】",                           #短信签名，该签名需要提前报备，生效后方可使用，不可修改，必填，示例如：【大汉三通】
    "subcode":"",                                   #扩展子码
    "sendtime":""                                   #定时发送时间，格式yyyyMMddHHmm，为空或小于当前时间则立即发送
    }
    code,text=smsClient.dopost(url1,data1)
    print("http_code：%s,response:%s"%(code,text))

    #Report 主动获取状态报告,data只需要传账号和密码
    url2="http://www.dh3t.com/json/sms/Report"
    data2={
        "account":"dhlftest",
        "password":smsClient.md5("123.com") 
    }
    code,text=smsClient.dopost(url2,data2)
    print("http_code：%s,response:%s"%(code,text))

    #Deliver 主动获取上行，data只需要传账号和密码 ，这里使用data2
    url3="http://www.dh3t.com/json/sms/Deliver"
    code,text=smsClient.dopost(url3,data2)
    print("http_code：%s,response:%s"%(code,text))

    #Balance 查询余额，data只需要传账号和密码 ，这里使用data2
    url4="http://www.dh3t.com/json/sms/Balance"
    code,text=smsClient.dopost(url4,data2)
    print("http_code：%s,response:%s"%(code,text))

    ####签名在内容里接口,注意data1和data5数据区别，签名在内容里，没有单独的签名字段
    ####注意：使用这个接口，如果data里有sign字段且值不为空，则会出现双签名#####
    url5="http://www.dh3t.com/json/sms/SubmitWithSign"
    data5={      
    "account":"dh****",
    "password":"e717ebfd5271ea4a98bd38653c01113d",
    "msgid":"2c92825934837c4d0134837dcba00150",
    "phones":"1571166****,1571165****",
    "content":"【大汉三通】您好，您的手机验证码为：430237。",
    "subcode":"",
    "sendtime":""
    }
    code,text=smsClient.dopost(url5,data5)
    print("http_code：%s,response:%s"%(code,text))

    ####模板下发接口##########
    url6="http://www.dh3t.com/json/sms/Submit"
    data6={
    "account":"dh****",                             #账号，需要在大汉运营平台开通
    "password":"e717ebfd5271ea4a98bd38653c01113d",  #密码，需采用MD5加密(32位小写)
    "msgid":"2c92825934837c4d0134837dcba00150",     #该批短信编号(32位UUID)，需保证唯一，选填，不填的话响应里会给一个系统生成的
    "phones":"1571166****",                         #接收手机号码，多个手机号码用英文逗号分隔，最多1000个，必填，国际号码格式为+国别号手机号，如：+85255441234（国际手机号前如果带0会去0后下发）
    "template":{"id":"d65b268cba2243d8a4b15f22f9e847d8","variables":[{"name":"1","value":"内容1"},{"name":"2","value":"内容2"}]},#短信模板格式，id对应模板id，variables对应模板内容的键值对集合，name对应变量内容序号（序号从1开始，必填），value对应具体内容；
    "subcode":"",                                   #该批次扩展子码
    "sendtime":""                                   #定时发送时间，格式yyyyMMddHHmm，为空或小于当前时间则立即发送
    }
    code,text=smsClient.dopost(url6,data6)
    print("http_code：%s,response:%s"%(code,text))

    ###模板上传接口########
    url7="http://www.dh3t.com/json/sms/upload/template"
    data7={
    "account":"dh****",                             #账号，需要在大汉运营平台开通
    "password":"e717ebfd5271ea4a98bd38653c01113d",  #密码，需采用MD5加密(32位小写)
    "content":"你好，这是白模板${1,10}示例",          #变量采用：${n,m}的格式，匹配n到m个文字，n<m，必填
    "sign":"【大汉三通】",                           #签名（必填），该签名需要提前报备，生效后方可使用，不可修改，必填，示例如：【大汉三通】
    "remark":""                                     #备注。可不填
    }
    code,text=smsClient.dopost(url7,data7)
    print("http_code：%s,response:%s"%(code,text))

    ##模板查询
    url8="http://www.dh3t.com/json/sms/show/template"
    data8={
    "account":"dh****",
    "password":"bb43a2c4081bec02fca7b72f38e63021",
    "templateIds":"2c9282395f23f49f015f23fc04180000,2c9282395f23c9aa015f23cb88af0002"#上传模板时响应包中的templateId值,多个用英文逗号做分隔
    }
    code,text=smsClient.dopost(url8,data8)
    print("http_code：%s,response:%s"%(code,text))

    ##模板删除
    url9="http://www.dh3t.com/json/sms/delete/template"
    data9={
    "account":"dh****",
    "password":"e717ebfd5271ea4a98bd38653c01113d",
    "templateIds":"f02adaaa99c54ea58d626aac2f4ddfa8,z2sds3aa99c54ea58d626aaaj12de214" #本次删除的模板编号，可以多个，用逗号分隔，必填
    }
    code,text=smsClient.dopost(url8,data8)
    print("http_code：%s,response:%s"%(code,text))
