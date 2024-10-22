from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView

from djangoProject.bean import R
from hzadmin.serializers import LoginSerializer, UserSerializer


class Login(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = auth.authenticate(username=username,password=password)
        if user_obj==None:
            return R.fail('用户名或密码错误')
        auth.login(request,user_obj)
        print(user_obj.username)
        return R.ok(user_obj.username)

class Register(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.create_user(username=username, password=password)
        except Exception as e:
            if e.args[0] == 1062:
                return R.fail('注册失败,用户已存在')
            else:
                return R.fail('注册失败',e.args)
        return R.ok('注册成功')

class Logout(GenericAPIView):

    def get(self, request):
        auth.logout(request)
        return R.ok()

class UserInfo(GenericAPIView):

    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return R.ok(data=self.get_serializer(user).data)
        else:
            return R.fail('用户未登录')

    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user = request.user
        if user == None:
            return R.fail('用户不存在')
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return R.ok(data=self.get_serializer(request.user).data)

