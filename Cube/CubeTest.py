import unittest
import Cube

class TestCube(unittest.TestCase):
	def test_cube(self):
		self.assertEqual(Cube.cube(3), 27)
		self.assertIsNotNone(Cube.cube(10))
		self.assertIs(Cube.cube(5), 125)

if __name__ == '__main__':
	unittest.main()