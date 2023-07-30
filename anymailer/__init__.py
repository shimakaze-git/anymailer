# email_provider_switcher/__init__.py
# from email_provider_switcher.mailer import Mailer
# from email_provider_switcher.config import load_config

# config = load_config()


def send_email(to: str, subject: str, body: str, provider: str | None = None) -> None:
    if not property:
        # if provider is None:
        return None
        # provider = config['email_provider']

    # mailer = Mailer(provider=provider)
    # mailer.send_email(to, subject, body)
