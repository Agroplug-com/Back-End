from django.shortcuts import render
from userauths.decorators import email_verification_required

# Create your views here.
@email_verification_required
def dashboard(request):
    return render(request, 'store/dashboard.html')