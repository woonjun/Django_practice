from django.shortcuts import get_object_or_404, render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # 모든 Post 객체를 가져옵니다.
    return render(request, 'ex01/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # pk(Primary Key)를 사용하여 Post 객체를 가져옵니다.
    return render(request, 'ex01/post_detail.html', {'post': post})