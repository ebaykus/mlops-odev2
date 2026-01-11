import unittest
from prediction_service import hash_feature

class TestFeatureEngineering(unittest.TestCase):
    def test_hash_consistency(self):
        val1 = hash_feature("kalem")
        val2 = hash_feature("kalem")
        self.assertEqual(val1, val2)

    def test_value_range(self):
        val = hash_feature("kitap")
        self.assertTrue(0 <= val < 100)

if __name__ == '__main__':
    unittest.main()