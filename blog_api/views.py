from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissoin import BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly


class PostUserWritePermission(BasePermission):
    message = "Only Author can edit post."
    #https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
    def has_object_permission(self, request, view, obj):
        # if get options head
        if request.method in SAFE_METHODS:
            return True


    

class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # returns all the posts flagged as published 
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pass  
