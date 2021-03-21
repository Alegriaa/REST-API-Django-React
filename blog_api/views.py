from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    # returns all the posts flagged as published 
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pass  
