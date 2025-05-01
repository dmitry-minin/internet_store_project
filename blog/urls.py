from django.urls import path
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView


app_name = 'blog'

urlpatterns = [
    path('blog', BlogListView.as_view(), name='home',),
    path('blog/create', BlogCreateView.as_view(), name='create_post'),
    path('bog/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='update_post'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='delete_post'),
]
