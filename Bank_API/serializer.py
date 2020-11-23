from rest_framework import serializers
from .models import Branches,Banks

class BankBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        # exclude = ['id']
        fields = '__all__'

class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = '__all__'