from django.shortcuts import render
from rest_framework import generics, status
from .models import BlogPost
from .serializer import BlogPostSerializer
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serialize_class = BlogPostSerializer
    

