from data_frame_reader import DataFrameReader

def main():
    print("Please specify file directory.")
    df_path = input()
    data_reader = DataFrameReader()

    original_df = data_reader.get_df(df_path)

    movie_count = data_reader.get_movie_count(original_df)
    movie_ratings = data_reader.get_average_movie_ratings(original_df)
    top_rated_movies = data_reader.get_top_rated_movies(original_df)
    movies_by_year = data_reader.get_movies_released_by_year(original_df)
    movies_by_genre = data_reader.get_movies_by_genre(original_df)

    print('''Please, select one of the options below (1-7): \n
            1. Print the number of movies in the dataset. \n
            2. Print the average rating of all the movies. \n
            3. Print the top 5 highest rated movies. \n
            4. Print the number of movies released each year. \n
            5. Print the number of movies in each genre. \n
            6. Save the dataset to a JSON file. \n
            7. Exit the program.''')


    while True:
        try:
            answer_string = int(input())
            assert 1 <= answer_string <= 7

            if answer_string == 1:
                print(movie_count)
            elif answer_string == 2:
                print(movie_ratings)
            elif answer_string == 3:
                print(top_rated_movies)
            elif answer_string == 4:
                print(movies_by_year)
            elif answer_string == 5:
                print(movies_by_genre)
            elif answer_string == 6:
                try:
                    print("Please add a directory for storing your JSON file.")
                    json_path = input()

                    print('''Please select which Data Frame you would like to store in .json file (1-5):
                    1. Original Data Frame.
                    2. The Average movie ratings Data Frame.
                    3. The Five top rated movies Data Frame.
                    4. The Movies released by year Data Frame.
                    5. The Movies realeased by genre Data Frame.''')

                    input_for_download = int(input())
                    assert 1 <= input_for_download <= 5 


                    if input_for_download == 1:
                        data_reader.store_df_to_json(original_df, json_path)
                    elif input_for_download == 2:
                        data_reader.store_df_to_json(movie_ratings, json_path)
                    elif input_for_download == 3:
                        data_reader.store_df_to_json(top_rated_movies, json_path)
                    elif input_for_download == 4:
                        data_reader.store_df_to_json(movies_by_year, json_path)
                    elif input_for_download == 5:
                        data_reader.store_df_to_json(movies_by_genre, json_path)
                except:
                    print("Sorry, please choose a value between 1 and 5 to download your JSON file.")

            elif answer_string == 7:
                break
        except:
            print("Sorry, please choose a value between 1 and 7")
            continue

if __name__ == "__main__":
    exit(main())
