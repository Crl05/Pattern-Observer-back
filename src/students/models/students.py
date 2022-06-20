from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit


class Student(Audit):
    model_name = _('Students')

    name: str = models.CharField(_('Name'), max_length=50, default='')
    last_name: str = models.CharField(_('Last name'), max_length=50, default='')
    note: float = models.FloatField(_('Note'), max_length=100, default=0)

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return f'{self.name} {self.last_name}'
