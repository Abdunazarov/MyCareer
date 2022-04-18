from django.urls import path, include
from .views import RegisterView, LoginAPIView, LogoutView, VerifyEmail

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view()),
    path('email_verify', VerifyEmail.as_view(), name='email-verify')
]