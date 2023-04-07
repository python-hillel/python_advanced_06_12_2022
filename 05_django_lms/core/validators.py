from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

DOMAINS = ('gmail.com', 'yahoo.com')


def validate_email_domain(value):       # email_name@domain.com  --> ['email_name', 'domain.com']
    # domains = ('gmail.com', 'yahoo.com')
    domain = value.split('@')[-1]
    # if domain not in domains:
    if domain not in DOMAINS:
        raise ValidationError(f'Emails domain "{domain}" is not correct.')


@deconstructible
class ValidateEmailDomain:
    def __init__(self, *domains):
        if domains:
            self.domains = tuple(domains)
        else:
            self.domains = DOMAINS

    def __call__(self, *args, **kwargs):
        domain = args[0].split('@')[-1]
        if domain not in self.domains:
            raise ValidationError(f'Emails domain "{domain}" is invalid.')
