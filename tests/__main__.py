from app import get_message
import unittest

class TestMessage(unittest.TestCase):
    def test_message_good(self):
        assert get_message() == "Go Banana Slugs!"

if __name__ == "__main__":
    unittest.main()

