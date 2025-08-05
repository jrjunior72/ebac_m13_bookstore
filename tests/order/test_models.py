import pytest
from order.models import Order
from ..factories.order_factory import OrderFactory
from tests.factories.product_factory import ProductFactory

@pytest.mark.django_db
def test_order_creation():
    order = OrderFactory()
    assert order.pk is not None
    assert order.user is not None
    assert order.products.count() > 0

@pytest.mark.django_db
def test_order_with_products():
    products = ProductFactory.create_batch(2)
    order = OrderFactory(products=products)
    assert order.products.count() == 2
