from django.urls import path
from blog import views
from blog.views import PostListView,PostCreateView

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('blog/',PostListView.as_view(),name='blogpost'),
    path('createpost/',PostCreateView.as_view(),name='blogpostcreate'),
    path('readme/',views.read,name='read')
]
