from rest_framework import serializers
from .models import *


class ExperienceSerializer(serializers.ModelSerializer):

	class Meta:
		model = experience
		exclude = ('id',)


class EducationSerializer(serializers.ModelSerializer):

	class Meta:
		model = education
		exclude = ('id',)

class HobbiesSerializer(serializers.ModelSerializer):

	class Meta:
		model = hobbies
		exclude = ('id',)

class LanguageSerializer(serializers.ModelSerializer):

	class Meta:
		model = language
		exclude = ('id',)

class SkillsSerializer(serializers.ModelSerializer):

	class Meta:
		model = requiredskills
		# fields = ('name',)
		exclude = ('id',)




# Resume
class ResumeSectionSerializer(serializers.ModelSerializer):
	user = serializers.StringRelatedField(many=False)

	skills_select = SkillsSerializer(many=True, required=False)
	language = LanguageSerializer(many=True)
	hobbies = HobbiesSerializer(many=True)
	education = EducationSerializer(many=True)
	experience = ExperienceSerializer(many=True)

	class Meta:
		model = ResumeSection
		# fields = ('skills_select', 'user', 'language', 'hobbies', 'education', 'experience')
		fields = '__all__'



	def save(self):
		user = self.context['request'].user
		data = self.data

		

		skills = []
		languages = []
		hobbies_ls = []
		education_ls = []
		experience_ls = []


		all_skills_request = data['skills_select']
		all_languages_request = data['language']
		all_hobbies_request = data['hobbies']
		all_education_request = data['education']
		all_experience_request = data['experience']
 

		for skill in all_skills_request:
			obj = requiredskills.objects.get_or_create(**skill)[0]
			skills.append(obj)

		for lan in all_languages_request:
			languages.append(language.objects.get_or_create(**lan)[0])

		for hobby in all_hobbies_request:
			hobbies_ls.append(hobbies.objects.get_or_create(**hobby)[0])

		for edu in all_education_request:
			education_ls.append(education.objects.get_or_create(**edu)[0])

		for exp in all_experience_request:
			experience_ls.append(experience.objects.get_or_create(**exp)[0])
		



		del data['skills_select']
		del data['language']
		del data['hobbies']
		del data['education']
		del data['experience']



		instance = self.Meta.model(
			user=user,
			**data
		)


		instance.save()
		instance.skills_select.add(*skills)
		instance.language.add(*languages)
		instance.hobbies.add(*hobbies_ls)
		instance.education.add(*education_ls)
		instance.experience.add(*experience_ls)

		instance.save()
		return instance





# Job Post
class JobPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = JobPost
		fields = '__all__'

	def save(self, validated_data, user):
		instance =self.Meta.model(
			user=user,
			**validated_data
		)
		instance.save()
		return instance

# Adding a company (admin)
class AddingCompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = AddingCompany
		fields = '__all__'

	
	def save(self, validated_data, user):
		instance = self.Meta.model(
			user=user,
			**validated_data
		)

		instance.save()
		return instance

