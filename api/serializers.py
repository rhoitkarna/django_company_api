from rest_framework import serializers
from api.models import Company


# Create Serializers Here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

