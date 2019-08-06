from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
    body = models.TextField(null=False)
    publication_date = models.DateField(auto_now_add=True)
    #likes = models.PositiveIntegerField(default=0)
    #dislikes = models.PositiveIntegerField(default=0)
    #users_reaction = models.ManyToManyField(get_user_model(), blank=True, related_name='user_like')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
