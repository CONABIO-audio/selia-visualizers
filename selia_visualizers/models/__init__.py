import os

from .visualizer_item_type import VisualizerItemType
from .visualizer_module import VisualizerModule
from .visualizer_version import VisualizerVersion
from .visualizer import Visualizer


def visualizer_path(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'visualizers/{name}_{version}.{ext}'.format(
        name=instance.visualizer.name.replace(' ', '_'),
        version=instance.visualizer.version.replace('.', '_'),
        ext=ext)


__all__ = [
    'VisualizerItemType',
    'VisualizerModule',
    'visualizer_path',
    'VisualizerVersion',
    'Visualizer',
]
