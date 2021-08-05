from django.views import View
from django.http import Http404
from django.http import JsonResponse

from .models import Redirect

class RedirectView(View):
    def get(self, request):

        key = request.GET.get("key", None)

        if key:
            try:
                return JsonResponse(Redirect.objects.get_redirect(key))
            except Redirect.DoesNotExist:
                pass
        raise Http404()
