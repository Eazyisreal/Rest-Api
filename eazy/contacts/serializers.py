from rest_framework import serializers
from models import contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'id': {'read_only': True},
        }