import pytest

from products_monitor.models import Product, Brand, ProductURL

pytestmark = pytest.mark.django_db

def test_addBrand():
    b = Brand.objects.create(
        name="hello",
        url="hello.com",
        logo_url="hello_pic.jpg"
    )
    assert b.name == "hello"
    assert b.url == "hello.com"
