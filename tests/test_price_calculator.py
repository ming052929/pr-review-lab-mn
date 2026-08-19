# 放置檔案：tests/test_price_calculator.py（刪除原內容後，完整貼上）
import unittest

from app.price_calculator import calculate_total


class CalculateTotalTests(unittest.TestCase):
    def test_without_discount(self) -> None:
        # 保留原本的基本情境，避免新增驗證時破壞正常計算。
        self.assertEqual(calculate_total(100, 2), 200)

    def test_with_discount(self) -> None:
        # 確認折扣邏輯仍維持原本行為。
        self.assertEqual(calculate_total(100, 2, 15), 170)

    def test_rejects_negative_unit_price(self) -> None:
        # 新增：負數單價應被拒絕。
        with self.assertRaises(ValueError):
            calculate_total(-100, 2)

    def test_rejects_negative_quantity(self) -> None:
        # 新增：負數數量應被拒絕。
        with self.assertRaises(ValueError):
            calculate_total(100, -2)

    def test_rejects_invalid_discount(self) -> None:
        # 新增：超出 0 到 100 的折扣應被拒絕。
        with self.assertRaises(ValueError):
            calculate_total(100, 2, 101)


if __name__ == "__main__":
    unittest.main()