from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from account.models import User
from blog.forms import CommentForm
from blog.models import Blog
from blog.models import BlogCategory, BlogTag, BlogComment


def SinglePost(request, slug):
    post = get_object_or_404(Blog, status='p', slug=slug)
    comments = BlogComment.objects.filter(post=post, reply=None, status="p")
    ip_address = request.user.ip_address
    if ip_address not in post.ip.all():
        post.ip.add(ip_address)
    post.save()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid:
            content = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = BlogComment.objects.get(id=reply_id)
            comment = BlogComment.objects.create(post=post, user=request.user, body=content, reply=comment_qs)
            comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'comments': comments,
        'object': post,
        'related': post.get_related_posts_by_tags()[:3],
        'comment_form': comment_form,
    }
    return render(request, 'singleBlog.html', context)


class PostList(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        global blog, category, tag
        blog = Blog.objects.filter(status='p')
        category = BlogCategory.objects.filter(status='p')
        tag = BlogTag.objects.all()
        return blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        context['first'] = blog.first()
        context['blog'] = blog[1:]
        context['tag'] = tag
        return context


class categoryList(ListView):
    template_name = 'list.html'
    paginate_by = 15

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(BlogCategory, status='p', slug=slug)
        return category.Category.filter(status='p')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = category
        return context


class tagList(ListView):
    template_name = 'list.html'
    paginate_by = 15

    def get_queryset(self):
        global tag, product
        slug = self.kwargs.get('slug')
        tag = get_object_or_404(BlogTag, slug=slug)
        return tag.tag.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = tag
        return context


class Author(ListView):
    template_name = 'author.html'
    paginate_by = 15

    def get_queryset(self):
        global author
        slug = self.kwargs.get('username')
        author = get_object_or_404(User, username=slug)
        return author.author.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = author
        return context


class SearchBlog(ListView):
    model = Blog
    template_name = "list.html"
    paginate_by = 15

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Blog.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(keyword__icontains=query) | Q(
                body__icontains=query)
        )
        return object_list
