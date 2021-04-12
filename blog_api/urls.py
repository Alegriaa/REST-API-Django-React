from .views import PostList
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'
# utilizing router from the django rest framework
router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls





# urlpatterns = [
#     # primary key
#     path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
#     path('', PostList.as_view(), name='listcreate'),
# ] 