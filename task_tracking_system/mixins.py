from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user_creator != request.user:
            raise PermissionDenied("It's not your task! Dont touch it!")
        return super().dispatch(request, *args, **kwargs)