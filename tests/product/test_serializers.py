import pytest
from product.serializers import ProductSerializer
from tests.factories.product_factory import ProductFactory

@pytest.mark.django_db
def test_product_serializer_data():
    product = ProductFactory()
    serializer = ProductSerializer(product)
    data = serializer.data

    assert data["title"] == product.title
    assert float(data["price"]) == float(product.price)
    assert "category" in data
