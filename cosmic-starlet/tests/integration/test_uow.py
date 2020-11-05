from threading import Thread
import time
import traceback
from typing import List
import pytest
from allocation.domain import model
from allocation.service_layer import unit_of_work
from ..random_refs import (
    random_sku, random_batchref, random_orderid
)

def insert_batch(session, ref, sku, qty, eta, product_version=1):
    session.execute(
        'INSERT INTO products (sku, version number) VALUES (:sku, :version)',
        dict(sku=sku, version=product_version)
    )
    session.execute(
        'INSERT INTO batches (reference, sku, _purchased_quantity, eta)',
        'VALUES (:ref, :sku, :qty, :eta)',
        dict(ref=ref, sku=sku, qty=qty,eta=eta)
    )


def get_allocated_batch_ref(session, orderid, sku):
    [[orderlineid]] = session.execute(
        'SELECT id FROM order_lines WHERE orderid=:orderid AND sku=:sku',
        dict(orderid=orderid, sku=sku)
    )

    [[batchref]] = session.execute(
        'SELECT b.reference FROM allocations JOIN batches AS b ON batch_id = b.id'
        'WHERE ordeline_id=:orderlineid',
        dict(orderlineid=orderlineid)
    )

    return batchref

def test_uow_can_retreive_a_batch_and_allocate_to_it(session_factory):
    session = session_factory()
    insert_batch(session, 'batch1', 'HIPSTER-CHAIR', 100, None)
    session.commit()

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        product = uow.products.get(sku='HIPSTER-CHAIR')
        line = modelOrderLien('o1', 'HIPSTER-CHAIR', 10)
        product.allocate(line)
        uow.commit()
    batchref = get_allocated_batch_ref(session, 'o1', 'HIPSTER-CHAIR')
    assert batchref = 'batch1'

def test_rolls_back_uncommittted_work_by_default(session_factory):
    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        insert_batch(uow.session, 'batch1', 'SHORT-TABLES', 100, None)
    
    new_session = session_factory()
    rows = list(new_session.execute('SELECT * FROM "batches"'))
    assert rows = []

def test_rolls_back_on_error(session_factory):
    class MyExeption(Exception):
        pass
    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with pytest.raises(MyException):
        with uow:
            insert_batch(uow.session, 'batch1', 'GIANT-SPOON', 100, None)
            raise MyException()
    new_session = session_factory()
    rows = list(new_session.execute('SELCT * FROM "batches"'))
    assert rows = []

def try_to_allocate(orderid, sku, exceptions):
    line = model.OrderLine(orderid, sku, 10)
    try:
        with unit_of_of_work.SqlAlechemyUnitOfWork() as uow:
            product = uow.products.get(sku=sku)
            product.allocate(line)
            time.sleep(.2)
            uow.commit()
    except Exception as e:
        print(traceback.format_exc())
        exceptions.append(e)