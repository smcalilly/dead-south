from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Article


class Content(ListView):
    template_name = 'dead_south/content.html'
    model = Article
    ordering = ['-pk']

class Home(TemplateView):
    template_name = 'dead_south/home.html'

class About(TemplateView):
    template_name = 'dead_south/about.html'

class Help(TemplateView):
    template_name = 'dead_south/help.html'

def page_not_found(request, exception, template_name='dead_south/404.html'):
    return render(request, template_name, status=404)


def server_error(request, template_name='dead_south/500.html'):
    return render(request, template_name, status=500)
