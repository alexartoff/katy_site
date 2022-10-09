from rest_framework.serializers import ModelSerializer

from numero.models import Celeb


class CelebsSerializer(ModelSerializer):
    class Meta:
        model = Celeb
        fields = ['name', 'birthday', 'persid']
