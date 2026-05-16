

class UserQuerySetMixin():
    user_field = 'owner'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        qs = super().get_queryset(*args, **kwargs)

        if not user.is_authenticated:
            return qs.none()

        lookup_data = {}
        lookup_data[self.user_field] = user
        return qs.filter(**lookup_data)
        

