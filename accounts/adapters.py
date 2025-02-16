from allauth.account.adapter import DefaultAccountAdapter
from decouple import config

def get_base_url():
    return config("base_urls")

class CustomAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        context['protocol'] = get_base_url()
        super().send_mail(template_prefix, email, context)