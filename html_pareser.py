import requests
from bs4 import BeautifulSoup
import functions

domain = 'https://www.last.fm/'
url = 'ru/tag/rock/artists'
page_str = '?page='
page_number = 1

name_group_res = []
url_group = []
discrition_group = []

for i in range(1,49):
    print(f'страница {page_number}. Осталось пропарсить {48 - page_number} стр.')
    url_parsing = domain+url+page_str+str(page_number)
    response = requests.get(url_parsing)
    #создаем суп
    soup = BeautifulSoup(response.text, 'html.parser')
    # Поиск по классу -берем название групп и ссылку
    name_group = soup.find_all('h3', class_='big-artist-list-title')
    # Поиск по классу -берем описание
    name_group_discription = soup.find_all('div', class_='big-artist-list-bio')
    #создаем списки из названий, ссылок и описаниий
    name_artist, url_artist, discription_artis = functions.get_info_all_group_on_the_page(name_group, name_group_discription, domain, url)
    #конкантинируем в финальные словари
    name_group_res += name_artist
    url_group += url_artist
    discrition_group += discription_artis    
    #Увеличиваем страницу
    page_number += 1

#создаем словарь для записи в файл
rock_dict = functions.create_dict(name_group_res, url_group, discrition_group)
#запись в файл
functions.save_file(rock_dict)