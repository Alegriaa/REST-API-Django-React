from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly


# endpoints

class PostUserWritePermission(BasePermission):
    message = "Only Author can edit post."
    #https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
    def has_object_permission(self, request, view, obj):
        # if get options head
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user 


    
# https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # returns all the posts flagged as published 
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    

# Used for read-write-delete endpoitns to represent a single model instance
# Provides get, put, patch, and delete method handlers 
# https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview
class PostDetail(generics.RetrieveUpdateAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
  
