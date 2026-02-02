from django.core.exceptions import ObjectDoesNotExist

from .tenant import set_current_tenant, clear_current_tenant


class TenantMiddleware:
    """
    Associates the authenticated user with a tenant for the request lifecycle.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        clear_current_tenant()
        tenant = None
        if request.user.is_authenticated:
            try:
                user_tenant = request.user.user_tenant
            except ObjectDoesNotExist:
                user_tenant = None
            if user_tenant and user_tenant.is_active and user_tenant.tenant.is_active:
                tenant = user_tenant.tenant

        request.tenant = tenant
        if tenant:
            set_current_tenant(tenant)

        response = self.get_response(request)
        clear_current_tenant()
        return response
