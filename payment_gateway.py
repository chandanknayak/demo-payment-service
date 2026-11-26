# payment_gateway.py
def process_transaction(user_id: str, amount: float, currency: str = "USD") -> dict:
    """Critical payment transaction processor."""
    if amount <= 0:
        raise ValueError("Invalid amount")
    return {"status": "SUCCESS", "user_id": user_id, "amount": amount, "currency": currency}

def refund_transaction(transaction_id: str, amount: float) -> dict:
    """Process customer refund."""
    return {"refund_id": f"ref_{transaction_id}", "amount": amount, "status": "REFUNDED"}