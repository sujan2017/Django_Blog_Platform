from rest_framework import serializers
from .models import Post,Category, Comment
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields= ['id', 'name', 'slug']

class PostSerializer(serializers.ModelSerializer):
    category= CategorySerializer(read_only=True)
    author= serializers.ReadOnlyField(source='author.username')

    class Meta:
        model= Post
        fields= '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user= serializers.ReadOnlyField(source='user.username') #show username

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True)

    class Meta:
        model= User
        fields= ['username', 'email', 'password']

    def create(self, validated_data):
        user= User.objects.create_user(
            username= validated_data['username'],
            email=validated_data.get['email'],
            password= validated_data['password']

        )
        return user
