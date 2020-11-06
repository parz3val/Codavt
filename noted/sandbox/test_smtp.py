from fixtures import (
    smtp_connection
)
# Test func
def test_smtp(smtp_connection):
    response = smtp_connection.ehlo()
    assert response == 250
    assert 0
