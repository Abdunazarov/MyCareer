from unicodedata import name
from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()


router.register('ResumeColors', ResumeColorsViewset)
router.register('ResumeSection', ResumeSectionViewset)
router.register('JobPost', JobPostViewset)
router.register('AddingCompany', AddingCompanyViewset)



urlpatterns = [
    path('', include(router.urls)),
    path("contact/", contact, name="contact"), 
    path('pdf/', GeneratePDF.as_view(), name='pdf')

]