from rest_framework  import serializers
from rest_framework.serializers import ValidationError
from .models import Blog, Comment, Likes


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id',
            'author',
            'title',
            'image',
            'content',
            'publish_date',
            'update_date',
        )