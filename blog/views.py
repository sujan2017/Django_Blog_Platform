from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseForbidden
from .models import Post,Comment, Category
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def post_list(request):

    posts=Post.objects.all().order_by('-created_at')
    categories= Category.objects.all()

    category_slug= request.GET.get('category')   # take category form url

    

    if category_slug:       # if category is provided then apply filter
        posts=posts.filter(category__slug=category_slug)

    
    query = request.GET.get('q')
    if query:
        posts=posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)

        )

    


    # pagination 

    paginator=Paginator(posts, 5)   #per page 5 posts
    page_number=request.GET.get('page')
    posts = paginator.get_page(page_number)

    # to send in template 
    context={
        'posts': posts,
        'categories': categories,
        'query': query,
    }

    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post= get_object_or_404(Post, pk=pk)

    #if user submits a comment
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.user=request.user
            new_comment.save()

            return redirect('post_detail',pk=pk)
    else:
        form=CommentForm()
    comments=post.comments.all()

    return render(request, 'blog/post_detail.html',{
        'post': post,
        'form': form,
        'comments': comments
    })


def delete_comment(request, comment_id):
    comment=get_object_or_404(Comment, pk=comment_id)

    #Permission for comment owner of post author
    if request.user==comment.user or request.user==comment.post.author:
        post_pk=comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)
    else:
        return HttpResponse("You are not allowed to delete this comment.")
    
def edit_comment(request, pk):
    comment=get_object_or_404(Comment,pk=pk)

    #check if current user is comment author
    if request.user !=comment.user:
        return HttpResponseForbidden("You are not allowed to edit this comment.")
    if request.method=="POST":
        form=CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail',pk=comment.post.pk)
    else:
        form=CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form':form})


        





@login_required
def post_create(request):
    if request.method== 'POST':
        form= PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author =request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm()
    return render(request, 'blog/post_form.html', {'form':form})

def post_edit(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.user !=post.author:
        return HttpResponseForbidden("you are not allowed to edit this post.")
    
    if request.method=='POST':
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form':form})


def post_delete(request,pk):
    post=get_object_or_404(Post, pk=pk)

    if request.user !=post.author:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    
    post.delete()
    return redirect('post_list')