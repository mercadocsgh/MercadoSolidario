import pytest
from django.contrib.auth import get_user_model
from django.test import RequestFactory

from Mercado.middleware import TenantMiddleware
from Mercado.models import Tenant, UserTenant
from Mercado.tenant import set_current_tenant, get_current_tenant, clear_current_tenant


def test_thread_local_helpers_store_and_clear_tenant():
    tenant = Tenant(name='Tenant A', slug='tenant-a')

    clear_current_tenant()
    assert get_current_tenant() is None

    set_current_tenant(tenant)
    assert get_current_tenant() == tenant

    clear_current_tenant()
    assert get_current_tenant() is None


@pytest.mark.django_db
def test_middleware_assigns_tenant_from_authenticated_user():
    tenant = Tenant.objects.create(name='Tenant B', slug='tenant-b')
    user = get_user_model().objects.create_user(
        username='tenant-user', password='testpass', email='user@example.com'
    )
    UserTenant.objects.create(user=user, tenant=tenant)
    request = RequestFactory().get('/')
    request.user = user

    middleware = TenantMiddleware(lambda req: req)
    response = middleware(request)

    assert response.tenant == tenant
    assert request.tenant == tenant
    # middleware must clean thread-local context after response cycle
    assert get_current_tenant() is None


@pytest.mark.django_db
def test_middleware_handles_user_without_tenant():
    user = get_user_model().objects.create_user(
        username='no-tenant', password='testpass', email='no-tenant@example.com'
    )
    request = RequestFactory().get('/')
    request.user = user

    middleware = TenantMiddleware(lambda req: req)
    response = middleware(request)

    assert response.tenant is None
    assert request.tenant is None
    assert get_current_tenant() is None
