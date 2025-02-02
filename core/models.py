from django.db import models
from accounts.models import User
# Create your models here.

# Modèle du Casier Judiciaire
class CasierJudiciaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    infractions = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    statut = models.CharField(
        max_length=20, choices=[("clean", "Aucune infraction"), ("condamned", "Condamné")], default="clean"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Casier de {self.user.username}"

# Modèle pour garder un historique des modifications
class HistoriqueModification(models.Model):
    casier = models.ForeignKey(CasierJudiciaire, on_delete=models.CASCADE, related_name="modifications")
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    modifications = models.TextField()
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Modification sur {self.casier.user.username} par {self.modified_by}"
