from django.views import generic
from rest_framework import serializers
from .models import *


# foreign keylarga serializer chiqariladimi

# Resume
class ResumeSectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResumeSection
		fields = '__all__'


# Job Post
class JobPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = JobPost
		fields = '__all__'


# Adding a company (admin)
class AddingCompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = AddingCompany
		fields = '__all__'