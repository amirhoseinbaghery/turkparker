from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from product.models import Product, ProductComment, ProductTag, ProductCategory


def product(request, slug):
    product_ = get_object_or_404(Product, status='p', slug=slug)
    comments = ProductComment.objects.filter(product=product_, reply=None, status="p")
    ip_address = request.user.ip_address
    if ip_address not in product_.ip.all():
        product_.ip.add(ip_address)
    product_.save()

    context = {
        'object': product_,
        'related': product_.get_related_posts_by_tags()[:3],
    }
    return render(request, 'product.html', context)


class ProductList(ListView):
    template_name = 'productlist.html'
    paginate_by = 15

    def get_queryset(self):
        global product_
        product_ = Product.objects.filter(status='p')
        return product_


class ProductCategoryList(ListView):
    template_name = 'productlist.html'
    paginate_by = 15

    def get_queryset(self):
        global prod
        slug = self.kwargs.get('slug')
        prod = get_object_or_404(ProductCategory, status='p', slug=slug)
        return prod.ProductCategory.filter(status='p')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = prod
        return context


class ProductTagList(ListView):
    template_name = 'productlist.html'
    paginate_by = 15

    def get_queryset(self):
        global tag, product
        slug = self.kwargs.get('slug')
        tag = get_object_or_404(ProductTag, slug=slug)
        return tag.tag.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = tag
        return context


class SearchProduct(ListView):
    model = Product
    template_name = "productlist.html"
    paginate_by = 15


    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(keyword__icontains=query) | Q(
                body__icontains=query)
        )
        return object_list
