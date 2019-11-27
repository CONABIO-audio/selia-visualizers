from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from selia_visualizers.models import VisualizerComponentItemType


@require_http_methods(["GET"])
def get_visualizer(request):
    item_type = request.GET.get('item_type', None)
    visualizer = get_object_or_404(
        VisualizerComponentItemType,
        item_type=item_type,
        is_active=True)

    response = {
        "visualizer": visualizer.visualizer_component.visualizer.pk,
        "file_url": visualizer.visualizer_component.javascript_file.url
    }
    return JsonResponse(response)
