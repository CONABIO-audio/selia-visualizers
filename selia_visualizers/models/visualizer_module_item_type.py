from django.db import models
from django.utils.translation import gettext_lazy as _

from irekua_database.models import ItemType


class VisualizerModuleItemType(models.Model):
    item_type = models.ForeignKey(
        ItemType,
        on_delete=models.CASCADE,
        db_column='item_type_id',
        verbose_name=_('item type'),
        help_text=_('Item type'))
    visualizer_module = models.ForeignKey(
        'VisualizerModule',
        on_delete=models.CASCADE,
        db_column='visualizer_module_id',
        verbose_name=_('visualizer module'),
        help_text=_('Visualizer module'))

    is_active = models.BooleanField(
        db_column='is_active',
        verbose_name=_('is active'),
        help_text=_('Is visualizer app active?'),
        default=True,
        blank=False,
        null=False)

    class Meta:
        verbose_name = _('Visualizer Module Item Type')
        verbose_name_plural = _('Visualizer Module Item Types')

        unique_together = (
            ('item_type', 'visualizer_module'),
        )

    def deactivate(self):
        self.is_active = False
        self.save()

    def save(self, *args, **kwargs):
        if self.is_active:
            queryset = VisualizerModuleItemType.objects.filter(
                item_type=self.item_type, is_active=True)
            for entry in queryset:
                if entry != self:
                    entry.deactivate()

        super().save(*args, **kwargs)
