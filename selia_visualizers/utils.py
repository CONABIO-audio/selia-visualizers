from selia_visualizers.models import VisualizerModuleItemType


def get_visualizer_module_instance(item_type):
    visualizer = VisualizerModuleItemType.objects.get(
        item_type=item_type,
        is_active=True)
    return visualizer.visualizer_module
