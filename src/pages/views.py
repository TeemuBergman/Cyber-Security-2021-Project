from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
import datetime

from .models import Message


@login_required
def homePageView(request, id):
    user_id = request.user.id
    messages = Message.objects.filter(
        Q(recipient=user_id) & Q(sender=id) | Q(recipient=id) & Q(sender=user_id)).order_by('id')
    accounts = User.objects.exclude(pk=user_id).exclude(pk=1)

    if request.method == 'POST':
        content = request.POST.get('content')
        recipient = User.objects.get(id=id)
        sender = User.objects.get(username=request.user.username)
        opened = 0
        Message.objects.create(
            content=content, sender=sender, recipient=recipient, opened=opened,
            timestamp=datetime.datetime.now())

    return render(request, 'pages/index.html', {'messages': messages, 'accounts': accounts})
