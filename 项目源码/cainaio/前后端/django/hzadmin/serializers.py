from django.contrib.auth.models import Userfrom rest_framework import serializersfrom .models import *class UserSerializer(serializers.ModelSerializer):	class Meta:		model = User		# fields 除password外的所有字段		fields = ('id', 'username', 'first_name', 'last_name', 'email','date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_active')class LoginSerializer(serializers.Serializer):	username = serializers.CharField()	password = serializers.CharField()