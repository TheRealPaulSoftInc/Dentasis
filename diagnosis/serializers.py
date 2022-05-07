from rest_framework.serializers import ModelSerializer, ValidationError

from diagnosis.models import DiagnosisSummaryCaries, DiagnosisSummaryDental, DiagnosisSummaryTeeth


class DiagnosisSummaryDentalSerializer(ModelSerializer):
    class Meta:
        model = DiagnosisSummaryDental
        exclude = ['user', 'date_created']


class DiagnosisSummaryTeethSerializer(ModelSerializer):
    class Meta:
        model = DiagnosisSummaryTeeth
        fields = '__all__'

    def validate_diagnosis_summary_dental(self, diagnosis_summary_dental):
        '''
        Checks if the user is the owner of diagnosis_summary_dental
        '''
        if diagnosis_summary_dental.user != self.context['request'].user:
            raise ValidationError("You do not have permission")
        return diagnosis_summary_dental


class DiagnosisSummaryCariesSerializer(ModelSerializer):
    class Meta:
        model = DiagnosisSummaryCaries
        fields = '__all__'

    def validate_diagnosis_summary_teeth(self, diagnosis_summary_teeth):
        '''
        Checks if the user is the owner of diagnosis_summary_teeth
        '''
        if diagnosis_summary_teeth.diagnosis_summary_dental.user != self.context['request'].user:
            raise ValidationError("You do not have permission")
        return diagnosis_summary_teeth
