# 放置檔案：app/price_calculator.py（刪除原內容後，完整貼上）
"""用來練習 PR 審查的小型價格計算模組。"""


def calculate_total(unit_price: float, quantity: int, discount_percent: float = 0) -> float:
    """先驗證輸入，再回傳折扣後的訂單總額。"""
    # 價格與數量不可為負數，否則訂單沒有合理意義。
    if unit_price < 0:
        raise ValueError("unit_price cannot be negative")
    if quantity < 0:
        raise ValueError("quantity cannot be negative")

    # 折扣必須落在 0 到 100 之間，避免計算出負總額或不合理結果。
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")

    subtotal = unit_price * quantity
    return round(subtotal * (1 - discount_percent / 100), 2)