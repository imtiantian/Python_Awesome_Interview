#!/usr/bin/env python
from email.MIMEText import MIMEText
from email import Utils
message = 'lll'
msg = MIMEText(message)
msg['To'] = 'linhanqiu1123@163.com'
msg['From'] = 'Test Sender <sender@example.com >'
msg['Subject'] = 'c9'
msg['Date'] = Utils.formatdate(localtime=1)
msg['Message-ID'] = Utils.make_msgid()
print msg.as_string()
