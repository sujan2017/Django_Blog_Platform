from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Post, Category, Comment, User
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, RegisterSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

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


# create post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_create_api(request):
    serializer = PostSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update Post
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def post_update_api(request,slug):
    post=get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return Response({'error':'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
    serializer= PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Post
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def post_delete_api(request, slug):
    post= get_object_or_404(Post, slug=slug)
    if post.author !=request.user:
        return Response({'error':'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
    post.delete()
    return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)
    
#List Comments per post
@api_view(['GET'])
def comment_list_api(request, post_slug):
    post= get_object_or_404(Post, slug=post_slug)
    Comments= post.comments.all()   #related_name= commments
    Serializer= CommentSerializer(Comments, many= True)
    return Response(Serializer.data)

# Create Comment
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create_api(request, post_slug):
    post= get_object_or_404(Post, slug=post_slug)
    serializer= CommentSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, post= post)  #logged-in user
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#updatae comments
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def comment_update_api(request, comment_id):
    comment=get_object_or_404(Comment, id=comment_id)

    #ownership check
    if comment.user != request.user:
        return Response({'error':'you are not allowed to edit this comment.'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer= CommentSerializer(comment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# DElete comment
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete_api(request, comment_id):
    comment = get_object_or_404(Comment, id= comment_id)

    #ownership check
    if comment.user != request.user:
        return Response({'error':'ypu are not allowed to delete this comment.'}, status=status.HTTP_403_FORBIDDEN)
    
    comment.delete()
    return Response({'message':'comment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


# Signup api 
@api_view(['POST'])
def register_api(request):
    serializer= RegisterSerializer(data= request.data)
    if serializer.is_valid():
        user= serializer.save()
        Token.objects.create(user=user)
        return Response(
            {"message":"User registered successfully."},
            status= status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#login Api 

@api_view(['POST'])
def login_api(request):
    username= request.data.get('username')
    password= request.data.get('password')

    user= authenticate(username=username, password= password)

    if user is not None: 
        token, _=Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username

        })
    return Response(
        {"error": "invalid username or password"},
        status= status.HTTP_400_BAD_REQUEST
    )


#logout api 

@api_view(['POST'])
@permission_classes([IsAuthenticated])

def logout_api(request):
    request.user.auth_token.delete()
    return Response({"message": "Logged out successfully"})