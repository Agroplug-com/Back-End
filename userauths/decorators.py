from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def email_verification_required(view_func):
    """
    Decorator that checks if a user's email is verified.
    If not verified, redirects to resend verification page.
    Requires user to be logged in first.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Use Django's login_required behavior
            return redirect('userauths:login')
        
        if not request.user.email_verified:
            messages.error(request, 'Please verify your email first. Check your inbox for the verification link.')
            return redirect('userauths:resend-verification')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper


def login_and_email_verified(view_func):
    """
    Combination decorator: requires both login AND email verification.
    More concise than stacking @login_required and @email_verification_required.
    """
    return login_required(email_verification_required(view_func), login_url='userauths:login')
