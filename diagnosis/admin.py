from django.contrib import admin
from diagnosis.models import DiagnosisSummaryDental, DiagnosisSummaryTeeth, DiagnosisSummaryCaries

admin.site.register(DiagnosisSummaryDental)
admin.site.register(DiagnosisSummaryTeeth)
admin.site.register(DiagnosisSummaryCaries)
