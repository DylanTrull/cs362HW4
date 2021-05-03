import unittest
import Name

class TestName(unittest.TestCase):
	def test_NotNone(self):
		self.assertIsNotNone(Name.name("Dylan", "Matthew"))
		
	def test_Equal(self):
		self.assertMultiLineEqual(Name.name("John", "Phillip"), "John Phillip")

	def test_NotEqual(self):
		self.assertMultiLineEqual(Name.name("Collette", "Adele"), "ColletteAdele")


if __name__ == '__main__':
	unittest.main()