import unittest
import hash_functions

class TestHashFunctions(unittest.TestCase):
    
    def test_list__h_ascii_empty_list(self):        
        r = hash_functions.h_ascii([])
        self.assertEqual(r, None)
        
    def test_list_h_ascii_for_None_list(self):
        r = hash_functions.h_ascii(None)
        self.assertEqual(r, None)
        
    def test_list__h_rolling_empty_list(self):        
        r = hash_functions.h_polynomial_rolling([])
        self.assertEqual(r, None)
        
    def test_list_h_rolling_for_None_list(self):
        r = hash_functions.h_polynomial_rolling(None)
        self.assertEqual(r, None)


    

