from django.shortcuts import render
from django.views.generic import TemplateView
from webScrapa.forms import HomeForm
from django.views import generic
from webScrapa.models import RamParts, MotherboardParts, GpuParts
from .filters import RamFilter, GpuFilter, MotherboardFilter
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):

        form = HomeForm()

        return render(request,'homepage.html',{'form':form})

class ramlistView(generic.ListView):
    model = RamParts
    template_name = 'ram_search.html'
    context_object_name = 'ramParts_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RamFilter(self.request.GET, queryset=self.get_queryset())
        return context


class gpulistView(generic.ListView):
    model = GpuParts
    template_name = 'gpu_search.html'
    context_object_name = 'gpuParts_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = GpuFilter(self.request.GET, queryset=self.get_queryset())
        return context

class motherboardlistView(generic.ListView):
    model = MotherboardParts
    template_name = 'motherboard_search.html'
    context_object_name = 'motherboardParts_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RamFilter(self.request.GET, queryset=self.get_queryset())
        return context
