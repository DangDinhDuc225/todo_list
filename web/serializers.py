from rest_framework import serializers
from web.models import Post


class GetAllPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'category',
                  'content',
                  'create_by',
                  'create_at',
                  'update_by',
                  'update_by')

