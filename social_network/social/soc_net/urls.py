from django.urls import path
from .views import SocListView, SocCreateView, SocDetailView


urlpatterns = [
    path('posts/', SocCreateView.as_view(), name='post_new'),
    path('posts/all/', SocListView.as_view(), name='all_posts'),
    path('post/<int:pk>/', SocDetailView.as_view(), name='post_detail'),
]
