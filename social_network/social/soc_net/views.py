from django.views.generic import View
from .models import Post
from rest_framework import generics
from rest_framework.response import Response
from .serializers import SocCreateSerializers, SocListSerializers, SocDetailSerializers


class SocListView(generics.ListAPIView):
    serializer_class = SocListSerializers
    queryset = Post.objects.all()


class SocDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = SocDetailSerializers
    queryset = Post.objects.all()

    def put(self, request, *args, **kwargs):
       return self.update(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     post_id = self.request.GET.get('post_id')
    #     post = Post.objects.get(id=post_id)
    #     like = self.request.GET.get('like')
    #     dislike = self.request.GET.get('dislike')
    #     if like and (request.user not in post.users_reaction.all()):
    #         post.likes += 1
    #         post.users_reaction.add(request.user)
    #         post.save()
    #     if dislike and (request.user not in post.users_reaction.all()):
    #         post.dislikes += 1
    #         post.users_reaction.add(request.user)
    #         post.save()
    #     data = {
    #         'likes': post.likes,
    #         'dislikes': post.dislikes
    #     }
    #     return Response(data)


class SocCreateView(generics.CreateAPIView):
    serializer_class = SocCreateSerializers


# class UserReactionView(View):
#     template_name = 'home.html'
#
#     def get(self, request, *args, **kwargs):
#         post_id = self.request.GET.get('post_id')
#         post = Post.objects.get(id=post_id)
#         like = self.request.GET.get('like')
#         dislike = self.request.GET.get('dislike')
#         if like and (request.user not in post.users_reaction.all()):
#             post.likes += 1
#             post.users_reaction.add(request.user)
#             post.save()
#         if dislike and (request.user not in post.users_reaction.all()):
#             post.dislikes += 1
#             post.users_reaction.add(request.user)
#             post.save()
#         data = {
#             'likes': post.likes,
#             'dislikes': post.dislikes
#         }
#         return JsonResponse(data)

# class SocListView(ListView):
#     model = Post
#     template_name = 'home.html'
#
#
# class SocDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#
#
# class SocCreateView(CreateView):
#     model = Posts
#     template_name = 'post_new.html'
#     fields = ['title', 'author', 'body']
#
#
# class UserReactionView(View):
#     template_name = 'home.html'
#
#     def get(self, request, *args, **kwargs):
#         post_id = self.request.GET.get('post_id')
#         post = Post.objects.get(id=post_id)
#         like = self.request.GET.get('like')
#         dislike = self.request.GET.get('dislike')
#         if like and (request.user not in post.users_reaction.all()):
#             post.likes += 1
#             post.users_reaction.add(request.user)
#             post.save()
#         if dislike and (request.user not in post.users_reaction.all()):
#             post.dislikes += 1
#             post.users_reaction.add(request.user)
#             post.save()
#         data = {
#             'likes': post.likes,
#             'dislikes': post.dislikes
#         }
#         return JsonResponse(data)
