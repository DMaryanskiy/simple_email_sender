from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import EmailForm

def index(request):
    """ main function which sends emails using form """
    messageSent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = cd['message']
            recipents = cd['recipents'].split(', ')
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipents)
            messageSent = True
    else:
        form = EmailForm()
    return render(request, 'index.html', {
        'form': form,
        'messageSent': messageSent,
    })
