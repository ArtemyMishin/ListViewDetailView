from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, InvalidPage
from page.models import Category, Good
from django.http import HttpResponse, Http404

class GoodListView(ListView):
    template_name = "index.html"
    paginate_by = 2
    cat = None

    def get(self, request, *args, **kwargs):
        if self.kwargs["cat_id"] == None:
            self.cat = Category.objects.first()
        else:
            self.cat = Category.objects.get(pk = self.kwargs["cat_id"])
        return super(GoodListView,self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodListView,self).get_context_data(**kwargs)
        context["cats"] = Category.objects.order_by("name")
        context["category"] = self.cat
        return context

    def get_queryset(self):
        return Good.objects.filter(category = self.cat).order_by("name")

class GoodDetailView(DetailView):
    template_name = "good.html"
    model = Good
    pk_url_kwarg = "good_id"

    def get_context_data(self, **kwargs):
        context = super(GoodDetailView,self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        context["cats"] = Category.objects.order_by("name")
        return context