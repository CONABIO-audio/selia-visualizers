from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from irekua_database.models import base
from irekua_database.models import ItemType

from irekua_database.utils import validate_JSON_schema
from irekua_database.utils import validate_JSON_instance
from irekua_database.utils import simple_JSON_schema


class Visualizer(base.IrekuaModelBase):
    name = models.CharField(
        max_length=64,
        db_column='name',
        verbose_name=_('name'),
        help_text=_('Name of visualizer app'),
        blank=False,
        null=False)
    description = models.TextField(
        db_column='description',
        verbose_name=_('description'),
        help_text=_('Description of the visualizer'),
        blank=True)
    website = models.URLField(
        db_column='website',
        verbose_name=_('website'),
        help_text=_('Link to visualizer website'),
        blank=True)
    configuration_schema = models.JSONField(
        db_column='configuration_schema',
        verbose_name=_('configuration schema'),
        help_text=_('JSON schema for visualizer tool configuration info'),
        blank=True,
        null=False,
        validators=[validate_JSON_schema],
        default=simple_JSON_schema)

    item_types = models.ManyToManyField(
        ItemType,
        through='VisualizerItemType',
        through_fields=('visualizer', 'item_type'))

    class Meta:
        verbose_name = _('Visualizer')
        verbose_name_plural = _('Visualizers')

        ordering = ['-created_on']

    def validate_configuration(self, configuration):
        try:
            validate_JSON_instance(
                schema=self.configuration_schema,
                instance=configuration)
        except ValidationError as error:
            msg = _('Invalid visualizer configuration. Error: %(error)s')
            params = dict(error=str(error))
            raise ValidationError(msg, params=params)

    def __str__(self):
        return str(self.name)
