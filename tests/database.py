from layadb.Database import Database
from layadb.Database.Schema import Entry

def test_add_and_get_entry() -> None:
    database = Database("test_quantity.db")
    entry = Entry(id="1", name="pen", quantity=10)

    assert database.add_entry(entry) is True

    retrieved = database.get_entry("1")
    assert retrieved is not None
    assert retrieved.id == "1"
    assert retrieved.name == "pen"
    assert retrieved.quantity == 10

    database.close()

def test_remove_entry() -> None:
    database = Database("test_quantity.db")
    entry = Entry(id="2", name="notebook", quantity=5)
    database.add_entry(entry)

    assert database.remove_entry("2") is True
    assert database.get_entry("2") is None

    database.close()

def test_patch_entry() -> None:
    database = Database("test_quantity.db")
    entry = Entry(id="3", name="paper", quantity=100)
    database.add_entry(entry)

    assert database.patch_entry("3", {"quantity": 200}) is True

    retrieved = database.get_entry("3")
    assert retrieved is not None
    assert retrieved.quantity == 200

    database.close()

def test_list_entries() -> None:
    database = Database("test_quantity.db")
    database.add_entry(Entry(id="4", name="pen", quantity=1))
    database.add_entry(Entry(id="5", name="paper", quantity=2))

    entries = database.list_entries()
    assert len(entries) >= 2

    ids = {entry.id for entry in entries}

    assert "4" in ids
    assert "5" in ids

    database.close()

def test_get_nonexistent() -> None:
    database = Database("test_quantity.db")

    assert database.get_entry("nonexistent") is None

    database.close()

def test_remove_nonexistent() -> None:
    database = Database("test_quantity.db")

    assert database.remove_entry("nonexistent") is False

    database.close()

def test_patch_nonexistent() -> None:
    database = Database("test_quantity.db")

    assert database.patch_entry("nonexistent", {"quantity": 5}) is False

    database.close()

def test_add_multiple_same_id() -> None:
    database = Database("test_quantity.db")
    database.add_entry(Entry(id="6", name="a", quantity=1))
    database.add_entry(Entry(id="6", name="b", quantity=2))

    retrieved = database.get_entry("6")
    assert retrieved is not None
    assert retrieved.name == "b"
    assert retrieved.quantity == 2

    database.close()
