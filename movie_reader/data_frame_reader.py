from ast import literal_eval

import logging
import pandas as pd

logging.basicConfig(level = logging.INFO)


class DataFrameReader:
    
    
    def get_df(self, csv_path):
        '''
        This function returns the specified csv file as a Data Frame with no NaN values
        Parameters:
                csv_path (str)
        Returns:
                result (DataFrame)
        '''
        try:
            logging.info("Fetching data...")
            result = pd.read_csv(csv_path)
            logging.info("Cleaning NaN values...")
            result = result.dropna()
            logging.info("Successfully retrieved data.")

            return result

        except FileNotFoundError:
            logging.error("Not a valid directory.")
        except Exception as error:
            logging.error(f"An error occurred: {error}")


    def get_movie_count(self, df):
        '''
        This function returns a count of all unique IDs in the given DataFrame
        Parameters:
                df (DataFrame) 
        Returns: 
                result (int): number of unique IDs
                
        '''
        try:
            logging.info("Fetching data...")
            result = df["id"].nunique()
            logging.info("Successfully retrieved movie count.")

            return result

        except Exception as error:
            logging.error(f"An error occurred: {error}")


    def get_average_movie_ratings(self, df):
        '''
        This function returns a data set of the movie titles and their average voting
        Parameters:
                df (DataFrame) 
        Returns: 
                result (DataFrame): a Data Frame containing "original_title" and "vote_average"
                
        '''
        try:
            logging.info("Fetching data...")
            df_average_rating = pd.DataFrame(df[["original_title", "vote_average"]])
            logging.info("Successfully retrieved data.")

            return df_average_rating
        
        except Exception as error:
            logging.error(f"An error occurred: {error}")


    def get_top_rated_movies(self, df):
        '''
        This function returns a data set of the top 5 rated movies
        Parameters:
                df (DataFrame) 
        Returns: 
                result (DataFrame): a Data Frame containing the top 5 rated movies from the input DataFrame
                
        '''
        try:
            logging.info("Fetching data...")
            df_average_rating = self.get_average_movie_ratings(df)
            result = df_average_rating.sort_values("vote_average", ascending=False).head(5)
            logging.info("Successfully retrieved top rated movies.")

            return result
        
        except Exception as error:
            logging.error(f"An error occurred: {error}")


    def get_movies_released_by_year(self, df):
        '''
        This function returns a data set of the number of movies released each year
        Parameters:
                df (DataFrame) 
        Returns: 
                result (DataFrame): a Data Frame containing "release_year" and the number of movies released
                
        '''
        try:
            logging.info("Fetching data...")
            df["release_year"] = pd.to_datetime(df["release_date"])
            result = df["release_year"].dt.year.value_counts()
            logging.info("Successfully retrieved release year data.")
            result = result.to_frame()

            return result
        
        except Exception as error:
            logging.error(f"An error occurred: {error}")


    def get_movies_by_genre(self, df):
        '''
        This function returns a data set of the number of movies in each genre
        Parameters:
                df (DataFrame) 
        Returns: 
                result (DataFrame): a Data Frame containing "name" and the number of movies in each genre
                
        '''
        try:
            logging.info("Fetching data...")
            list_df = df["genres"].map(literal_eval)
            exploded_df = list_df[list_df.str.len() > 0].explode()
            genre_df = pd.DataFrame(list(exploded_df), index=exploded_df.index)
            logging.info("Successfully retrieved data.")
            result = genre_df.name.value_counts()
            logging.info("Successfully sorted data by genre.")
            result = result.to_frame()

            return result
        
        except Exception as error:
            logging.error(f"An error occurred: {error}")



    def store_df_to_json(self, df, json_path):
        '''
        This function returns and stores the Data Frame to the specified location as a json file.
        Parameters:
                df (DataFrame) 
                json_path (str)
        '''
        try:
            logging.info("Fetching data...")
            df.to_json(json_path)
            logging.info(f"Successfully stored data to .json file at: {json_path}.")
        
        except Exception as error:
            logging.error(f"An error occurred: {error}")
