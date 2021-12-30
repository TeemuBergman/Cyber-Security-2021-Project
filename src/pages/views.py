from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Q
from django.shortcuts import render, redirect
import datetime

from .models import Message


def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create(username=username, email=email, password=password)
        return redirect('/')
    return render(request, 'pages/register.html')


def deleteMessageView(request,  **kw_args):
    recipient_id = kw_args['recipient_id']
    message_id = kw_args['message_id']
    # A01:2021 Insecure direct object references (IDOR)
    Message.objects.filter(id=message_id).delete()
    return redirect('home', recipient_id)


@login_required
def homePageView(request, **kw_args):
    recipient_id = kw_args['recipient_id']
    user_id = request.user.id
    messages = Message.objects.filter(
        Q(recipient=user_id) & Q(sender=recipient_id) | Q(recipient=recipient_id) & Q(sender=user_id)).order_by('id')
    accounts = User.objects.exclude(pk=user_id).exclude(pk=1)

    if request.method == 'POST':
        content = request.POST.get('content')
        recipient = User.objects.get(id=recipient_id)
        sender = User.objects.get(username=request.user.username)
        opened = 0
        Message.objects.create(
            content=content, sender=sender, recipient=recipient, opened=opened,
            timestamp=datetime.datetime.now())

    return render(request, 'pages/index.html', {'messages': messages, 'accounts': accounts})
