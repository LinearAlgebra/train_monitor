from poplib import POP3_SSL
import re, os

pop3server = 'pop.qq.com'

revcSer = POP3_SSL(pop3server)
# revcSer.starttls()
revcSer.user('412313393@qq.com')  
revcSer.pass_('xwxsxkestgedcajf')

num,total_size = revcSer.stat()
hdr,text,octet=revcSer.retr(num)

full_mail = map(bytes.decode, text)
content = ''.join(full_mail)
if 'xietaitong@163.com' in content:
    pattern = re.compile('Subject: (.+?)From')
    ans = re.search(pattern, content)
    order = ans.group(1)
    os.system(order)
    revcSer.dele(num)
    revcSer.quit()
