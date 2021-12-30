from django.urls import path

from .views import homePageView

urlpatterns = [
    # path('', homePageView, name='home'),
    path('id=<int:id>', homePageView, name='home')
]
