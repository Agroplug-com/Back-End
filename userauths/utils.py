from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from Agrosite import settings
from django.urls import reverse

def send_verification_email(user, request):
    """
    Send verification email to user
    """
    # Generate verification URL
    verification_url = request.build_absolute_uri(
        reverse('userauths:verify-email', kwargs={'token': str(user.verification_token)})
    )
    
    # Email content
    subject = 'Verify Your Email - Abiagrow.connect'
    
    # HTML email template
    html_message = render_to_string('emails/verification_email.html', {
        'user': user,
        'verification_url': verification_url,
        'site_name': 'Abiagrow.connect'
    })
    
    # Plain text version
    plain_message = strip_tags(html_message)
    
    # Send email
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html_message,
        fail_silently=False,
    )

def send_welcome_email(user):
    """
    Send welcome email after verification
    """
    subject = 'Welcome to Abiagrow.connect!'
    
    html_message = render_to_string('emails/welcome_email.html', {
        'user': user,
        'site_name': 'Abiagrow.connect'
    })
    
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html_message,
        fail_silently=False,
    )