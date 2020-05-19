from jikanpy import Jikan
from pprint import pprint
import time

jikan = Jikan()


def main():
    # Test Code line 10 - 33
    our_list = [{'Genres': ['Drama', 'Romance', 'School', 'Shoujo Ai'],
                 'Title': 'Citrus'},
                {'Genres': ['Action', 'Adventure', 'Comedy', 'Super Power', 'Supernatural', 'Shounen'],
                 'Title': 'Bleach'},
                {'Genres': ['Comedy', 'Ecchi', 'Romance', 'School', 'Seinen'], 'Title': 'Prison School'}]

    top_anime = jikan.top(type="anime", page=1, subtype="upcoming")
    id_list = get_id(top_anime)
    upcoming_shows = get_anime_object(id_list)

    recommendations = recommended_list(our_list, upcoming_shows)

    print('*************Watched Shows************')
    print_table(our_list)
    print()

    print('*************Upcoming Shows************')
    print_table(upcoming_shows)
    print()

    print('*************Recommended Based Off of Our List************')
    print_table(recommendations)
    print()


def get_id(data):
    anime_access = data['top']
    id_list = []

    # Only use 25 of the 50 ID
    for container in anime_access[:25]:
        identification = container['mal_id']
        id_list.append(identification)

    return id_list


def get_anime_object(data):
    anime_list = []

    # API RULES: 30 Requests/Minute
    for id in data:
        # API RULES: 4 Seconds between requests
        time.sleep(4)
        show = jikan.anime(id)
        title = show['title']
        genres = []
        for genre in show['genres']:
            genres.append(genre['name'])

        anime_list.append({"Title": title, "Genres": genres})

    return anime_list


def print_table(list_of_anime):
    max_length = 0
    for anime in list_of_anime:
        current_length = len(anime['Title'])
        if current_length > max_length:
            max_length = current_length

    print("Title" + max_length*' ' + "Genre")
    spaces = 3 + max_length
    for anime in list_of_anime:
        distance = spaces - len(anime['Title'])
        print(anime['Title'], distance*' ', anime['Genres'])


def recommended_list(our_list, top_anime):
    genre_list = []
    for anime in our_list:
        genre_list.append(anime['Genres'])

    flattened_list = [genre for item in genre_list for genre in item]  # Removes nested lists
    flattened_list = list(dict.fromkeys(flattened_list))  # Removes duplicate genres

    recommendation = []
    flattened_list = set(flattened_list)  # Creates a set
    for item in top_anime:
        if set(item['Genres']) & flattened_list and\
        (number_of_matches(set(item['Genres']), set(flattened_list)) > 1):  # If both lists intersect and have
                                                                            # more than 1 similar genre
            recommendation.append(item)

    return recommendation


def number_of_matches(list_one, list_two):
    num = 0
    for x in list_one:
        if x in list_two:
            num += 1
    return num

main()

