from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class DiagnosisSummaryDental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    dental_image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=1000,)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"Diagnosis Summary Dental {self.date_created}"


class DiagnosisSummaryTeeth(models.Model):
    diagnosis_summary_dental = models.ForeignKey(
        DiagnosisSummaryDental, on_delete=models.CASCADE)
    teeth_name = models.CharField(max_length=255, default="")
    teeth_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Diagnosis Summary Teeth{self.teeth_name}"


class DiagnosisSummaryCaries(models.Model):
    diagnosis_summary_teeth = models.ForeignKey(
        DiagnosisSummaryTeeth, on_delete=models.CASCADE)
    caries_type = models.CharField(
        max_length=255, default="", blank=True, null=True)
    accuracy = models.DecimalField(
        default=None, blank=True, null=True, decimal_places=4, max_digits=7)
    x_pos = models.DecimalField(
        default=None, blank=True, null=True, decimal_places=4, max_digits=7)
    y_pos = models.DecimalField(
        default=None, blank=True, null=True, decimal_places=4, max_digits=7)

    def __str__(self):
        return f"Diagnosis Summary Caries {self.caries_type} {self.accuracy}"
