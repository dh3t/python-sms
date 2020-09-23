#python3封装短信云json数据包
短信下发

    访问地址：http://www.dh3t.com/json/sms/Submit

提交方式：

支持https
只支持POST
功能:

发送一条或者多条内容相同的短信
请求参数:

参数值说明：以下json内容为提交请求数据格式

{
    "account":"dh****",
    "password":"e717ebfd5271ea4a98bd38653c01113d",
    "msgid":"2c92825934837c4d0134837dcba00150",
    "phones":"1571166****,1571165****",
    "content":"您好，您的手机验证码为：430237。",
    "sign":"【****】",
    "subcode":"",
    "sendtime":"201405051230"
}

参数名 	说明
account 	用户账号
password 	密码，需采用MD5加密(32位小写) ，如调用大汉三通提供jar包的话使用明文
msgid 	该批短信编号(32位UUID)，需保证唯一，选填，不填的话响应里会给一个系统生成的
phones 	接收手机号码，多个手机号码用英文逗号分隔，最多1000个，必填，国际号码格式为+国别号手机号，示例：+85255441234（国际手机号前如果带0会去0后下发）
content 	短信内容，最多1000个汉字，必填,内容中不要出现【】[]这两种方括号，该字符为签名专用
sign 	短信签名，该签名需要提前报备，生效后方可使用，不可修改，必填，示例如：【大汉三通】
subcode 	短信签名对应子码(大汉三通提供)+自定义扩展子码(选填)，必须是数字，选填，未填使用签名对应子码，无法前匹配签名对应子码则使用签名对应子码+所填子码，通常建议不填
sendtime 	定时发送时间，格式yyyyMMddHHmm，为空或早于当前时间则立即发送

该响应为提交响应，发送到手机是否成功请获取状态报告确认该响应为提交响应，发送到手机是否成功请获取状态报告确认
返回示例:

{
    "msgid":"f02adaaa99c54ea58d626aac2f4ddfa8",
    "result":"0",
    "desc":"提交成功",
    "failPhones":"12935353535,110,130123123"
}

返回参数说明:
参数名 	说明
desc 	状态描述
msgid 	该批短信编号
result 	该批短信提交结果；说明请参照：提交响应错误码
failPhones 	如果提交的号码中含有错误（格式）号码将在此显示
Postman 请求示例截图

文档更新时间: 2020-07-09 16:50   作者：夏亮

