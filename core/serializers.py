from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import CasierJudiciaire, HistoriqueModification


class CasierJudiciaireSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CasierJudiciaire
        fields = ["id", "user", "infractions", "statut", "created_at", "updated_at"]

class HistoriqueModificationSerializer(serializers.ModelSerializer):
    modified_by = UserSerializer(read_only=True)

    class Meta:
        model = HistoriqueModification
        fields = ["id", "casier", "modified_by", "modifications", "modified_at"]
