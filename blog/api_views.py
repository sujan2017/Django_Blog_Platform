from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from django.shortcuts import get_object_or_404

#all posts
@api_view(['GET'])
def post_list_api(request):
    posts=Post.objects.all().order_by('-created_at')
    serializer =PostSerializer(posts, many=True)
    return Response(serializer.data)


#single post
@api_view(['GET'])
def post_detail_api(request, slug):
    post= Post.objects.get(slug=slug)
    serializer= PostSerializer(post)
    return Response(serializer.data)

#Categories
@api_view(['GET'])
def category_list_api(request):
    categories= Category.objects.all()
    serializer= CategorySerializer(categories, many=True)
    return Response(serializer.data)

#post by category
@api_view(['GET'])
def post_by_category_api(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
