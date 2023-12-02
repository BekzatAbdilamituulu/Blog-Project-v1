from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from .models import Post, PostComment, Category, User
from django.views.generic.edit import FormMixin
from .forms import CommentForm, PostCreateForm, PostUpdateForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url='/login/')
def article_list_view(request):
    post = Post.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': post,
        'cats': cats,
    }
    return render(request, "article/index.html", context)

@login_required(login_url='/login/', redirect_field_name='next')
def post_detail(request, pk):
    template_name = 'article/detail.html'
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.all()
    comment_form=CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            text = comment_form.cleaned_data['text']
            new_comment = PostComment(post=post, text=text, author_id=request.user.id)
            new_comment.save()
            return redirect('detail', pk=post.id)
        else:
            comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'comment_form': comment_form})

def category_detail(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    post = Post.objects.filter(category__exact=cat)
    return render(request, 'article/category.html', {'cat':cat, 'post': post})

@login_required(login_url='/login/')
def add_post(request):
    form = PostCreateForm()
    if request.method=='POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            author = User.objects.get(username=request.user.username)
            obj.author = author
            obj.save()
            return redirect('home')
        else:
            print (form.errors)
            form = PostCreateForm()
    return render(request,'article/add_post.html',{'form':form})

@login_required(login_url='/login/')
def update_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    author = get_object_or_404(User, id=post.author.id)
    if author.id == request.user.id:
        form = PostUpdateForm(instance=post)
        if request.method=="POST":
            form = PostUpdateForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('/'+str(post.id)+'/')
            else:
                form = PostUpdateForm(instance=post)

        return render(request, 'article/update_post.html', {'form':form, 'post':post})
    else:
        return HttpResponseForbidden()

@login_required(login_url='/login/')
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    author = get_object_or_404(User, id=post.author.id)
    if author.id == request.user.id:
        if request.method == "POST":
            post.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseForbidden()


    
        
















class PostTemplateView(TemplateView):
    model = Post
    template_name = 'article/post.html'

class About(TemplateView):
    template_name = "article/about.html"

class Contact(TemplateView):
    template_name = "article/contact.html"



