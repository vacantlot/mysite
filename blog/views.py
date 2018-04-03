from django.shortcuts import render
from blog.models import BlogPost


# Create your views here.

def blog_index(request):
    blog_list = BlogPost.objects.all()  # 获取所有数据
    return render(request, 'index.html', {'blog_list': blog_list})  # 返回index.html页面
"""
blog_list = BlogPost.objects.all() ：获取数据库里面所拥有BlogPost对象

render返回一个页面(index.html)，顺带把数据库中查询出来的所有博客内容（blog_list）也一并返回。
"""
