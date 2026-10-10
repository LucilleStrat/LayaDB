from layadb.Quantity import extract_quantity_from_string

def test_remove_5_pens():
    assert extract_quantity_from_string("remove 5 pens") == 5

def test_add_10_items():
    assert extract_quantity_from_string("add 10 items") == 10

def test_delete_1_thing():
    assert extract_quantity_from_string("delete 1 thing") == 1

def test_decimal_quantity():
    assert extract_quantity_from_string("remove 2.5 reams") == 2

def test_empty_string():
    assert extract_quantity_from_string("") is None

def test_no_quantity():
    assert extract_quantity_from_string("nothing here") is None
