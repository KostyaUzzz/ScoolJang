from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from MyServ.models import Product


def show(request):
    return HttpResponse('Hello Django')


class TitleContextMixin:

    def get_title(self):
        return getattr(self, 'title', '')

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()

        )
        return context


class Products(TitleContextMixin, ListView):
    title = 'Продукты'
    template_name = 'MyServ/index.html'
    model = Product
