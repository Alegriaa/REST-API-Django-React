# allows data to be converted into python data types
# to render into JSON 

from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')