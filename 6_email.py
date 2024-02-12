import smtplib
import ssl 
import mimetypes
from email.message import EmailMessage
from dotenv import load_dotenv
import os 

load_dotenv()
# 1 - Dados do E-mail
password = os.getenv("PASSWORD")
from_email =os.getenv("EMAIL")
to_email = "emailquevaireceber@example.com"
subjective = "Automação Planilha"
body = """
Olá, segue em anexo a automação da planilha 
para a empresa XYZ Automação.

Qualquer dúvida estou a disposição!
"""

# 2 - Montando a estrutura do e-mail.
message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subjective
message.set_content(body)
safe = ssl.create_default_context()

# 3 - Anexando arquivo

anexo = "teste.xlsx"
mime_type,  mime_subtype = mimetypes.guess_type(anexo)[0].split("/")
with open(anexo, "rb") as a:
    message.add_attachment(a.read(), 
    maintype=mime_type, 
    subtype=mime_subtype, 
    filename=anexo
    )

    # 4 - Enviando e-mail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
        smtp.login(from_email, password)
        smtp.sendmail(
            from_email, 
            to_email, 
            message.as_string()
        )
