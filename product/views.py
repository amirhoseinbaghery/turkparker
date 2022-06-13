from django.shortcuts import render, get_object_or_404

from product.forms import CommentForm
from product.models import Product, ProductComment


def product(request, slug):
    product_ = get_object_or_404(Product, status='p', slug=slug)
    comments = ProductComment.objects.filter(product=product_, reply=None, status="p")
    ip_address = request.user.ip_address
    if ip_address not in product_.ip.all():
        product_.ip.add(ip_address)
    product_.save()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid:
            content = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = ProductComment.objects.get(id=reply_id)
            comment = ProductComment.objects.create(product=product_, user=request.user, body=content, reply=comment_qs)
            comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'comments': comments,
        'object': product_,
        'related': product_.get_related_posts_by_tags()[:3],
        'comment_form': comment_form,
    }
    return render(request, 'product.html', context)
