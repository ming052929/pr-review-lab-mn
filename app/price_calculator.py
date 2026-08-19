"""刻意維持簡單、用來練習 PR 審查的小程式。"""


def calculate_total(unit_price: float, quantity: int, discount_percent: float = 0) -> float:
    """計算折扣後的訂單總額。

    起始版本刻意沒有輸入驗證，讓學生可以在自己的 PR 補上驗證與測試。
    """
    # 目前先直接計算；課堂實作時會在此處加入負數與折扣範圍檢查。
    subtotal = unit_price * quantity
    return round(subtotal * (1 - discount_percent / 100), 2)
