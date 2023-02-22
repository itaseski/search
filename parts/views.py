from django.views.generic import TemplateView, ListView

from .models import Part
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Part
    context_object_name = 'parts'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Part.objects.filter(Q(part_number__icontains=query) | Q(part_number__icontains=query))

