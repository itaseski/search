from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'home/home.html'


