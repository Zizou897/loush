import logging
import socket
import after_response
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
logger = logging.getLogger(__name__)


@after_response.enable
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
        logger.error(f"Erreur lors de l'envoi de l'email : {e}")
    
    return False





def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Utiliser 8.8.8.8 comme serveur DNS
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip