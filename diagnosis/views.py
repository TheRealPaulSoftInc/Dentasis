import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, parsers
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from diagnosis.models import (DiagnosisSummaryCaries, DiagnosisSummaryDental,
                              DiagnosisSummaryTeeth)
from diagnosis.permissions import (IsDiagnosisSummaryCariesOwner,
                                   IsDiagnosisSummaryTeethOwner, IsOwner)
from diagnosis.serializers import (DiagnosisSummaryCariesSerializer,
                                   DiagnosisSummaryDentalSerializer,
                                   DiagnosisSummaryTeethSerializer)


class DiagnosisSummaryDentalView(ListCreateAPIView):
    """
    get: List all DiagnosisSummaryDental of the authenticated user.
    post: Creates new DiagnosisSummaryDental.
    """

    serializer_class = DiagnosisSummaryDentalSerializer
    permission_classes = [IsAuthenticated, IsOwner, DjangoModelPermissions]
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser, parsers.FileUploadParser)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_favorite', 'date_created']
    search_fields = ['is_favorite', 'date_created']
    ordering_fields = ['is_favorite', 'date_created']
    ordering = ['is_favorite', 'date_created']

    def perform_create(self, serializer):
        teeth_name_types = ["molar", "premolar", "canino", "incisivo"]
        caries_types = ["corona", "fisura",
                        "radicular", "interdental", "recurrentes"]

        diagnosis_summary_dental = serializer.save(user=self.request.user)
        for i in range(random.randint(1, 4)):
            diagnosis_summary_teeth = DiagnosisSummaryTeeth(
                teeth_name=teeth_name_types[random.randint(0, 3)], teeth_number=random.randint(0, 31), diagnosis_summary_dental=diagnosis_summary_dental)
            diagnosis_summary_teeth.save()

            for i in range(random.randint(1, 2)):
                DiagnosisSummaryCaries(
                    caries_type=caries_types[random.randint(0, 4)], accuracy=random.uniform(75.5, 90.5), x_pos=random.uniform(5.5, 30.5), y_pos=random.uniform(5.5, 30.5), diagnosis_summary_teeth=diagnosis_summary_teeth).save()
        return diagnosis_summary_dental

    def get_queryset(self):
        return DiagnosisSummaryDental.objects.filter(user=self.request.user)


class DiagnosisSummaryDentalDetailView(RetrieveUpdateDestroyAPIView):
    """
    get: Retrieves a User's DiagnosisSummaryDental by Id
    put: Updates a DiagnosisSummaryDental by Id
    delete: Deletes a DiagnosisSummaryDental by Id
    """

    http_method_names = ['get', 'put', 'delete']
    serializer_class = DiagnosisSummaryDentalSerializer
    permission_classes = [IsAuthenticated, IsOwner, DjangoModelPermissions]
    lookup_field = 'id'

    def get_queryset(self):
        return DiagnosisSummaryDental.objects.filter(user=self.request.user)


class DiagnosisSummaryTeethView(ListAPIView):
    """
    get: List all DiagnosisSummaryTeeth of the authenticated user.
    """

    serializer_class = DiagnosisSummaryTeethSerializer
    permission_classes = [IsAuthenticated,
                          IsDiagnosisSummaryTeethOwner, DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
    ordering = ['diagnosis_summary_dental']

    def get_queryset(self):
        return DiagnosisSummaryTeeth.objects.filter(diagnosis_summary_dental__user=self.request.user)


class DiagnosisSummaryTeethDetailView(RetrieveUpdateDestroyAPIView):
    """
    get: Retrieves a User's DiagnosisSummaryTeeth by Id
    put: Updates a DiagnosisSummaryTeeth by Id
    delete: Deletes a DiagnosisSummaryTeeth by Id
    """

    http_method_names = ['get', 'put', 'delete']
    serializer_class = DiagnosisSummaryTeethSerializer
    permission_classes = [IsAuthenticated,
                          IsDiagnosisSummaryTeethOwner, DjangoModelPermissions]
    lookup_field = 'id'

    def get_queryset(self):
        return DiagnosisSummaryTeeth.objects.filter(diagnosis_summary_dental__user=self.request.user)


class DiagnosisSummaryCariesView(ListAPIView):
    """
    get: List all DiagnosisSummaryCaries of the authenticated user.
    """

    serializer_class = DiagnosisSummaryCariesSerializer
    permission_classes = [IsAuthenticated,
                          IsDiagnosisSummaryCariesOwner, DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
    ordering = ['diagnosis_summary_teeth']

    def get_queryset(self):
        return DiagnosisSummaryCaries.objects.filter(diagnosis_summary_teeth__diagnosis_summary_dental__user=self.request.user)


class DiagnosisSummaryCariesDetailView(RetrieveUpdateDestroyAPIView):
    """
    get: Retrieves a User's DiagnosisSummaryCaries by Id
    put: Updates a DiagnosisSummaryCaries by Id
    delete: Deletes a DiagnosisSummaryCaries by Id
    """

    http_method_names = ['get', 'put', 'delete']
    serializer_class = DiagnosisSummaryCariesSerializer
    permission_classes = [IsAuthenticated,
                          IsDiagnosisSummaryCariesOwner, DjangoModelPermissions]
    lookup_field = 'id'

    def get_queryset(self):
        return DiagnosisSummaryCaries.objects.filter(diagnosis_summary_teeth__diagnosis_summary_dental__user=self.request.user)
