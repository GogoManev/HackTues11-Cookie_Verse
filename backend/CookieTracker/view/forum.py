from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from ..models import Post, Comment, Forum
from django.http import Http404

def forum(request):
    forums = Forum.objects.all()
    
    context = {
        'forums': []
    }

    for f in forums:
        forum_data = {
            'forum': f,
            'posts': Post.objects.filter(forum=f)
        }
        context['forums'].append(forum_data)
    print(context)
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
        forum = Forum.objects.get(name = request.POST.get('forum')) 
        
        new_post = Post.objects.create(
                                        title=title, poster=request.user, text=post_body, forum=forum)
        return redirect('/viewpost/' + (str)(new_post.id))

    forums = Forum.objects.all()
    return render(request, 'newpost.html', { 'forums': forums })

def viewpost(request, post_id):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        comment = Comment.objects.create(
                                        text=comment_text,poster=request.user,post=Post.objects.get(id=post_id))

    try:
        post = Post.objects.get(id=post_id)
        context = {
            'post': post,
            'comments': Comment.objects.filter(post_id = post.id),
        }
        return render(request, 'viewpost.html', context)
    except Exception as e:
        return render(request, 'viewpost.html', {'error': str(e)})

@login_required(login_url='/login/')
def likepost(request, id):
    #MOVE POStoWEte DA BYDAT LIKNATI NQKOLKO PYTI
    post = Post.objects.get(id=id)
    post.likes = post.likes + 1
    post.save()
    return redirect('/viewpost/' + (str)(id))