import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


my_sender = 'huyingjie86@163.com'
my_user = '510814247@qq.com'


def mail():
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["发件人邮箱昵称", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["收件人邮箱昵称", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "主题"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, "EKDSUVPSGFYHQGDU")  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, my_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()
    except Exception:
        ret = False
    return ret
