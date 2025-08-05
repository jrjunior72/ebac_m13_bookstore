import pytest
from order.serializers import OrderSerializer
from tests.factories.order_factory import OrderFactory
from tests.factories.product_factory import ProductFactory

@pytest.mark.django_db
def test_order_serializer_data():
    product = [ProductFactory(title="Livro A"), ProductFactory(title="Livro B")]
    order = OrderFactory(product=product)
    serializer = OrderSerializer(order)
    data = serializer.data

    # assert data["status"] == order.status
    # assert len(data["product"]) == 2

    product_titles = [product["title"] for product in data["product"]]
    assert "Livro A" in product_titles
    assert "Livro B" in product_titles
