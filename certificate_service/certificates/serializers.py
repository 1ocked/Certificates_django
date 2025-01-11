from rest_framework import serializers
from .models import Certificate, Owner, Skill

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model = Certificate
        fields = '__all__'