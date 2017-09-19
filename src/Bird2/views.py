from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        html_var = "hello !"
        context = {
            "html_var": html_var,
        }
        return context
