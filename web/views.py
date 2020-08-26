from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, User
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .serializers import GetAllPostSerializer
from .forms import PostForm, SendEmail


def create_post(request):
    post = PostForm()
    return render(request, 'web/create_posts.html', {'p': post})


def new_post(request):
    if request.method == "POST":
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
            context = {'new_post': post}
            return render(request, 'web/new_posts.html', context)
        else:
            return HttpResponse('Khong dung validate')
    else:
        return HttpResponse('Khong phai method POST')


def email_view(request):
    m = SendEmail()
    return render(request, 'web/email2.html', {'f': m})


def delete_post(request, pk=None):
    object = Post.objects.get(id=pk)
    object.delete()
    return HttpResponse('da xoa bai dang')


def edit_post(request, pk=None):
    object = Post.objects.get(id=pk)
    if request.method == "GET":
        post = PostForm(request.GET, instance=object)
        if post.is_valid():
            post.save()
            object.delete()
            return redirect('/list_post')
        else:
            return HttpResponse('Khong dung validate')
    else:
        post = PostForm(instance=object)
        return render(request, 'web/create_posts.html', {'p': post})

@csrf_exempt
def savepost(request):
    id=request.POST.get('id','')
    value = request.POST.get('value','')
    type = request.POST.get('type','')
    post=Post.objects.get(id=id)
    if type=="title":
        post.title=value

    if type=="category":
        post.category=value

    if type=="content":
        post.content=value

    if type=="create_by":
        post.create_by=value

    if type=="create_at":
        post.create_at=value

    if type=="update_by":
        post.update_by=value

    if type=="update_at":
        post.update_at=value

    post.save()
    return JsonResponse({"success":"updated"})


    # id=request.POST.get('id','')
    # type=request.POST.get('type','')
    # value=request.POST.get('value','')
    # post=Post.objects.get(id=id)
    # if type=="name":
    #     post.title=value
    #
    # if type=="category":
    #     post.category=value
    #
    # if type=="content":
    #     post.content=value
    #
    # if type=="create_by":
    #     post.create_by=value
    #
    # if type=="create_at":
    #     post.create_at=value
    #
    # if type=="update_by":
    #     post.update_by=value
    #
    # if type=="update_at":
    #     post.update_at=value
    #
    # post.save()
    # return JsonResponse({"success":"Updated"})

# def edit_post(request, pk = None):
#     if request.method == "POST":
#         if request.POST['title'] and request.POST['content']:
#             post = Post(pk=pk)
#             post.title = request.POST['title']
#             post.category = request.POST['category']
#             post.content = request.POST['content']
#             post.create_by = request.POST['create_by']
#             post.create_at = request.POST['create_at']
#             post.update_by = request.POST['update_by']
#             post.update_at = request.POST['update_at']
#             post.save(pk=pk)
#             return render(request, 'web/detail_post.html', {'post':post})
#
#         else:
#             return HttpResponse('All fields are required')

# else:
#     return render(request, 'that is not post method')

# class DeleteView(SuccessMessageMixin, DeleteView):
#     model = Post
#     success_url = '/'
#     success_message = "delete..."
#
#     def delete(self, request, *args, **kwargs):
#         post = Post.objects.get()
#         # self.object = self.get_object()
#         # name = self.object.name
#         # request.session['name'] = name
#         # message = request.session['name'] + 'deleted successfully'
#         return super(DeleteView, self).delete(request, *args, **kwargs)

# def save_email(request):
#     if request.method=="POST":
#         m = SendEmail(request.POST)
#         if m.is_valid():
#             tieude = m.cleaned_data['title']
#             cc = m.cleaned_data['title']
#             email = m.cleaned_data['title']
#             noidung = m.cleaned_data['title']
#             context = {'td':tieude, 'c':cc, 'e':email, 'n':noidung}
#             return render(request, 'web/print_email2.html', context)
#         else:
#             return HttpResponse('khong dung validate')
#     else:
#         return HttpResponse('khong phai method POST')

def save_email(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            context = {'email_data': m}
            return render(request, 'web/print_email2.html', context)


def save_newpost(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('luu Oke')
        else:
            return HttpResponse('khong duoc validate')
    else:
        return HttpResponse('khong phai post request')


def list_post(request):
    posts = Post.objects.all()
    return render(request, 'web/list_post.html', {'lists': posts})


class GetAllPostAPIView(APIView):

    def get(self, request):
        list_post = Post.objects.all()
        mydata = GetAllPostSerializer(list_post, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

    # Đoạn anh Đồng viết
    def post(self, request, format=None):
        serializer = GetAllPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response('delete successful', status=status.HTTP_204_NO_CONTENT)

    # def put(self, request, pk, format=None):
    #     post = Post.objects.get(pk=pk)
    #     serializer = GetAllPostSerializer(post, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GetAllPostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
