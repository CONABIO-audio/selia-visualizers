from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from selia_visualizers.models import VisualizerItemType


@require_http_methods(["GET"])
def get_visualizer(request):
    mime_type = request.GET.get('item_type', None)
    visualizer = get_object_or_404(VisualizerItemType, item_type=mime_type, is_active=True)
    return HttpResponseRedirect(visualizer.visualizer.javascript_file.url)
