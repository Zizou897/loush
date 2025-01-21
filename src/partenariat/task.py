import logging

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from core.celery import app
logger = logging.getLogger(__name__)


@app.task
def send_costumize_email(subjet: str, receivers: list, template: str, context: dict):
    """
        pour envoyer des emails personalisés
    """
    
    try:
        message = render_to_string(template, context)
        send_mail(
            subjet,
            message,
            settings.EMAIL_HOST_USER,
            receivers,
            fail_silently=True,
            html_message=message
        )
        
        return True
         
    except Exception as e:
        logger.error(e)
    
    return False