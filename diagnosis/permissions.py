from django.contrib.auth import get_user_model
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit and retrieve it.
    Assumes the model instance has an 'user' attribute.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsDiagnosisSummaryTeethOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of a DiagnosisSummaryTeeth to edit and retrieve it.
    Assumes the model instance has an 'user' attribute.
    """

    def has_object_permission(self, request, view, obj):
        return obj.diagnosis_summary_dental.user == request.user


class IsDiagnosisSummaryCariesOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of a DiagnosisSummaryCaries to edit and retrieve it.
    Assumes the model instance has an 'user' attribute.
    """

    def has_object_permission(self, request, view, obj):
        return obj.diagnosis_summary_teeth.diagnosis_summary_dental.user == request.user
