import unittest
import Average

list = [1,2,3,4,5,6,7,8,9,10, 11] ## should average of 6 

class TestAverage(unittest.TestCase):
	
	def test_average(self):
		self.assertEqual(Average.Average(list), 5)

	def test_listNotEmpty(self):
		self.assertIsNotNone(Average.Average(list))

	def test_listNotEqual(self):
		self.assertNotEqual(Average.Average(list), 0)


if __name__ == '__main__':
	unittest.main()