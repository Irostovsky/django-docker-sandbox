from django.http import HttpResponse
from django.views.generic import DetailView

class IndexView(DetailView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the tracker index.")
