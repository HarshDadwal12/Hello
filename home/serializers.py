from rest_framework import serializers
from home.models import Contact

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contact
        fields='__all__'
