from django.urls import path, include
from .views import SocListView, SocCreateView, SocDetailView#, UserReactionView


urlpatterns = [
    path('posts/', SocCreateView.as_view(), name='post_new'),
    path('all/', SocListView.as_view(), name='all_posts'),
    path('post/<int:pk>/', SocDetailView.as_view(), name='post_detail'),
    #path('user_reaction', UserReactionView.as_view(), name='user_reaction'),
    #path('likes/', SocDetailView.as_view(), name='post_detail'),
]
