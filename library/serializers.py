from rest_framework import  serializers
from .models import User, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    # comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id','title', 'content', 'author', 'published_date')

