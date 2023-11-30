from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


#class CustomAuthentication (BaseAuthentication):
# def authentication(self,request):
#     username=request.GET.get('username')
#     if username is NONE:
#         return None

#     try:
#         email=User.objects.get(uname=username)
#     except User.DoesnotExist:
#         raise AuthenticationFailed('no such user')
#     return (user, None)