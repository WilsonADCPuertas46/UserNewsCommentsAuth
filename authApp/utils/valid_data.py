from django.conf import settings

from rest_framework_simplejwt.backends import TokenBackend

def get_valid_token_data(request):
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = tokenBackend.decode(token, verify=False)
    return valid_data