from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('register/', views.registerView, name='register'),
    path('msg/', views.messagePrePageView, name='pre_messaging'),
    path('msg/id=<int:recipient_id>', views.messagePageView, name='messaging'),
    path('msg/id=<int:recipient_id>&del=<int:message_id>',
         views.deleteMessageView, name='delete_message')
]
