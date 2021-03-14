from .models import Corona
from rest_framework import serializers

class CoronaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Corona
        fields = [ 'id', 'uf', 'state', 'cases', 'deaths', 'suspects']