# test_payment.py
from payment_gateway import process_transaction, get_supported_currencies

def test_currencies():
    currencies = get_supported_currencies()
    assert "USD" in currencies
    assert "INR" in currencies

def test_valid_transaction():
    result = process_transaction("user_123", 100.0)
    assert result["status"] == "SUCCESS"
