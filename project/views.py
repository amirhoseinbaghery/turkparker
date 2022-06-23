from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from project.forms import CommentForm
from project.models import Project, ProjectComment, ProjectCategory, ProjectTag


def single_project(request, slug):
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
    return render(request, 'project.html', context)


class ProjectList(ListView):
    template_name = 'projectlist.html'

    def get_queryset(self):
        global project_
        project_ = Project.objects.filter(status='p')
        return project_


class ProjectCategoryList(ListView):
    template_name = 'projectlist.html'
    paginate_by = 15

    def get_queryset(self):
        global proj
        slug = self.kwargs.get('slug')
        proj = get_object_or_404(ProjectCategory, status='p', slug=slug)
        return proj.ProjectCategory.filter(status='p')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = proj
        return context


class ProjectTagList(ListView):
    template_name = 'projectlist.html'
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


class SearchProject(ListView):
    model = Project
    template_name = "projectlist.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Project.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(keyword__icontains=query) | Q(
                body__icontains=query)
        )
        return object_list
