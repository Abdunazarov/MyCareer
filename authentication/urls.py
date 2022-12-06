from django.urls import path, include
from .views import (RegisterView, LoginAPIView, LogoutView, VerifyEmail, SendCodeView, PasswordResetView, SendVerificationAgainView, 
ProfileView)


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('send-code/', SendCodeView.as_view()),
    path('password-reset/', PasswordResetView.as_view()),
    path('email-verify-again/', SendVerificationAgainView.as_view()),

    path('profile/', ProfileView.as_view())

]