from django.shortcuts import render
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view   #


# Create we create a view for the api

@api_view(["GET"])      #this tell the the view to work with get request
def api_home_page(request):
    all_posts = Post.objects.all()
    new_serialized_data = PostSerializer(all_posts, many=True)  #many=True must be present therem
    
    return Response(new_serialized_data.data)


@api_view(["GET"])
def api_detail_page(request, id):   
    single_post = Post.objects.get(id=id)   # for geting a single object from the model
    serialized_post = PostSerializer(single_post)
    return Response(serialized_post.data)


@api_view(["PUT"])  #  <-- WE USE "put" FOR UPDATING
def api_update_page(request, id):
    single_post = Post.objects.get(id=id)  #<-- geting the object to be updated
    new_data = request.data #<--- store the new value of the updated object
    serialized_new_data = PostSerializer(single_post, data=new_data, partial=True)
    if serialized_new_data.is_valid():# Validate the data
        serialized_new_data.save() # then save the update object
        return Response(serialized_new_data.data)
    
    else:
        return Response({"Error": "You typed rubbish!!"})


@api_view(["DELETE"])  #<-- use for deleting an object
def api_delete_page(request, id):
    single_post = Post.objects.get(id=id)
    single_post.delete()
    return Response({"Success": "Object deleted successfuly"})

@api_view(["POST"]) #,--- for creating an object
def api_create_page(request):
    new_data = PostSerializer(data=request.data)
    if new_data.is_valid():
        new_data.save()
        return Response(new_data.data)
    


