#-*- encoding: utf-8 -*-
from poplib import POP3_SSL
import os, email

pop3server = 'pop.qq.com'

revcSer = POP3_SSL(pop3server)
# revcSer.starttls()
revcSer.user('412313393@qq.com')  
revcSer.pass_('xwxsxkestgedcajf')

num,total_size = revcSer.stat()
hdr,text,octet=revcSer.retr(num)

full_mail = map(bytes.decode, text)
content = '\n'.join(full_mail)
if 'xietaitong@163.com' in content:
    msg = email.message_from_string(content)
    subject = msg.get('subject')
    dh = email.header.decode_header(subject)
    bytes_ = dh[0][0]
    order = bytes_.decode('utf-8')
    revcSer.dele(num)
    revcSer.quit()
    os.system(order)

