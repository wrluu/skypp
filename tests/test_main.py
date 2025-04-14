import pytest
from src.main import Product, Category

@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0

def test_product_initialization():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10

def test_category_initialization():
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    category = Category("Test Category", "Test Description", [product1, product2])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2

def test_multiple_categories():
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    product3 = Product("Product 3", "Description 3", 300.0, 2)
    category1 = Category("Category 1", "Description 1", [product1, product2])
    category2 = Category("Category 2", "Description 2", [product3])
    assert Category.category_count == 2
    assert Category.product_count == 3
