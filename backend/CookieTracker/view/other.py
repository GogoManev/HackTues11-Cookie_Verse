from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from ..models import Post, Comment
from django.http import Http404

User = get_user_model()

def articles(request):
    return render(request, 'Articles.html')

def exercises(request):
    return render(request, 'exercises.html')

def debloat(request):
    return render(request, 'debloat.html')

@login_required(login_url='/login/')
def newpost(request):
    if request.method == 'POST':
        title = request.POST.get('post_title')
        if not title:
            raise Http404('Invalid title')
        post_body = request.POST.get('post_body')
        if not post_body:
            raise Http404('invaid post body')
        new_post = Post.objects.create(
                                        title=title, poster=request.user, text=post_body)
        return redirect('/viewpost/' + (str)(new_post.id))

    return render(request, 'newpost.html')

def viewpost(request, post_id):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        comment = Comment.objects.create(
                                        text=comment_text,poster=request.user,post=Post.objects.get(id=post_id))

    try:
        post = Post.objects.get(id=post_id)
        context = {
            'poster': post.poster,
            'title': post.title,
            'text': post.text,
            'comments': Comment.objects.filter(post_id = post.id),
        }
        print(Comment.objects.filter(post_id = post.id)) 
        return render(request, 'viewpost.html', context)
    except Exception as e:
        return render(request, 'viewpost.html', {'error': str(e)})
