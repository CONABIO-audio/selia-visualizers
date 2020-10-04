from selia_visualizers import models


def get_visualizer_module_instance(item_type):
    visualizer = models.VisualizerItemType.objects.get(
        item_type=item_type,
        is_active=True)
    return models.VisualizerModule.objects.get(
        visualizer=visualizer,
        is_active=True)
