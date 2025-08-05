import pytest
from order.serializers import OrderSerializer
from tests.factories.order_factory import OrderFactory
from tests.factories.product_factory import ProductFactory

@pytest.mark.django_db
def test_order_serializer_data():
    products = ProductFactory.create_batch(2)
    order = OrderFactory(products=products)
    serializer = OrderSerializer(order)
    data = serializer.data

    assert data["id"] == order.id
    assert data["status"] == order.status
    assert len(data["products"]) == 2
