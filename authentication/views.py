from rest_framework import generics, status, views, permissions
from .serializers import (RegisterSerializer, EmailVerificationSerializer, LoginSerializer, UserSerializer, SendCodeSerializer,
ResetPasswordSerializer)
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg import openapi
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from django.shortcuts import redirect


class RegisterView(generics.GenericAPIView):

    '''1) Kerakli parametrlarni kiritilgandan keyin, kiritilgan emailga accountni aktivatsiya qilish uchun ssilka yuboriladi, 
    osha ssilkaga o'tgandan keyingina userga token beriladi.
    2) "role" digan fieldga faqat "Freelancer" yoki "Company" kiritish mumkin'''

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = f"<h2>Hi {user.email}, use the link below to verify your email:</h2> \n" + absurl
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}
        print(data)

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    ''' Bu urlni tekshirish shartmas, chunki bu register/ urldan kegin o'zi avtomatik ravishda ishga tushadi '''
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class SendVerificationAgainView(views.APIView):
    '''(Birinchi bo'lib /register/ va /email-verify/ API larini o'qib chiqishni tavsiya qilaman)
    User registratsiya (/register/) qilgandan keyin emailiga aktivatsiya uchun ssilka yuboriladi, agar o'sha ssilkani bosish esidan chiqib ketsa, 
    yoki boshqa sabablarga ko'ra aktivatsiya ssilkasini bosmasa, user yana bir bor aktivatsiya ssilkasini o'zini emaili orqali olishi mumkin'''


    def post(self, request):

        try:
            user = User.objects.get(email=request.data['email'])
        
        except User.DoesNotExist:
            raise serializers.ValidationError({'Error': 'User with this email does not exist'})
        
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = f"<h2>Hi {user.email}, use the link below to verify your email:</h2> \n" + absurl
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}

        Util.send_email(data)

        return Response({'Success': 'Verification link sent to the email'})



class LoginAPIView(generics.GenericAPIView):
    '''Email bilan password to'gri bo'lsa user uchun token yaratib beradi, va o'sha tokenni Headersga kiritib saytda lyuboy zaproslarni bersa bo'ladi'''

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class LogoutView(views.APIView):
    '''Oddiy logout API. Headersga userni tokenini kiritib shu APIga zapros berilsa userni logout qilib yuboradi'''

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Successfully logged out'
        }

        return response


class SendCodeView(views.APIView):
    '''(Bu URL ikki qisimdan iborat, 1) /send_code/ va 2) /reset-password/, ikkala url haqida o'qib chiqishni tavsiya qilaman)
    Kiritilgan emailga uzunligi 10ga teng bo'lgan kod yuboriladi, va o'sha kodni 2 minut ichida /password-reset/ urlga kiritish kerak '''

    serializer_class = SendCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(request.data['email'])
            code = serializer.send_code(request_data=request.data)
            request.session['reset_code'] = code
            request.session['email'] = request.data['email']
            request.session.set_expiry(120) # needs to enter code within 2 minutes

            return Response({"Success": "Code sent to email"})
        
        return Response(serializer.errors) 
    


class PasswordResetView(views.APIView):
    '''1) Bu url da uchta field bor "reset_code" fieldga emailga yuborilgan kod kiritiladi, qogan "new_password" va "new_password2" ga esa yangi parolni kiritish kerak.
    2) Emailga yuborilgan kodni 2 minut ichida kiritmasa, yuborilgan kod ishlash muddati o'tib ketadi va yana bir martta /send_code/ url ga zapros yuborishga to'g'ri keladi  '''

    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            code = request.session['reset_code']
            email = request.session['email']
            serializer.save(request.data, email, code)

            return Response({'Success': 'Password is updated'})
        
        return Response(serializer.errors)


from mainAPI.models import ResumeSection

class ProfileView(views.APIView):
    '''Headers ga userni tokeni kiritilgandan keyingina bu API ishga tushadi, kiritilgan token boyicha userni aniqlab, o'sha userni profilidegi malumotlrni chiqarib beradi'''
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        user = request.user
        resumes = [x.id for x in ResumeSection.objects.filter(user=user)] # loops and stores in list

        data = self.serializer_class(instance=user).data
        data['resumes'] = resumes 

        return Response(data)
        

