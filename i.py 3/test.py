# i wrote all of this code

import unittest
import surfshop

class SurfTests(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboards(self):
    string = self.cart.add_surfboards(1)
    self.assertEqual(string, 'Successfully added 1 surfboard to cart!')

  def test_add_surfboards1(self):
    for i in range(2, 5):
      with self.subTest(i=i):
        string1 = self.cart.add_surfboards(i)
        self.assertEqual(string1, f'Successfully added {i} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()

  @unittest.skip
  def test_too_many_boards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  # @unittest.expectedFailure
  def test_locals_discount(self):
    self.assertTrue(self.cart.locals_discount)

unittest.main()