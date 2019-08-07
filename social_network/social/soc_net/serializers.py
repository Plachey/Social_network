from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model


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

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.body = validated_data.get('body', instance.body)
    #     instance.likes = validated_data.get('likes', instance.likes)
    #     instance.dislikes = validated_data.get('dislikes', instance.dislikes)
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        instance.post_id = validated_data.get('id')
        print(instance.post_id)
        instance.title = validated_data.get('title')
        print(instance.title)
        instance.body = validated_data.get('body')
        instance.likes = validated_data.get('likes')
        instance.dislikes = validated_data.get('dislikes')
        # post = Post.objects.get(id=instance.post_id)
        if instance.likes and (get_user_model() not in instance.users_reaction.all()):
            instance.likes += 1
            instance.users_reaction.add(get_user_model())
            instance.save()
        if instance.dislikes and (get_user_model() not in instance.users_reaction.all()):
            instance.dislikes += 1
            instance.users_reaction.add(get_user_model())
            instance.save()
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.dislikes = validated_data.get('dislikes', instance.dislikes)
        instance.save()
        return instance
