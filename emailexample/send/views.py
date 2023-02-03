from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        sender_email = request.POST['email']
        msg = request.POST['msg']

        #send email
        email = EmailMessage(
            'Test Email', #subject
            f'Hi There {name}!, \n Thank you for contacting us. This is your message: \n\n {msg}',
            settings.EMAIL_HOST_USER, #sender
            [sender_email] # receiver 
        )

        email.fail_silently = True
        email.send()

    return render(request, "send/index.html")
 