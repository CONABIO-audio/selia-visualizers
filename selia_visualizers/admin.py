from django.contrib import admin
from selia_visualizers import models


@admin.register(models.Visualizer, models.VisualizerItemType)
class VisualizersAdmin(admin.ModelAdmin):
    pass
