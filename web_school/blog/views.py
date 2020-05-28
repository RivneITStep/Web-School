from django.shortcuts import render
from .models import Blog, Blog_Img
from django.core.paginator import Paginator


def blog(request):
    blog_list = Blog.objects.filter(moderated=True).order_by('-pub_date')
    paginator = Paginator(blog_list, 3)
    page = request.GET.get("page")
    paged_blog = paginator.get_page(page)
    blog_img = Blog_Img.objects.all()
    context = {
        'blog_list':paged_blog,
        'imges':blog_img
    }
    return render(request, 'pages/blog.html',context)


def single_blog(request,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog_img = Blog_Img.objects.get(blog_id=blog_id)
    blog.views = blog.views + 1
    blog.save()
    return render(request, 'pages/one_news.html',context={'blog':blog,'img':blog_img})