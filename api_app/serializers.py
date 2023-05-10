from rest_framework import serializers
from blog.models import Post

#this serializer model is to convert all the fields in our model to JASON format

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        # fields = ["title", "content", "author", "date_posted"]
        fields = "__all__"