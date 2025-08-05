import factory
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()

from order.models import Order
from .product_factory import ProductFactory


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.PostGenerationMethodCall("set_password", "123456")

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    status = factory.Iterator(["pending", "completed", "cancelled"])

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.product.add(product)

    class Meta:
        model = Order
