from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from irekua_database.models import Item
# from selia_visualizers.models import VisualizerModuleItemType


class ItemVisualizerView(DetailView):
    template_name = 'selia_visualizers/visualizer.html'
    model = Item
    no_permission_template = 'selia_templates/generic/no_permission.html'

    def has_view_permission(self):
        return self.request.user.is_authenticated

    def no_permission_redirect(self):
        return render(self.request, self.no_permission_template)

    def get(self, *args, **kwargs):
        if not self.has_view_permission():
            return self.no_permission_redirect()

        return super().get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        # module = get_object_or_404(
        #     VisualizerModuleItemType,
        #     item_type=self.object.item_type,
        #     is_active=True).visualizer_module

        return {
            **super().get_context_data(*args, **kwargs),
            # 'module': module,
        }
