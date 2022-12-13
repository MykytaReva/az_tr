from bs4 import BeautifulSoup
import lxml
# import os
# path = os.getcwd()
# print(path)

with open('app/templates/base.html') as file:
    body = file.read()

soup = BeautifulSoup(body, 'lxml')

title = soup.title
# print(title)
# print(title.name)
# print(title.getText())

p = soup.p
# print(p)

first_div = soup.find('div')
# print(first_div.getText())

all_divs = soup.find_all('div')
for i in all_divs:
    # print('-------')
    # print(i)
    pass

# first_movie = soup.find('div', class_='movie')
first_movie = soup.select('.movie')[0]
# print(first_movie)
# all_movies = soup.find_all('div', class_='movie')
all_movies = soup.select(selector='.movie')
# print(all_movies)

links = soup.find_all('a')
# for link in links:
#     print(link)
#     print(link.getText())
#     print(link.get('href'))
#
#     print('----------')

movie_box = soup.select_one('#movie-box')
# print(movie_box)
# print(movie_box.getText())

parent = movie_box.parent
# print(parent)
child = movie_box.children
# print(child)
# for i in child:
#     print('===========')
#     print(i)

movie = soup.find('div', class_='movie')
parent = movie.find_parent()
# print(parent)
parent = movie.find_parent('div')

interstellar = soup.find(text='Interstellar')
print(interstellar)
print(interstellar.find_parent('div'))
print(interstellar.find_parent('a'))