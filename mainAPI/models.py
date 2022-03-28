from operator import mod
from statistics import mode
from tabnanny import verbose
from django.db import models
from colorfield.fields import ColorField
from django_countries.fields import CountryField
from django.conf import settings


# Resume Colors
class ResumeColors(models.Model):
	color1 = ColorField()
	color2 = ColorField()
	color3 = ColorField()
	color4 = ColorField()
	color5 = ColorField()
	color6 = ColorField()

	def __str__(self):
		return 'color'

	class Meta:
		verbose_name = 'Color'
		verbose_name_plural = 'Colors'

# Resume Section

class ResumeSection(models.Model):

	# Resume Personal Information
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
	photo = models.ImageField(blank=True)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.EmailField()
	phone = models.CharField(max_length=20)

	# Resume Address
	coutry = CountryField()
	region = models.CharField(max_length=70)
	district = models.CharField(max_length=70)
	quarter = models.CharField(max_length=100)
	street = models.CharField(max_length=150)

	# Resume Skills
	skills_select = models.ManyToManyField('requiredskills', related_name='resumeSkills')
	your_skills = models.ManyToManyField('requiredskills', related_name='resumeYourSkills')
	language = models.CharField(max_length=70)
	about_you = models.TextField()

	# Resume Contacts
	website_link = models.CharField(max_length=250)
	social_media = models.ManyToManyField('socialmedia')

	# Resume Experience
	company_name = models.CharField(max_length=150)
	role = models.CharField(max_length=150)
	info = models.TextField()

	# Resume Education
	university = models.CharField(max_length=150)
	degree = models.CharField(max_length=150)
	info = models.TextField()

	# Resume Interests
	hobbies = models.ManyToManyField('Hobbies')
	info = models.TextField()


	def __str__(self):
		return self.first_name + ' ' + self.last_name + '-' + self.email

	class Meta:
		verbose_name = 'Resume'
		verbose_name_plural = 'Resumes'


# Foreign Keys for Resume
class Hobbies(models.Model):
	hobby = models.CharField(max_length=150)

	def __str__(self):
		return self.hobby

	class Meta:
		verbose_name = 'Hobby (for Resume)'
		verbose_name_plural = 'Hobbies (for Resume)'	


class socialmedia(models.Model):
	platform_name = models.CharField(max_length=30)
	link = models.CharField(max_length=250)

	def __str__(self):
		return self.platform_name

	class Meta:
		verbose_name = 'Social Media (for Resume)'
		verbose_name_plural = 'Social Media (for Resume)'
	
# ----------------------------------------------------------------------------------------

# Posting Job

class JobPost(models.Model):
	# 1
	freelancer_type = models.CharField(max_length=100)
	location = CountryField()

	# 2
	price = models.IntegerField()
	description = models.TextField()	

	# 3
	skills = models.ManyToManyField('requiredskills')


	def __str__(self):
		return self.freelancer_type
	
	class Meta:
		verbose_name = 'Post Job'
		verbose_name_plural = 'Posted Jobs'


# Foreign key for JobPost
class requiredskills(models.Model):
	skills = models.CharField(max_length=100)

	def __str__(self):
		return self.skills

	class Meta:
		verbose_name = 'Required Skill (for JobPost)'
		verbose_name_plural = 'Required Skills (for JobPost)'
# ------------------------------------------------------------------------------------------------------------


# Adding a company (admin) 

class AddingCompany(models.Model):
	# Personal information
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=70)

	# Your company
	company_name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)

	# About Company
	company_link = models.CharField(max_length=300)
	company_phone = models.CharField(max_length=70)
	about_company = models.TextField()


	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' ' + self.company_name

	class Meta:
		verbose_name = 'Company'
		verbose_name_plural = 'Added Companies'




class sending_email(models.Model):
	name = models.CharField(max_length=250)
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return self.email
	

class PDF(models.Model):
	file = models.FileField()

	def __str__(self):
		return str(self.file)