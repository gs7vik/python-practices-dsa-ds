import pytest
from shopping_cart import ShoppingCart
from unittest.mock import mock
from retreive_from_db import Database

@pytest.fixture
def cart():
    return ShoppingCart(2)

def test_can_add_item_to_cart(cart):
     
    cart.add("apple")
    assert cart.size()==1 #if statement is true..the line will succeed or else an exception will be thrown making the test fail
    
def test_items_are_getting_added(cart):
     
    cart.add('apple')
    assert "apple" in cart.get_items()
    


def test_items_more_than_maxsize_fail(cart):
     
    for _ in range(2):
        cart.add('panipuri')
        
    with pytest.raises(OverflowError):
        cart.add('ad')

def test_get_total_price(cart):
    cart.add('apple')
    cart.add('orran')
    price_map={'apple':1,'orran':2}
    assert cart.get_total_price(price_map) == 3
    
    
@mock.patch('retrieve_from_db.get_user_by_id')
def test_get_user_by_id(mock_get_user_by_id):
    mock_get_user_by_id.return_value='satvik'
    user_name= Database.get_user_by_id('1')
    assert user_name==mock_get_user_by_id