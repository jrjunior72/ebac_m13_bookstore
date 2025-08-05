import pytest
from order.models import Order
from ..factories.order_factory import OrderFactory
from tests.factories.product_factory import ProductFactory

@pytest.mark.django_db
def test_order_creation():
    product = [ProductFactory()]
    order = OrderFactory(product=product)
    assert order.pk is not None
    assert order.user is not None
    assert order.product.count() > 0

@pytest.mark.django_db
def test_order_with_products():
    product = [ProductFactory(), ProductFactory()]
    order = OrderFactory(product=product)
    assert order.product.count() == 2
