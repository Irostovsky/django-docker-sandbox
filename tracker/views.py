from django.http import HttpResponse
from django.views.generic import DetailView

from tracker.models import Ping


class IndexView(DetailView):
    def get(self, request, *args, **kwargs):
        Ping.objects.create()
        total = Ping.objects.count()
        return HttpResponse(f"Hello, world. You're at the tracker index. {total}")
