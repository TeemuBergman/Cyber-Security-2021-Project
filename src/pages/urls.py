from django.urls import path

from . import views

urlpatterns = [
    # path('', homePageView, name='home'),
    path('register', views.registerView, name='register'),
    path('id=<int:recipient_id>', views.homePageView, name='home'),
    path('id=<int:recipient_id>&del=<int:message_id>',
         views.deleteMessageView, name='delete_message')
]
