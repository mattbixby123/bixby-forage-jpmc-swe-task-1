import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Assertions added below ------------ """
    for quote in quotes:
       stock, bid_price, ask_price, price = getDataPoint(quote)
       self.assertEqual(stock, quote['stock'])
       self.assertEqual(bid_price, quote['top_bid']['price'])
       self.assertEqual(ask_price, quote['top_ask']['price'])
       self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Assertions added below ------------ """
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(stock, quote['stock'])
            self.assertEqual(bid_price, quote['top_bid']['price'])
            self.assertEqual(ask_price, quote['top_ask']['price'])
            self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_positiveNumbers(self):
        self.assertEqual(getRatio(10, 2), 5)
        self.assertEqual(getRatio(15, 3), 5)
        self.assertEqual(getRatio(20, 4), 5)

  def test_getRatio_negativeNumbers(self):
        self.assertEqual(getRatio(-10, 2), -5)
        self.assertEqual(getRatio(10, -2), -5)
        self.assertEqual(getRatio(-10, -2), 5)

  def test_getRatio_zeroDenominator(self):
        self.assertIsNone(getRatio(10, 0))
        self.assertIsNone(getRatio(0, 0))

  def test_getRatio_floats(self):
        self.assertAlmostEqual(getRatio(10.5, 2.5), 4.2)
        self.assertAlmostEqual(getRatio(7.5, 2.5), 3.0)

  def test_getRatio_largeNumbers(self):
        self.assertAlmostEqual(getRatio(1e10, 2), 5e9)
        self.assertAlmostEqual(getRatio(1e10, 1e-10), 1e20)


if __name__ == '__main__':
    unittest.main()
