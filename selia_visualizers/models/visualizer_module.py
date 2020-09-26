import os

from django.db import models
from django.utils.translation import gettext_lazy as _

from irekua_database.models import ItemType
from selia_visualizers.models.visualizer_version import VisualizerVersion


def visualizer_version_module_path(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'visualizers/{name}_{version}.{ext}'.format(
        name=instance.visualizer.name.replace(' ', '_'),
        version=instance.visualizer.version.replace('.', '_'),
        ext=ext)


class VisualizerModule(VisualizerVersion):
    javascript_file = models.FileField(
        upload_to=visualizer_version_module_path,
        db_column='javascript_file',
        verbose_name=_('javascript file'),
        help_text=_('Javascript file containing visualizer version module'),
        blank=False,
        null=False)

    item_types = models.ManyToManyField(
        ItemType,
        through='VisualizerModuleItemType',
        through_fields=('visualizer_module', 'item_type'))

    class Meta:
        verbose_name = _('Visualizer Version Module')
        verbose_name_plural = _('Visualizers Version Modules')

    def __str__(self):
        return str(self.visualizer)
