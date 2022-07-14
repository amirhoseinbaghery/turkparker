from django.shortcuts import render, redirect

from blog.models import Blog
from content.forms import ContactUsForm
from content.models import About, ContactUs, Communication, Slider, First
from costumer.models import Costumer
from product.models import ProductCategory, Product
from project.models import Project


def about(request):
    about_ = About.objects.first()
    communicate = Communication.objects.all().first()
    costumer_ = Costumer.objects.count()
    project_ = Project.objects.count()
    context = {
        'object': about_,
        'com': communicate,
        'costumer': costumer_,
        'project': project_,
    }
    return render(request, 'about.html', context)


def contactus(request):
    communicate = Communication.objects.all().first()
    about_ = About.objects.all().first()

    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST or None)
        if contact_form.is_valid():
            name = contact_form.cleaned_data.get('name')
            email = contact_form.cleaned_data.get('email')
            subject = contact_form.cleaned_data.get('subject')
            message = contact_form.cleaned_data.get('message')
            phone = contact_form.cleaned_data.get('phone')
            ContactUs.objects.create(name=name, email=email, subject=subject, message=message, phone=phone,
                                     is_read=False)
            return redirect('content:contactus')
    else:
        contact_form = ContactUsForm()
    context = {
        'contact_form': contact_form,
        'com': communicate,
        'object': about_,
    }
    return render(request, 'contact us.html', context)


def home(request):
    context = {
        'slide': Slider.objects.all(),
        'category': ProductCategory.objects.filter(status='p'),
        'project': Project.objects.filter(status='p'),
        'product': Product.objects.filter(status='p'),
        'blog': Blog.objects.filter(status='p'),
        'first': First.objects.first(),
        'costumer': Costumer.objects.all(),
        'about': About.objects.all().first(),
    }
    return render(request, 'index.html', context)
