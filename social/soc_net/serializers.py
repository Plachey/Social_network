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
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'likes', 'dislikes', 'publication_date']

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author')
        likes = validated_data.get('likes')
        dislikes = validated_data.get('dislikes')

        if likes and (instance.author not in instance.users_reaction.all()):
            instance.likes += 1
            instance.users_reaction.add(instance.author)
            instance.save()
        if dislikes and (instance.author not in instance.users_reaction.all()):
            instance.dislikes += 1
            instance.users_reaction.add(instance.author)
            instance.save()
        return instance
