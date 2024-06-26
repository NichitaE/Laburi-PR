import smtplib
import imaplib
import poplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email_with_attachment():
    adresa_email = "edunikita@gmail.com"
    parola_email = "tqjo mruf umtf xpzj"
    adresa_destinatar = "edunikita@gmail.com"

    mesaj = MIMEMultipart()
    mesaj["From"] = adresa_email
    mesaj["To"] = adresa_destinatar
    mesaj["Subject"] = "E-mail de test."
    corp_mesaj = "E-mail de test."
    mesaj.attach(MIMEText(corp_mesaj, "plain"))

    file_path = r"\Users\Enter\Desktop\UTM\Anul 3\TPP\TPP_TI211_Edu_Nichita_laborator1.docx"  
    with open(file_path, "rb") as file:
        part = MIMEApplication(file.read(), Name="file.txt")
        part["Content-Disposition"] = f"attachment; filename={file_path}"
        mesaj.attach(part)

    server_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    server_smtp.starttls()
    server_smtp.login(adresa_email, parola_email)
    server_smtp.sendmail(adresa_email, adresa_destinatar, mesaj.as_string())
    server_smtp.quit()

    print(f"Email with attachment sent to {adresa_destinatar}")

def get_email_list_using_imap():
    adresa_email = "edunikita@gmail.com"
    parola_email = "tqjo mruf umtf xpzj"

    server_imap = imaplib.IMAP4_SSL("imap.gmail.com")
    server_imap.login(adresa_email, parola_email)
    server_imap.select("inbox")

    status, id_uri_email = server_imap.search(None, "ALL")
    if status == "OK":
        for id_email in id_uri_email[0].split()[0:5]: 
            status, date_email = server_imap.fetch(id_email, "(RFC822)")
            if status == "OK":
                mesaj_email = date_email[0][1].decode("utf-8", errors="ignore")  
                print(f"Email content for email ID {id_email}:\n{mesaj_email}\n")

    server_imap.logout()

def get_email_list_using_pop3():
    adresa_email = "edunikita@gmail.com"
    parola_email = "tqjo mruf umtf xpzj"

    server_pop3 = poplib.POP3_SSL("pop.gmail.com", 995)
    server_pop3.user(adresa_email)
    server_pop3.pass_(parola_email)

    num_emails, _ = server_pop3.stat()
    num_to_list = min(num_emails, 5)
    for i in range(num_to_list):
        _, email_lines, _ = server_pop3.retr(i + 1)
        mesaj_email = b"\n".join(email_lines).decode("utf-8", errors="ignore")
        print(f"Email {i + 1}:\n{mesaj_email}\n")
    server_pop3.quit()

def main():
    choice = input("Alege o optiune:\n1. Afisati lista de e-mail folosind IMAP\n2. Afisati lista de e-mail folosind POP3\nIntroduceti 1 sau 2: ")

    if choice == "1":
        get_email_list_using_imap()
    elif choice == "2":
        get_email_list_using_pop3()
    else:
        print("Alegere incorecta. Introduceti 1 sau 2.")

if __name__ == "__main__":
    send_email_with_attachment()

    main()