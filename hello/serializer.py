
from rest_framework import serializers
from hello.models import Party

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        #fields = ('name', 'address')
        #fields = ['name', 'address','status','distance',
        #'entryFee','dateTime','guysAllowed']
        fields = ['name', 'address','distance']
