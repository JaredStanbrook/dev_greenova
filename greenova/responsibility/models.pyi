# Stub file for responsibility.models

from django.db import models

class Responsibility(models.Model):
    name: models.CharField
    description: models.TextField
    company: models.ForeignKey
    is_active: models.BooleanField

    class Meta:
        verbose_name: str
        verbose_name_plural: str
        unique_together: list[str]

    def __str__(self) -> str: ...

class ResponsibilityAssignment(models.Model):
    user: models.ForeignKey
    responsibility: models.ForeignKey
    obligation: models.ForeignKey
    role: models.ForeignKey
    created_by: models.ForeignKey
    created_at: models.DateTimeField

    class Meta:
        verbose_name: str
        verbose_name_plural: str
        ordering: list[str]
        unique_together: list[str]

    def __str__(self) -> str: ...
