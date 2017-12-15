# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail():
    host_dir='smtp.exmail.qq.com'
    username='xuman@weitaikeji.com'
    password='Min%@)0214'
    from_mail = 'xuman@weitaikeji.com'
    to_list = ['13207140256@163.com', 'calvin1102@aliyun.com','847527255@qq.com']

    subject = 'Python SMTP 邮件测试'
    message = MIMEText(u'Python 自动化接口测试已完成。详细测试报告请点击：http://www.cx9z.com/', 'plain', 'utf-8')
    message['from']=Header('发件人','utf-8')
    message['to']=Header('收件人','utf-8')
    message['subject']=Header(subject,'utf-8')


    e = smtplib.SMTP()
    e.connect(host_dir, port=25)
    e.login(username, password)
    e.sendmail(from_mail, to_list, message.as_string())
    e.quit()

    print('邮件发送成功')


if __name__=='__main__':
    send_mail()
