from dataclasses import field
from operator import mod
from rest_framework import serializers
from .models import (Jobs, ResumeColor, ResumePersonalInfo, ResumeAddress,
 ResumeSkills, ResumeContacts, socialmedia, ResumeExperience, ResumeEducation, 
  ResumeInterests, JobPost, PersonalInfo, AboutCompany, YourCompany, test)

# AboutWork, RequiredSkills, FindFreelancer, 


class JobsSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=250)
	description = serializers.CharField(max_length=500)
	price = serializers.IntegerField()
	date = serializers.DateTimeField()



class ResumeColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResumeColor
		fields = '__all__'


class ResumePersonalInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResumePersonalInfo
		fields = '__all__'



class ResumeAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResumeAddress
		fields = '__all__'

class ResumeSkillsSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResumeSkills
		fields = '__all__'


class ResumeContactsSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResumeContacts
		fields = '__all__'

class socialmediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = socialmedia
		fields = '__all__'


class ResumeExperienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResumeExperience
		fields = '__all__'


class ResumeEducationSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResumeEducation
		fields = '__all__'


class ResumeInterestsSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResumeInterests
		fields = '__all__'


# Job Post

class FindFreelancerSerializer(serializers.ModelSerializer):
	class Meta:
		model = JobPost
		fields = ['freelancer_type', 'location']
		

class AboutWorkSerializer(serializers.ModelSerializer):
	class Meta:
		model = JobPost
		fields = ['price', 'description']


class RequiredSkillsSerializer(serializers.ModelSerializer):
	class Meta:
		model = JobPost
		fields = ['skills',]


# Adding a Company (admin)

class PersonalInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = PersonalInfo
		fields = '__all__'
		

class YourCompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = YourCompany
		fields = '__all__'


class AboutCompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = AboutCompany
		fields = '__all__'


	
class testFirstSerializer(serializers.ModelSerializer):
	class Meta:
		model = test
		fields = ['FIRST_text']


class testSecondSerializer(serializers.ModelSerializer):
	class Meta:
		model = test
		fields = ['SECOND_text']


