from django.db import models
import os
from django.utils.translation import gettext_lazy as _

from irekua_database.models import ItemType
from irekua_database.models.base import IrekuaModelBase


def visualizer_path(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'visualizers/{name}_{version}.{ext}'.format(
        name=instance.name.replace(' ', '_'),
        version=instance.version.replace('.', '_'),
        ext=ext)


class Visualizer(IrekuaModelBase):
    name = models.CharField(
        max_length=64,
        db_column='name',
        verbose_name=_('name'),
        help_text=_('Name of visualizer app'),
        blank=False,
        null=False)
    version = models.CharField(
        max_length=16,
        db_column='version',
        verbose_name=_('version'),
        help_text=_('Version of visualizer app'),
        blank=False,
        null=False)
    javascript_file = models.FileField(
        upload_to=visualizer_path,
        db_column='javascript_file',
        verbose_name=_('javascript file'),
        help_text=_('Javascript file containing visualizer component'),
        blank=False,
        null=False)
    repository = models.URLField(
        db_column='repository',
        verbose_name=_('repository'),
        help_text=_('Link to app repository'),
        blank=True)

    item_types = models.ManyToManyField(
        ItemType,
        through='VisualizerItemType',
        through_fields=('visualizer', 'item_type'))

    class Meta:
        verbose_name = _('Visualizer')
        verbose_name_plural = _('Visualizers')

        ordering = ['-created_on']
        unique_together = (
            ('name', 'version'),
        )

    def __str__(self):
        return '{}@{}'.format(self.name, self.version)


class VisualizerItemType(models.Model):
    item_type = models.ForeignKey(
        ItemType,
        on_delete=models.CASCADE)
    visualizer = models.ForeignKey(
        'Visualizer',
        on_delete=models.CASCADE)

    is_active = models.BooleanField(
        db_column='is_active',
        verbose_name=_('is active'),
        help_text=_('Is visualizer app active?'),
        default=True,
        blank=False,
        null=False)

    class Meta:
        verbose_name = _('VisualizerItemType')
        verbose_name_plural = _('VisualizerItemTypes')

        unique_together = (
            ('item_type', 'visualizer'),
        )

    def deactivate(self):
        self.is_active = False
        self.save()

    def save(self, *args, **kwargs):
        if self.is_active:
            queryset = VisualizerItemType.objects.filter(
                item_type=self.item_type, is_active=True)
            for entry in queryset:
                if entry != self:
                    entry.deactivate()

        super().save(*args, **kwargs)
