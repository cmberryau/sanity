from django.views.generic.base import View
from django.http.response import HttpResponse


class MostBasicView(View):
    def get(self, request, extra_context=None):
        return HttpResponse("hello get")

    def post(self, request, extra_context=None):
        return HttpResponse("hello post")
