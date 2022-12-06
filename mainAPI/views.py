from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import *
from .serializers import *


# Resume Section
class ResumeSectionViewset(viewsets.ModelViewSet):
	queryset = ResumeSection.objects.all()
	serializer_class = ResumeSectionSerializer
	permission_classes = [IsAuthenticated]

	# Search
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['id', 'first_name', 'last_name', 'skills_select']

	def retrieve(self, request, pk, *args, **kwargs):
		obj = self.get_object()
	
		if obj.user != request.user:
			return Response({'Error': 'You are not the owner of the resume'})

		return super().retrieve(request, *args, **kwargs)

	
	def update(self, request, pk, *args, **kwargs):
		# try:
		# 	obj = ResumeSection.objects.get(id=pk)
		# except ResumeSection.DoesNotExist:
		# 	raise serializers.ValidationError({'Error':'Object does not exist'})
		obj = self.get_object()

		if obj.user != request.user:
			return Response({'Error': 'You are not the owner of the resume'})

		return super().update(request, pk, *args, **kwargs)

	def destroy(self, request, *args, **kwargs):
		obj = self.get_object()

		if obj.user != request.user:
			return Response({'Error': 'You are not the owner of the resume'})

		return super().destroy(request, *args, **kwargs)



# Job Post
class JobPostViewset(viewsets.ModelViewSet):
	queryset = JobPost.objects.all()
	serializer_class = JobPostSerializer
	permission_classes = [IsAuthenticated]

	def create(self, request):
		user = request.user
		if user.role != 'Freelancer':
			raise serializers.ValidationError({'Error': 'You are freelancer, you cannot add job!'})

		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		data = serializer.save(request.data, user).data


		return Response(data)

	# Job search 
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['id', 'skills', 'freelancer_type', 'location']


# Adding Company
class AddingCompanyViewset(viewsets.ModelViewSet):
	queryset = AddingCompany.objects.all()
	serializer_class = AddingCompanySerializer
	permission_classes = [IsAuthenticated]

	def create(self, request):
		user = request.user
		if user.role != 'Company':
			raise serializers.ValidationError({'Error': 'You are freelancer, you cannot add company!'})

		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		data = serializer.save(request.data, user).data


		return Response(data)


# --------------------------------------------------------------------------------------------


