import os.path
import smtplib
import glob
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail(mail_id, mail_pass, name, email, attach_url, subject, body):
    try:
        # 네이버
        smtp_nmail = smtplib.SMTP_SSL('smtp.naver.com', 465) #tls 부분 주석 처리 필요
        #smtp_nmail = smtplib.SMTP_SSL('smtp.gmail.com', 587)
        smtp_nmail.ehlo()
        #smtp_nmail.starttls
        smtp_nmail.login(mail_id, mail_pass)

    except smtplib.SMTPRecipientsRefused:
        print('로그인 에러 - 잘 못된 아이디 패스워드')

    except smtplib.SMTPAuthenticationError:
        print('로그인 에러')

    except smtplib.SMTPException:
        print('에러')

    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = mail_id + '@naver.com'
    msg['To'] = email

    mail_body = MIMEText(body, 'html', 'utf-8')
    msg.attach(mail_body)

    pdf_list = glob.glob(attach_url + "/*" + name + "*.pdf")
    print(pdf_list)
    for file_path in pdf_list:
        with open(file_path, "rb") as f:
            attach = MIMEApplication(f.read())
            attach.add_header('Content-Disposition', 'attachment', filename=os.path.split(file_path)[1])
            print(os.path.split(file_path)[1] + " : 첨부")
            msg.attach(attach)

    if len(msg.get_payload()) <= 1:
        send_status = "첨부 없음"

    else:
        try:
            smtp_nmail.send_message(msg)
            send_status = "성공"
        except Exception as e:
            print('이메일 발송에 실패했습니다. 오류 메시지:', str(e))
            send_status = "실패"
        finally:
            smtp_nmail.quit()

    return send_status
