from jikanpy import Jikan
from pprint import pprint
import time

jikan = Jikan()


def main():
    #mushishi = jikan.anime(457, extension="pictures")
    top_anime = jikan.top(type="anime", page=1, subtype="upcoming")

    id_list = get_id(top_anime)
    shows = get_anime_object(id_list)
    print_table(shows)


def get_id(data):
    anime_access = data['top']
    id_list = []

    #Only use 25 of the 50 ID
    for container in anime_access[:25]:
        identification = container['mal_id']
        id_list.append(identification)

    return id_list


def get_anime_object(data):
    anime_list = []

    #API RULES: 30 Requests/Minute
    for id in data:
        #API RULES: 4 Seconds between requests
        time.sleep(4)
        show = jikan.anime(id)
        title = show['title']
        genres = []
        for genre in show['genres']:
            genres.append(genre['name'])

        anime_list.append({"Title": title, "Genres": genres})

    return anime_list


def print_table(list):
    max_length = 0
    for anime in list:
        current_length = len(anime['Title'])
        if current_length > max_length:
            max_length = current_length


    print("Title" + max_length*' ' + "Genre")
    spaces = 3 + max_length
    for anime in list:
        distance = spaces - len(anime['Title'])
        print(anime['Title'], distance*' ', anime['Genres'])


main()

