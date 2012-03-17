import unittest
import broable

class TestMyShit(unittest.TestCase):

    def test_myshit(self):
        self.assertTrue(broable.isBroable("low"))
        self.assertTrue(broable.isBroable("rohan"))
        self.assertTrue(broable.isBroable("Momentum"))
        self.assertTrue(broable.isBroable("programming"))

if __name__ == '__main__':
    print "fuckyeah"
    unittest.main()
