

class UserQuerySetMixin():
    user_field = 'owner'
    allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        qs = super().get_queryset(*args, **kwargs)

        if self.allow_staff_view and user.is_staff:
            return qs

        if not user.is_authenticated:
            return qs.none()

        lookup_data = {}
        lookup_data[self.user_field] = user
        return qs.filter(**lookup_data)


