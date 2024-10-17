import unittest
from scripts.backtest_strategy import backtest_strategy
import pandas as pd

class TestBacktestStrategy(unittest.TestCase):
    def test_backtest(self):
        data = pd.DataFrame({
            'Close': [100, 102, 105, 107, 110],
        })
        signals = [1, 0, 0, -1, 0]  # Buy on first, sell on fourth day
        result = backtest_strategy(data, signals)
        self.assertAlmostEqual(result['Balance'].iloc[-1], 10700)

if __name__ == '__main__':
    unittest.main()
