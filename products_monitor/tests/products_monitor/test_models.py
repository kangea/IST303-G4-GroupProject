import pytest
import datetime

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

@pytest.mark.xfail
def test_failaddbrand():
    b = Brand.objects.create(
        name="goodbye",
        logo_url=None
    )
    assert b.name == "goodbye"

def test_queryBrand():
    Brand.objects.create(
        name="hello",
        url="hello.com",
        logo_url="hello_pic.jpg"
    )
    b = Brand.objects.filter(name="hello")
    assert b[0].name == "hello"

def test_queryProduct():
    b = Brand.objects.create(
        name="hello",
        url="hello.com",
        logo_url="hello_pic.jpg"
    )
    Product.objects.create(
        name="1",
        brand=b,
        price=100,
        restock_date = datetime.datetime.now(),
        original_release_date = datetime.datetime.now(),
        instock = True
    )
    Product.objects.create(
        name="1",
        brand=b,
        price=100,
        restock_date = datetime.datetime.now(),
        original_release_date = datetime.datetime.now(),
        instock = True
    )
    p_list = list(Product.objects.filter(brand=b))
    assert len(p_list) == 2

@pytest.mark.xfail
def test_failBrandquery():
    Brand.objects.create(
        name="hello",
        url="hello.com",
        logo_url="hello.jpg"
    )
    Brand.objects.create(
        name="goodbye",
        url="goodbye.com",
        logo_url="goodbye.jpg"
    )
    b_list = list(Brand.objects.filter(name="ciao"))
    assert b_list[0].name == "ciao"
