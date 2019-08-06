from rest_framework import serializers
from .models import Post


class SocCreateSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['title', 'author', 'body']


class SocListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'publication_date']


class SocDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
