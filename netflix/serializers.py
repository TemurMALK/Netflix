from rest_framework.exceptions import *
from .models import *
from rest_framework.serializers import ModelSerializer


class AktyorSerializer(ModelSerializer):
    class Meta:
        model = Aktyor
        fields = '__all__'

    def validate_jins(self, jins):
        if jins.lower() != 'erkak' and jins.lower() != 'ayol':
            raise ValidationError("Jins kiritishda xatolik bor!")
        return jins


class KinoSerializer(ModelSerializer):
    aktyorlar = AktyorSerializer(many=True)

    class Meta:
        model = Kino
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
