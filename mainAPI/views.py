from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from django.core.mail import send_mail

# from .models import (Jobs, ResumeColor, ResumePersonalInfo, ResumeAddress,
# ResumeSkills, ResumeContacts, socialmedia, ResumeExperience, ResumeEducation,
# ResumeInterests, JobPost, AboutCompany, PersonalInfo, YourCompany)
from django_filters.rest_framework import DjangoFilterBackend

# from .serializers import (JobsSerializer, ResumeColorSerializer, ResumePersonalInfoSerializer,
#  ResumeAddressSerializer, ResumeSkillsSerializer, ResumeContactsSerializer,
#   socialmediaSerializer, ResumeExperienceSerializer, ResumeEducationSerializer,
#    ResumeInterestsSerializer, AboutWorkSerializer, RequiredSkillsSerializer,
#     FindFreelancerSerializer, PersonalInfoSerializer, AboutCompanySerializer, YourCompanySerializer,
# 	testFirstSerializer)

from .models import *
from .serializers import *

from rest_framework import viewsets, status


# AboutWork, RequiredSkills, FindFreelancer

class HomePageSearchView(ListAPIView):
	queryset = Jobs.objects.all()
	serializer_class = JobsSerializer
	filter_backends = (DjangoFilterBackend, SearchFilter)
	search_fields = ('name', 'description')


class ResumeColorViewset(viewsets.ModelViewSet):
	queryset = ResumeColor.objects.all()
	serializer_class = ResumeColorSerializer


class ResumePersonalInfoViewset(viewsets.ModelViewSet):
	queryset = ResumePersonalInfo.objects.all()
	serializer_class = ResumePersonalInfoSerializer


class ResumeAddressViewset(viewsets.ModelViewSet):
	queryset = ResumeAddress.objects.all()
	serializer_class = ResumeAddressSerializer


class ResumeSkillsViewset(viewsets.ModelViewSet):
	queryset = ResumeSkills.objects.all()
	serializer_class = ResumeSkillsSerializer


class ResumeContactsViewset(viewsets.ModelViewSet):
	queryset = ResumeContacts.objects.all()
	serializer_class = ResumeContactsSerializer


class socialmediaViewset(viewsets.ModelViewSet):
	serializer_class = socialmediaSerializer
	queryset = socialmedia.objects.all()


class ResumeExperienceViewset(viewsets.ModelViewSet):
	serializer_class = ResumeExperienceSerializer
	queryset = ResumeExperience.objects.all()


class ResumeEducationViewset(viewsets.ModelViewSet):
	serializer_class = ResumeEducationSerializer
	queryset = ResumeEducation.objects.all()


class ResumeInterestsViewset(viewsets.ModelViewSet):
	serializer_class = ResumeInterestsSerializer
	queryset = ResumeInterests.objects.all()



# Job Post

# @csrf_exempt
# def testFirstView(request):
# 	if request.method == 'POST':
# 		tests = test.objects.all()
# 		serializer = testFirstSerializer(tests)
# 		return JsonResponse(serializer.data, safe=False)

# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = testFirstSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status=201)
# 		return JsonResponse(serializer.errors, status=400)





class AboutWorkViewset(viewsets.ModelViewSet):
	serializer_class = AboutWorkSerializer
	queryset = JobPost.objects.all()



class RequiredSkillsViewset(viewsets.ModelViewSet):
	serializer_class = RequiredSkillsSerializer
	queryset = JobPost.objects.all()


class FindFreelancerViewset(viewsets.ModelViewSet):
	serializer_class = FindFreelancerSerializer
	queryset = JobPost.objects.all()


# Contact Uss

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


# Adding a Company (admin)

class AboutCompanyViewset(viewsets.ModelViewSet):
	serializer_class = AboutCompanySerializer
	queryset = AboutCompany.objects.all()



class PersonalInfoViewset(viewsets.ModelViewSet):
	serializer_class = PersonalInfoSerializer
	queryset = PersonalInfo.objects.all()


class YourCompanyViewset(viewsets.ModelViewSet):
	serializer_class = YourCompanySerializer
	queryset = YourCompany.objects.all()