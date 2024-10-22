from rest_framework import serializers
from .models import *
    
    
class CainiaoBased_Serializer(serializers.ModelSerializer):
                           
    class Meta:
        model = CainiaoBased
        fields = "__all__"
            
class Designlist_Serializer(serializers.ModelSerializer):
                           
    class Meta:
        model = Designlist
        fields = "__all__"
            
class UserLike_Serializer(serializers.ModelSerializer):
                           
    class Meta:
        model = UserLike
        fields = "__all__"
            
class Word_Serializer(serializers.ModelSerializer):
                           
    class Meta:
        model = Word
        fields = "__all__"


class TitleCount_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TitleCount
        fields = "__all__"