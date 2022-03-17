from email.mime import base
from django.contrib import admin
from django.urls import path, include
from .views import (HomePageSearchView, ResumeColorViewset,
 ResumePersonalInfoViewset, ResumeAddressViewset, ResumeSkillsViewset,
 ResumeContactsViewset, socialmediaViewset, ResumeExperienceViewset, ResumeEducationViewset,
  ResumeInterestsViewset, AboutWorkViewset, RequiredSkillsViewset, FindFreelancerViewset, contact,
  PersonalInfoViewset, YourCompanyViewset, AboutCompanyViewset)
# from .views import AboutWorkView
from rest_framework import routers


router = routers.DefaultRouter()

# Resume
router.register(r'ResumeColor', ResumeColorViewset)
router.register(r'ResumePersonalInfo', ResumePersonalInfoViewset)
router.register(r'ResumeAddress', ResumeAddressViewset)
router.register(r'ResumeSkills', ResumeSkillsViewset)
router.register(r'ResumeContacts', ResumeContactsViewset)
router.register('ResumeExperience', ResumeExperienceViewset)
router.register('ResumeEducation', ResumeEducationViewset)
router.register('ResumeInterests', ResumeInterestsViewset)
# Posting Job
router.register('AboutWork', AboutWorkViewset)
router.register('RequiredSkills', RequiredSkillsViewset)
router.register('FindFreelancer', FindFreelancerViewset)
# Adding Company (admin)
router.register('PersonalInfo', PersonalInfoViewset)
router.register('YourCompany', YourCompanyViewset)
router.register('AboutCompany', AboutCompanyViewset)
# router.register('testFirst', testFirstView, basename='testFirst')


urlpatterns = [
    path('', include(router.urls)),
    # path('apis/', include('rest_framework')),
    # path('aboutwork/<int:model>', AboutWorkView, name='detail')
    path("contact/", contact, name="contact"), 

]