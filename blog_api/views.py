from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response



# endpoints

class PostUserWritePermission(BasePermission):
    message = "Only Author can edit post."
    #https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
    def has_object_permission(self, request, view, obj):
        # if get options head
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user 

# recreating using ModelViewSet
# another level of abstraction
# ModelViewSet inherits from the generic API view
# 
class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    
    # overring GET object
    def get_object(self, queryset=None, **kwargs):
        # capturing the item typed in with kwargs
        item = self.kwargs.get('pk')
        # creating new endpoint 
        return get_object_or_404(Post, slug=item )


    # defining a custom queryset
    def get_queryset(self):
        return Post.objects.all()



# recreating using viewsets

# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         # getting an object from the db
#         post = get_object_or_404(self.queryset, pk=pk)
#         # run it through the serializer
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)



    
# # https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     # returns all the posts flagged as published 
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer

    

# # Used for read-write-delete endpoitns to represent a single model instance
# # Provides get, put, patch, and delete method handlers 
# # https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview
# class PostDetail(generics.RetrieveUpdateAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
  
