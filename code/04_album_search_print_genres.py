"""
Script takes a list of genres, a list of search terms and return n albums that contain that text.
Albums are ranked in order of
Inputs:
    Genre list, case agnostic
    Search term - text, case agnostic
    Number of albums to return
Output:
    Print of dataframe containing relevant albums with relevant text snippets.
"""


import pandas as pd

def read_ra_reviews(file_in="C:/code/music_nlp/data/reviews.csv"):
    df = pd.read_csv(file_in,
                    header=None)
    df = df.iloc[:, 1:6]
    df.columns = ['artist','album','rating','genre','text']
    df['id'] = df.reset_index().index
    return(df)

def get_top_albums(album_df, num_albums):
    album_df = album_df.sort_values(by='rating', axis=0, ascending=False)
    return(album_df.iloc[0:(num_albums), :])

def return_relevant_sentences(text_input, search_term_list):
    relevant_sentences = []
    for term in search_term_list:
        relevant_sentences.append([x for x in text_input.split(". ") if term in x])
    return(relevant_sentences)

def string_to_list(string_in):
    if string_in == '':
        return([])
    else:
        list_out = string_in.split(",")
        list_out = [x.strip() for x in list_out]
        return(list_out)

df = read_ra_reviews()

# Print allowable genre values
df['genre_list'] = [string_to_list(x) for x in df['genre']]
all_genres = [item for x in df['genre_list'] for item in x]
print('Allowable genres:\n')
print(set(all_genres))

# To Do
# Add these as parameters
genre_list = input('\nEnter genres separated by commas. Will return albums that are in all genres inputted:')
search_terms = input('\nEnter search terms separated by commas. Will return albums that contain all search terms:')
num_albums_to_returns = int(input('\nEnter number of albums to return:'))

genre_list_split = string_to_list(genre_list)
search_term_list = string_to_list(search_terms)

result = df.copy()

if len(genre_list_split) > 0:
    for term in genre_list_split:
        result = result.loc[result['genre'].str.contains(term, case=False)]

if len(search_term_list) > 0:
    for term in search_term_list:
        result = result.loc[result['text'].str.contains(term, case=False)]

result = get_top_albums(result, num_albums_to_returns)

result['relevant_sentences'] = [return_relevant_sentences(x, search_term_list) for x in result['text']]

pd.options.display.max_colwidth = 200
print(result.loc[:, ['artist','album','rating','genre','relevant_sentences']].to_string())

# Tasks
# Done - Return relevant sentences
# Done - Return top three relevant albums
# Done - Input a list of search terms and genres
# Done - Search by genre
