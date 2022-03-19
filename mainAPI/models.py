from operator import mod
from django.db import models
from colorfield.fields import ColorField
from django_countries.fields import CountryField


# class Jobs(models.Model):
# 	name = models.CharField(max_length=250)
# 	description = models.TextField()
# 	price = models.IntegerField()
# 	date = models.DateTimeField()

# 	def __str_(self):
# 		return self.name


class ResumeColor(models.Model):
	color1 = ColorField()
	color2 = ColorField()
	color3 = ColorField()
	color4 = ColorField()
	color5 = ColorField()
	color6 = ColorField()

	def __str__(self):
		return('Resume Colors')


class ResumePersonalInfo(models.Model):
	photo = models.ImageField(blank=True)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.EmailField()
	# phone = PhoneNUmberField()
	phone = models.CharField(max_length=20)
	password = models.CharField(max_length=20)


	def __str__(self):
		return self.first_name


class ResumeAddress(models.Model):
	coutry = CountryField()
	region = models.CharField(max_length=70)
	district = models.CharField(max_length=70)
	quarter = models.CharField(max_length=100)
	street = models.CharField(max_length=150)

	def __str__(self):
		return self.region


class ResumeSkills(models.Model):
	skills_select = models.CharField(max_length=70)
	your_skills = models.CharField(max_length=70)
	language = models.CharField(max_length=70)
	# about_you = RichTextField()  # code bilan berlishini so'rash****

	def __str__(self):
		return self.language


class socialmedia(models.Model):
	platform_name = models.CharField(max_length=30)
	link = models.CharField(max_length=250)

	def __str__(self):
		return self.platform_name


class ResumeContacts(models.Model):
	website_link = models.CharField(max_length=250)
	social_media = models.ManyToManyField(socialmedia)

	def __str__(self):
		return self.website_link


class ResumeExperience(models.Model):
	company_name = models.CharField(max_length=150)
	role = models.CharField(max_length=150)
	info = models.TextField()


	def __str__(self):
		return self.company_name


class ResumeEducation(models.Model):
	university = models.CharField(max_length=150)
	degree = models.CharField(max_length=150)
	info = models.TextField()


	def __str__(self):
		return self.university

class Hobbies(models.Model):
	hobby = models.CharField(max_length=150)



class ResumeInterests(models.Model):
	hobbies = models.ManyToManyField(Hobbies)  # xato!
	info = models.TextField()


	def __str__(self):
		return self.hobbies.__str__()


# Posting Job

class requiredskills(models.Model):
	skills = models.CharField(max_length=100)

	def __str__(self):
		return self.skills


class JobPost(models.Model):
	# 1
	freelancer_type = models.CharField(max_length=100)
	location = CountryField()

	# 2
	price = models.IntegerField()
	description = models.TextField()	

	# 3
	skills = models.ManyToManyField(requiredskills)


	def __str__(self):
		return self.freelancer_type



# Adding a company (admin) 

class AddingCompany(models.Model):
	# Persona information
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


class PersonalInfo(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=70)

	def __str__(self):
		return self.first_name + ' ' + self.last_name



class YourCompany(models.Model):
	company_name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)


	def __str__(self):
		return self.company_name


class AboutCompany(models.Model):
	company_link = models.CharField(max_length=300)
	company_phone = models.CharField(max_length=70)
	about_company = models.TextField()


	def __str__(self):
		return str(self.about_company)[0:20]


# class test(models.Model):
# 	FIRST_text = models.TextField(null=True)
# 	SECOND_text = models.TextField(null=True)

# 	def __str__(self):
# 		return self.FIRST_text