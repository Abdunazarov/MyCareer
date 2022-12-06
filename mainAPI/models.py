from django.db import models
from django_countries.fields import CountryField
from django.conf import settings
from authentication.models import User


TEMPLATE_TYPES = [
    ('1', 'Template 1'),
    ('2', 'Template 2'),
    ('3', 'Template 3'),
    ('4', 'Template 4'),
    ('5', 'Template 5'),
]

# Resume Section

class ResumeSection(models.Model):
	# Resume Template Selection
	template_type = models.CharField(max_length=1, choices=TEMPLATE_TYPES, default='1')

	# Resume Personal Information
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
	photo = models.ImageField(blank=True, null=True)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.EmailField()
	phone = models.CharField(max_length=20, blank=True, null=True)

	# Resume Address
	country = models.CharField(max_length=100)
	region = models.CharField(max_length=70, blank=True, null=True)
	district = models.CharField(max_length=70, blank=True, null=True)
	quarter = models.CharField(max_length=100, blank=True, null=True)
	street = models.CharField(max_length=150, blank=True, null=True)

	# Resume Skills
	skills_select = models.ManyToManyField('requiredskills', related_name='resumeSkills', blank=True)
	language = models.ManyToManyField('language')
	about_you = models.TextField(blank=True, null=True)

	# Resume Contacts
	website_link = models.CharField(max_length=250, blank=True, null=True)
	twitter = models.CharField(max_length=500, blank=True, null=True)
	linkedin = models.CharField(max_length=500, blank=True, null=True)
	instagram = models.CharField(max_length=500, blank=True, null=True)
	facebook = models.CharField(max_length=500, blank=True, null=True)


	# Resume Experience
	experience = models.ManyToManyField('experience', blank=True)


	# Resume Education
	education = models.ManyToManyField('education', blank=True)

	# Resume Interests
	hobbies = models.ManyToManyField('hobbies')

	def __str__(self):
		return self.first_name

	class Meta:
		verbose_name = 'Resume'
		verbose_name_plural = 'Resumes'


# Foreign Keys for Resume
class hobbies(models.Model):
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Hobby (for Resume)'
		verbose_name_plural = 'Hobbies (for Resume)'	


class socialmedia(models.Model):
	name = models.CharField(max_length=30)
	link = models.CharField(max_length=250)

	def __str__(self):
		return self.platform_name

	class Meta:
		verbose_name = 'Social Media (for Resume)'
		verbose_name_plural = 'Social Media (for Resume)'


class language(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Language'
		verbose_name_plural = 'Languages'

class experience(models.Model):
	company_name = models.CharField(max_length=150, null=True, blank=True)
	role = models.CharField(max_length=150, null=True, blank=True)
	info = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.company_name + '-' + self.role
	
	class Meta:
		verbose_name = 'Experience'
		verbose_name_plural = 'Experience'


class education(models.Model):
	university = models.CharField(max_length=150)
	degree = models.CharField(max_length=150)
	info = models.TextField()

	def __str__(self):
		return self.university + '-' + self.degree
	
	class Meta:
		verbose_name = 'Education'
		verbose_name_plural = 'Education'
# ----------------------------------------------------------------------------------------

# Posting Job

class JobPost(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	# 1
	freelancer_type = models.CharField(max_length=100)
	location = CountryField(blank=True, null=True)

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
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Required Skill'
		verbose_name_plural = 'Required Skills'
# ------------------------------------------------------------------------------------------------------------


# Adding a company (admin) 

class AddingCompany(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	# Personal information
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=70)

	# Your company
	img = models.ImageField(blank=True)
	company_name = models.CharField(max_length=200)
	number = models.CharField(max_length=50, blank=True)

	# About Company
	location = models.CharField(max_length=200)
	description = models.TextField()

	# Contacts
	website_link = models.CharField(max_length=300, blank=True)
	whatsapp = models.CharField(max_length=300, blank=True)
	facebook = models.CharField(max_length=300, blank=True)
	instagram = models.CharField(max_length=300, blank=True)
	telegram = models.CharField(max_length=300, blank=True)
	github = models.CharField(max_length=300, blank=True)
	twitter = models.CharField(max_length=300, blank=True)



	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' ' + self.company_name

	class Meta:
		verbose_name = 'Company'
		verbose_name_plural = 'Added Companies'



