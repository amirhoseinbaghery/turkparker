from django.views.generic import ListView

from catalog.models import Catalog


class CatalogList(ListView):
    template_name = 'cataloglist.html'
    paginate_by = 15

    def get_queryset(self):
        global catalog
        catalog = Catalog.objects.all()
        return catalog
