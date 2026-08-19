import unittest

from app.price_calculator import calculate_total


class CalculateTotalTests(unittest.TestCase):
    def test_without_discount(self) -> None:
        # 基本情境：不給折扣時，總額就是單價乘數量。
        self.assertEqual(calculate_total(100, 2), 200)

    def test_with_discount(self) -> None:
        # 基本情境：確認既有折扣計算不會因後續修改而壞掉。
        self.assertEqual(calculate_total(100, 2, 15), 170)


if __name__ == "__main__":
    unittest.main()
