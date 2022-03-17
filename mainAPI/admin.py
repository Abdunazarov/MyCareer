from django.contrib import admin
from .models import (Jobs, ResumeColor, ResumePersonalInfo, ResumeAddress,
 ResumeSkills, ResumeContacts, socialmedia, ResumeExperience, ResumeEducation, 
  ResumeInterests, Hobbies, JobPost, requiredskills, test)

#  AboutWork, RequiredSkills,


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
	list_display = ("name", "description")

	# class Meta:
		# ordering = ("name", "description")


admin.site.register(ResumeColor)
admin.site.register(ResumePersonalInfo)
admin.site.register(ResumeAddress)
admin.site.register(ResumeSkills)
admin.site.register(test)


@admin.register(ResumeContacts)
class ContactAdmin(admin.ModelAdmin):
	list_display = ("website_link",)

	search_fields = ["social_media__platform_name",]  # Foreignkey should be filtered as it is!

admin.site.register(socialmedia)

@admin.register(ResumeExperience)
class ResumeExperienceAdmin(admin.ModelAdmin):
	list_display = ("company_name", "role")
	# title = ["role",]  # order in which fileds are shown

admin.site.register(ResumeEducation)
admin.site.register(ResumeInterests)
admin.site.register(Hobbies)
# admin.site.register(AboutWork)
# admin.site.register(RequiredSkills)
admin.site.register(JobPost)
admin.site.register(requiredskills)


