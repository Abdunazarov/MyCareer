from tempfile import gettempdir
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from .models import *
from .serializers import *


from datetime import datetime
from django.http import HttpResponse
from django.views import View


from django.template.loader import get_template
from . utils import render_to_pdf 

obj = ResumeSection.objects.get(id=1)

data = {
	'first_name': obj.first_name,
	'last_name': obj.last_name,
	'email': obj.email,
	'country': obj.coutry,
	'street': obj.street,

}

class GeneratePDF(View):

	def get(self, request):
		pdf = render_to_pdf('mainAPI/resume_pdf.html', data)

		# user = self.request.user.body
		# print(user)
		# print(ResumeSection.objects.get(email=user))

		# save pdf to database
		return HttpResponse(pdf, content_type='application/pdf')























# Resume Colors
class ResumeColorsViewset(viewsets.ModelViewSet):
	queryset = ResumeColors.objects.all()
	serializer_class = ResumeColorsSerializer


# Resume Section
class ResumeSectionViewset(viewsets.ModelViewSet):
	queryset = ResumeSection.objects.all()
	serializer_class = ResumeSectionSerializer


# Job Post
class JobPostViewset(viewsets.ModelViewSet):
	queryset = JobPost.objects.all()
	serializer_class = JobPostSerializer


# Adding Company
class AddingCompanyViewset(viewsets.ModelViewSet):
	queryset = AddingCompany.objects.all()
	serializer_class = AddingCompanySerializer


# --------------------------------------------------------------------------------------------
# Home Page Search
class HomePageSearchView(generics.ListCreateAPIView):
	serializer_class = JobPostSerializer
	permission_classes = (IsAuthenticated,) 
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]

	search_fields = ['id', 'skills', 'freelancer_type', 'location']


	def perform_create(self, serializer):
		return serializer.save(owner=self.request.user)

	def get_queryset(self):
		return JobPost.objects.filter(owner=self.request.user)


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



# def contactView(request):
# 	if request.method == 'POST':




