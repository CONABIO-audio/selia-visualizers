from django.shortcuts import get_object_or_404
from selia_visualizers.models import VisualizerComponentItemType


def get_visualizer(item_type):
    visualizer = get_object_or_404(
        VisualizerComponentItemType,
        item_type=item_type,
        is_active=True)
    return visualizer
