import pandas as pd
import unittest

from movie_reader.data_frame_reader import DataFrameReader
from pandas.testing import assert_frame_equal 


class TestDataFrameReader(unittest.TestCase):

    def setUp(self):
        self.test_df_path = "movie_reader_unittests/test_samples/test_sample.csv"
        self.test_fake_path = "/fake_path.csv"
        self.test_df = pd.read_csv(self.test_df_path)
        self.data_reader = DataFrameReader()


    def test_get_df(self):
        '''Test if get_df function, logs correct information if a valid directory is given'''
        with self.assertLogs() as captured:
            self.data_reader.get_df(self.test_df_path)
            self.assertEqual(len(captured.records), 3)
            self.assertEqual(captured.records[0].getMessage(), "Fetching data...")
            self.assertEqual(captured.records[1].getMessage(), "Cleaning NaN values...")
            self.assertEqual(captured.records[2].getMessage(), "Successfully retrieved data.")


    def test_get_df_invalid_path(self):
        '''Test if get_df function, logs correct information if a invalid directory is given'''
        with self.assertLogs() as captured:
            self.data_reader.get_df(self.test_fake_path)
            self.assertEqual(len(captured.records), 2)
            self.assertEqual(captured.records[0].getMessage(), "Fetching data...")
            self.assertEqual(captured.records[1].getMessage(), "Not a valid directory.")


    def test_get_movie_count(self):
        '''Test if get_movie_count function returns expected result and logs correct statements'''
        test_count = 10

        with self.assertLogs() as captured:
            self.assertEqual(test_count, self.data_reader.get_movie_count(self.test_df))
            self.assertEqual(len(captured.records), 2)
            self.assertEqual(captured.records[0].getMessage(), "Fetching data...")
            self.assertEqual(captured.records[1].getMessage(), "Successfully retrieved movie count.")


    def test_get_average_movie_ratings(self):
        '''Test if get_average_movie_ratings function returns expected result and logs correct statements'''
        exp_df = pd.read_csv("movie_reader_unittests/test_samples/test_avg_movie_ratings.csv")

        with self.assertLogs() as captured:
            assert_frame_equal(exp_df, self.data_reader.get_average_movie_ratings(self.test_df))
            self.assertEqual(len(captured.records), 2)
            self.assertEqual(captured.records[0].getMessage(), "Fetching data...")
            self.assertEqual(captured.records[1].getMessage(), "Successfully retrieved data.")


    def test_get_top_rated_movies(self):
        '''Test if get_top_rated_movies function returns expected result and logs correct statements'''
        exp_df = pd.read_csv("movie_reader_unittests/test_samples/test_top_rated_movies.csv")

        with self.assertLogs() as captured:
            assert_frame_equal(exp_df, self.data_reader.get_top_rated_movies(self.test_df).reset_index(drop=True))
            self.assertEqual(len(captured.records), 4)
            self.assertEqual(captured.records[0].getMessage(), "Fetching data...")
            self.assertEqual(captured.records[1].getMessage(), "Fetching data...")
            self.assertEqual(captured.records[2].getMessage(), "Successfully retrieved data.")
            self.assertEqual(captured.records[3].getMessage(), "Successfully retrieved top rated movies.")



if __name__ == "__main__":
    unittest.main()