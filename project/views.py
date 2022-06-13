from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from account.models import User
from project.models import Project, ProjectComment, ProjectCategory, ProjectTag
from project.forms import CommentForm


def SinglePost(request, slug):
    project = get_object_or_404(Project, status='p', slug=slug)
    comments = ProjectComment.objects.filter(project=project, reply=None, status="p")
    ip_address = request.user.ip_address
    if ip_address not in project.ip.all():
        project.ip.add(ip_address)
    project.save()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid:
            content = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = ProjectComment.objects.get(id=reply_id)
            comment = ProjectComment.objects.create(project=project, user=request.user, body=content, reply=comment_qs)
            comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'comments': comments,
        'object': project,
        'related': project.get_related_posts_by_tags()[:3],
        'comment_form': comment_form,
    }
    return render(request, 'singleBlog.html', context)


class PostList(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        global project_
        project_ = Project.objects.filter(status='p')
        return project_

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newest'] = project_[:1]
        context['new'] = project_[1:4]
        context['similar'] = project_.filter(category__slug='استراتژی-ولوم-تریدینگ')
        context['filter'] = project_.filter(category__slug='فیلتر-نویسی')
        return context


class categoryList(ListView):
    template_name = 'list.html'
    paginate_by = 15

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(ProjectCategory, slug=slug)
        return category.ProjectCategory.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = category
        return context


class tagList(ListView):
    template_name = 'list.html'
    paginate_by = 15

    def get_queryset(self):
        global tag
        slug = self.kwargs.get('slug')
        tag = get_object_or_404(ProjectTag, slug=slug)
        return tag.ProjectTag.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = tag
        return context

