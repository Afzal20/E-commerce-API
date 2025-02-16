from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views import View

@method_decorator(csrf_protect, name='dispatch')
class MyView(View):
    def post(self, request, *args, **kwargs):
        return JsonResponse({'message': 'CSRF token verified'})


def csrf_token_view(request):
    csrf_token = get_token(request)
    print(f"CSRF Token: {csrf_token}")  # Print the actual token
    return JsonResponse({'csrfToken': csrf_token})
