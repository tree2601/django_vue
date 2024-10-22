from rest_framework.authentication import BaseAuthentication, SessionAuthentication

'''
自定义Session认证类
取消CSRF认证
'''

class HZAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user = getattr(request._request, 'user', None)
        if not user or not user.is_active:
            return None
        return (user, None)

