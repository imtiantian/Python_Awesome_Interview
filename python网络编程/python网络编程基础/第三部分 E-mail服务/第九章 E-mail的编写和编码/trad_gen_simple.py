#!/usr/bin/env python
from email.MIMEText import MIMEText
message = 'lll'
msg = MIMEText(message)
msg['To'] = 'linhanqiu1123@163.com'
msg['From'] = 'Test Sender <sender@example.com >'
msg['Subject'] = 'c9'
print msg.as_string()
