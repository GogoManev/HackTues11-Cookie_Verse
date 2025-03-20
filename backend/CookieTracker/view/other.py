from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from ..models import Post
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
        new_guild = Post.objects.create(
                                        title=title, poster=request.user, text=post_body)
        
        #return redirect('/channels/guilds/' + (str)(new_guild.id) + '/' + (str)(new_channel.id))
    return render(request, 'newpost.html')

def viewpost(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        context = {
            'poster': post.poster,
            'title': post.title,
            'text': post.text,
        }
        return render(request, 'viewpost.html', context)
    except Exception as e:
        return render(request, 'viewpost.html', {'error': str(e)})
