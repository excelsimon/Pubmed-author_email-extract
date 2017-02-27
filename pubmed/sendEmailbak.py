# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication 
from email.MIMEBase import MIMEBase
from email import Utils,Encoders
from email.utils import parseaddr, formataddr
import smtplib
import sys

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

#from_addr = raw_input('From: ')
#password = raw_input('Password: ')
#to_addr = raw_input('To: ')
#smtp_server = raw_input('SMTP server: ')
from_addr = "hsgene_todaysoft@163.com"
password = "hsgene123"
#to_addr = "zj_bupt@sina.com"
to_addr = ["zj_bupt@sina.com","1094253356@qq.com"]
#to_addr = sys.argv[1]
#to_addr = []
#f = open('test.txt','r')
#for ln in f:
#	if ln in to_addr:
#		continue
#	to_addr.append(ln)
#f.close()
smtp_server = 'smtp.163.com'


#text
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#html
#msg = MIMEText('<html><body><h1>Hello</h1>' +
#    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#    '</body></html>', 'html', 'utf-8')

#attatchment
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python <%s>' % from_addr)
msg['To'] = _format_addr(u'<%s>' % to_addr)
#msg['To'] = ",".join(to_addr)
msg['Subject'] = Header(u'sayhello', 'utf-8').encode()
#text part
#msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))


#attatchment part  附件1 图片
with open('E:\\test.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('image', 'jpg', filename='test.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    #把图片插入正文
    msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    	'<p><img src="cid:0"></p>' +
    	'</body></html>', 'html', 'utf-8'))
    # 添加到MIMEMultipart:
    msg.attach(mime)
#attatchment part 附件2 文本
part = MIMEApplication(open('E:\\test.txt','rb').read())  
part.add_header('Content-Disposition', 'attachment', filename="test.txt")  
msg.attach(part) 
    
#明文传输
server = smtplib.SMTP(smtp_server, 25)
#加密传输 端口从C:\Anaconda2\Lib\smtplib.py  line 58读到
#server = smtplib.SMTP(smtp_server,465)
#server = smtplib.SMTP_SSL(smtp_server, 465 )
#server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
