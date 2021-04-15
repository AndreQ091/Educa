from rest_framework.authentication import BaseAuthentication


class IsEnrolled(BaseAuthentication):
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exist()
