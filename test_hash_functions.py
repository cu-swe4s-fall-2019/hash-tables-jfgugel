import unittest
import hash_functions

class TestHashFunctions(unittest.TestCase):
    
    def test_list__h_ascii_empty_list(self):        
        r = hash_functions.h_ascii([])
        self.assertEqual(r, None)
        
    def test_list_mean_for_None_list(self):
        r = hash_functions.h_ascii(None)
        self.assertEqual(r, None)


    

