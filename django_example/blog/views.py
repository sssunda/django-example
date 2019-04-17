from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post


def index(request):
    post_list = Post.objects.all()

    # render() 쓰기 전
    # template = loader.get_template('blog/index.html')
    # context= {
    #     'post_list':post_list,
    # }
    # return HttpResponse(template.render(context,request))
    return render(request, 'blog/index.html', {'post_list':post_list})

def detail(request, post_id):
    # short_cut에 있는 404에러 잡기 전
    # try : 
    #     post  = Post.objects.get(pk=post_id)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exist")
    # return render(request, 'blog/detail.html', {'post':post})
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/detail.html', {'post':post})
