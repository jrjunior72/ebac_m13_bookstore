import pytest
from product.models import Product, Category
from tests.factories.product_factory import ProductFactory, CategoryFactory

@pytest.mark.django_db
def test_product_creation():
    product = ProductFactory()
    assert isinstance(product, Product)
    assert product.title
    assert product.price > 0

@pytest.mark.django_db
def test_product_with_category():
    category = CategoryFactory()
    product = ProductFactory(category=[category])
    assert product.category.count() == 1

