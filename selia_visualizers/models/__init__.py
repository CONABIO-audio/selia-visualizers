import os

from .visualizer_module_item_type import VisualizerModuleItemType
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
    'VisualizerModuleItemType',
    'VisualizerModule',
    'visualizer_path',
    'VisualizerVersion',
    'Visualizer',
]
