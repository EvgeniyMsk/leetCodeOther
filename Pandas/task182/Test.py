import unittest

import numpy as np

import Solution
import pandas as pd


solution = Solution.solution


class TaskTest(unittest.TestCase):
    def test(self):
        data = {
            'id': [1, 2, 3],
            'email': ['a@b.com', 'c@d.com', 'a@b.com']
        }
        dataFrame = pd.DataFrame(data)

        expectedData = {
            'id': [1],
            'email': ['a@b.com']
        }

        expectedDataFrame = pd.DataFrame(expectedData)
        np.testing.assert_array_equal(solution.duplicate_emails(dataFrame), expectedDataFrame[['email']])




