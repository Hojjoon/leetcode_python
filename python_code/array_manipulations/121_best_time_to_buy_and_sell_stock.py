class Solution:
    # noinspection PyMethodMayBeStatic
    def max_profit(self, prices: list) -> int:

        if len(prices) == 0 or len(prices) == 1:
            return 0

        min_price = sys.maxsize
        max_profit = -sys.maxsize

        for i in prices:
            min_price = min(min_price, i)
            max_profit = max(max_profit, i - min_price)

        return max_profit
