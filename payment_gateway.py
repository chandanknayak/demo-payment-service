# payment_gateway.py

def process_transaction(user_id: str, total_amount: float) -> dict:
    """Critical payment transaction processor."""
    if total_amount <= 0:
        raise ValueError("Invalid amount")
    return {"status": "SUCCESS", "user_id": user_id, "amount": total_amount}

def refund_transaction(transaction_id: str, amount: float) -> dict:
    """Process customer refund."""
    return {"refund_id": f"ref_{transaction_id}", "amount": amount, "status": "REFUNDED"}

def get_supported_currencies() -> list[str]:
    """Safe non-breaking helper function."""
    return ["USD", "EUR", "INR", "GBP"]
