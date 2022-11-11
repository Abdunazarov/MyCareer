from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from .models import *
from .serializers import *


# Resume Section
class ResumeSectionViewset(viewsets.ModelViewSet):
	queryset = ResumeSection.objects.all()
	serializer_class = ResumeSectionSerializer

	# Search
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['id', 'first_name', 'last_name', 'skills_select']


# Job Post
class JobPostViewset(viewsets.ModelViewSet):
	queryset = JobPost.objects.all()
	serializer_class = JobPostSerializer

	# Job search 
	# permission_classes = [IsAuthenticated]
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['id', 'skills', 'freelancer_type', 'location']


# Adding Company
class AddingCompanyViewset(viewsets.ModelViewSet):
	queryset = AddingCompany.objects.all()
	serializer_class = AddingCompanySerializer


# --------------------------------------------------------------------------------------------

# Contact Us
def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')

		data = {
			'name': name,
			'email': email,
			'message': message,
		}

		message = f"From: {data['name']} ({data['email']}) \n \n Message: {data['message']}"


		send_mail('Contact a Client', message, data['email'], ['abdunazarovdior@gmail.com'], fail_silently=False)

	return render(request, 'mainAPI/contact.html', {})




