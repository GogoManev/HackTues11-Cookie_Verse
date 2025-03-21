from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from ..models import Post, Comment, Forum
from django.http import Http404

def forum(request):
    context = {
        'forums': Forum.objects.all()
    }
    return render(request, 'forums.html', context)

def viewforum(request, id):
    forum = Forum.objects.get(id=id)
    posts = Post.objects.filter(forum=forum)
    context = {
        'forum': forum,
        'posts': posts
    }
    return render(request, 'forum/viewforum.html', context)

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