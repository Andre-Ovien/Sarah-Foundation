from django.shortcuts import render
from rest_framework.response  import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.

class BlogListCreateApi(generics.ListCreateAPIView):
    queryset = Blog.objects.order_by('-publish_date')
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        self.permission_classes =  [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes= [IsAdminUser]
        return super().get_permissions()
    

class BlogDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'

    
    def get_permissions(self):
        self.permission_classes =  [AllowAny]
        if self.request.method in ['PUT','PATCH','DELETE']:
            self.permission_classes= [IsAdminUser]
        return super().get_permissions()