from rest_framework import serializers
from app1.models import autorModel



class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = autorModel
        fields = ('id', 'nombre_proyecto', 'nombre_empresa','descripcion','tipo_licencia','categoria')


        


