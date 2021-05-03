import unittest
import Cube

class TestCube(unittest.TestCase):
	def test_Equal(self):
		self.assertEqual(Cube.cube(3), 27)

	def test_NotNone(self):
		self.assertIsNotNone(Cube.cube(10))

	def test_is(self):
		self.assertIs(Cube.cube(5), 125)

if __name__ == '__main__':
	unittest.main()