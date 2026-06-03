import unittest
import pandas as pd
from solution import combine_two_tables

class TestSolution(unittest.TestCase):
    def test_example1(self):
        person_data = {
            'personId': [1, 2],
            'lastName': ['Wang', 'Alice'],
            'firstName': ['Allen', 'Bob']
        }
        address_data = {
            'addressId': [1, 2],
            'personId': [2, 3],
            'city': ['New York City', 'Leetcode'],
            'state': ['New York', 'California']
        }
        
        person_df = pd.DataFrame(person_data)
        address_df = pd.DataFrame(address_data)
        
        result_df = combine_two_tables(person_df, address_df)
        
        # Verify shape
        self.assertEqual(len(result_df), 2)
        
        # Verify Bob
        bob_row = result_df[result_df['firstName'] == 'Bob'].iloc[0]
        self.assertEqual(bob_row['city'], 'New York City')
        self.assertEqual(bob_row['state'], 'New York')
        
        # Verify Allen
        allen_row = result_df[result_df['firstName'] == 'Allen'].iloc[0]
        self.assertTrue(pd.isna(allen_row['city']))
        self.assertTrue(pd.isna(allen_row['state']))

if __name__ == '__main__':
    unittest.main()
