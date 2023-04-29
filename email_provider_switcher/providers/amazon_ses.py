from .email_provider import EmailProvider


class AmazonSES(EmailProvider):
    def send_email(self, to: str, subject: str, body: str) -> None:
        # Amazon SES に適したメール送信処理を実装

        print("AmazonSES send_email", to, subject, body)
        return None
