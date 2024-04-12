from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()  # 모든 Post 객체를 가져옵니다.
    return render(request, 'ex01/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # pk(Primary Key)를 사용하여 Post 객체를 가져옵니다.
    return render(request, 'ex01/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # 필요하다면 여기서 post의 다른 필드를 설정할 수 있습니다.
            # 예: post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'ex01/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'ex01/post_edit.html', {'form': form})
