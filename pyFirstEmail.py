import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

email = EmailMessage()
email['Subject'] = "First email from Python"
email['From'] = "Me@gmail.com"
email['To'] = "ihpnip@ogcio.gov.hk"

# read in the html file as email content
html = Template(Path("./email_body.html").read_text())

# replace $name by Ivan, $sex by M, $age by 18 in the template object
email.set_content(html.substitute({"name": "Ivan", "sex": "M", "age": 18}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user="xxxxx@gmail.com", password="*******")
    smtp.sendmail(email)
