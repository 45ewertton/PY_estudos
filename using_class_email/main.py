from email_provider import EmailProvider

def main():
    stop = True
    email_provider = EmailProvider("Google", "ewertton45mb@gmail.com")
    email_provider.__show_password()

    while not stop:
        subject = input("Digite o assunto: ")
        body = input("Digite a mensagem: ")
        receiver = input("Digite o destinatário: ")

        email_provider.send_email(subject, body, receiver)

        resp = input("Você deseja enviar outro e-mail? (s/n) ")

        if resp != "s":
            stop = True
    
    email_provider.open_outbox()

main()