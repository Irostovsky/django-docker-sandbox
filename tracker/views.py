from django.http import HttpResponse
from django.views.generic import DetailView

# class IndexView(DetailView):
#     def get(self):
#         return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")