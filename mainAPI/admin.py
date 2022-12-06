from django.contrib import admin
from .models import *


# Resume Section (Admin)
@admin.register(ResumeSection)
class ResumeSectionAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'country')


# Job Post (Admin)
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
	list_display = ('freelancer_type', 'location', 'price')


# Adding Company (Admin)
@admin.register(AddingCompany)
class AddingCompanyAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'company_name', 'location')


# Other admin models
admin.site.register(socialmedia)
admin.site.register(hobbies)
admin.site.register(requiredskills)
admin.site.register(language)
admin.site.register(education)
admin.site.register(experience)









# 	search_fields = ["social_media__platform_name",]  # Foreignkey should be filtered as it is!


