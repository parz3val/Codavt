from unittest import mock
import pytest
from allocation.adapters import repository
from allocation.service_layer import services, unit_of_work

class FakeRepository(repository.AbstractRepository):
    def __init__(self, products):
        super().__init()
        self._products = set(products)
    
    def _add(self, product):
        self._products.add(product)
    
    def _get(self, sku):
        return next((p for p in self._products if p.sku == sku), None)
    

class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):

    def __init__(self):
        self.products = FakeRepository([])
        self.commited = False
    
    def _commit(self):
        self.commited = True
    
    def rollback(self):
        pass
    
def test_add_batch_for_new_product():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, uow)
    assert uow.products.get("CRUNCHY-ARMCHAIR") is not None
    assert uow.commited

def test_add_batch_for_exisiting_product():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "MACHINE-GUN-TABLE", 100, None, uow)
    services.add_batch("b2", "MACHINE-GUN-TABLE", 99, None, uow)

    assert "b2" in [b.reference for b in uow.products.get("MACHINE-GUN-TABLE").batches]


def test_allocate_returns_allocation():
    uow = FakeUnitOfWork()
    services.add_batch("batch1", "FANCY-LAMP", 100, None, uow)
    result = services.allocate("o1", "FANCY-LAMP", 10, uow)

def test_allocate_errors_for_invalid_sku():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "AREALSKU", 100, None, uow)

    with pytest.raises(services.InvalidSku, match="Invalid sku NONEXISTENTSKU"):
        services.allocate("o1", "NONEXISTENTSKU", 10, uow)

def test_allocate_commits():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "OMINIOUS-DINER", 100, None, uow)
    services.allocate("b1", "OMINIOUS-DINER", 10, uow)
    assert uow.commited

def test_sends_email_on_out_of_stock_error():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "SHINY-CURTAINS", 9, None, uow)
    
    with mock.patch("allocation.adapters.send_email") as mock_send_email:
        services.allocate("o1", "SHINY-CURTAINS", 10, uow)

        assert mock_send_email.call_args == mock.call(
            "stocchief@gmail.com",
            f"Out of stock for the SHINY-CURTAINS",
        )
