from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password, ValidationError
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import datetime

from .models import Message


def homePageView(request):
    return render(request, 'pages/home.html')


@csrf_exempt  # BUG: A03:2021 - Injection: Cross site scripting (XSS)
def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            validate_password(password)
        except ValidationError:
            # BUG: A07:2021 – Identification and Authentication Failures: Permits weak passwords
            pass
        User.objects.create_user(
            username=username, email=email, password=password)
        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        return redirect('pre_messaging')
    return render(request, 'pages/register.html')


@login_required
def deleteMessageView(request,  **kw_args):
    recipient_id = kw_args['recipient_id']
    message_id = kw_args['message_id']
    # BUG: A01:2021 - Broken Access Control: Insecure direct object references (IDOR)
    Message.objects.filter(id=message_id).delete()
    return redirect('home', recipient_id)


@login_required
def messagePrePageView(request):
    user_id = request.user.id
    accounts = User.objects.exclude(pk=user_id).exclude(pk=1)
    recipient_id = accounts[0].id
    return redirect('messaging', recipient_id)


@login_required
def messagePageView(request, **kw_args):
    user_id = request.user.id
    accounts = User.objects.exclude(pk=user_id).exclude(pk=1)
    recipient_id = kw_args['recipient_id']
    messages = Message.objects.filter(
        Q(recipient=user_id) & Q(sender=recipient_id) | Q(recipient=recipient_id) & Q(sender=user_id)).order_by('id')
    if request.method == 'POST':
        # BUG: A02:2021 – Cryptographic Failures
        content = request.POST.get('content')
        recipient = User.objects.get(id=recipient_id)
        sender = User.objects.get(username=request.user.username)
        opened = 0
        Message.objects.create(
            content=content, sender=sender, recipient=recipient, opened=opened,
            timestamp=datetime.datetime.now())
    return render(request, 'pages/messaging.html', {'messages': messages, 'accounts': accounts})
