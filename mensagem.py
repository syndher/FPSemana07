class Mensagem:
    def enviar_mensagem(self):
        raise NotImplementedError()

class Email(Mensagem):
    def __init__(self, destinatario, assunto, corpo):
        self.destinatario = destinatario
        self.assunto = assunto
        self.corpo = corpo

    def enviar_mensagem(self):
        print(f"Email({self.destinatario}). Assunto: {self.assunto}")

class SMS(Mensagem):
    def __init__(self, numero, mensagem):
        self.numero = numero
        self.mensagem = mensagem

    def enviar_mensagem(self):
        print(f"SMS({self.numero}). {self.mensagem}")

class NotificacaoPush(Mensagem):
    def __init__(self, dispositivo_id, mensagem):
        self.dispositivo_id = dispositivo_id
        self.mensagem = mensagem

    def enviar_mensagem(self):
        print(f"Notificação Push({self.dispositivo_id}). {self.mensagem}")

def realizar_envio(mensagem: Mensagem):
    mensagem.enviar_mensagem()

if __name__ == "__main__":
    email = Email(destinatario="joao.silva@email.com", assunto="Reunião", corpo="Reunião marcada para as 10h.")
    sms = SMS(numero="912345678", mensagem="A sua Encomenda Chegou!")
    notificacao = NotificacaoPush(dispositivo_id="abc123", mensagem="Tem uma Nova Mensagem.")

    realizar_envio(email)
    realizar_envio(sms)
    realizar_envio(notificacao)