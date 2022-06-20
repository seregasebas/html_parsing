import json

def get_info_about_group(name_group, name_group_discription):
    return name_group.a.text, name_group.a.get('href'), name_group_discription.p.text

def get_info_all_group_on_the_page(name_group, name_group_discription, domain):
    name_artis = []
    url_artist = []
    discription_artis = []
    for i in range(len(name_group)):
        #Исключаем пустые значения(их всего 2)
        try:
            name, url_art, discrip = get_info_about_group(name_group[i], name_group_discription[i])
            name_artis.append(name)
            url_artist.append(domain+str(url_art).replace(' ', '+'))
            discription_artis.append(discrip)
        except AttributeError:
            print(f'{name_group[i]} {name_group_discription[i]}')
    return name_artis, url_artist, discription_artis


def create_dict(name_artis, url_artist, discription_artis):
    dict_res = {'rock':[{} for i in range(len(name_artis))]}
    for i in range(len(dict_res['rock'])):
        dict_res['rock'][i]['name'] = name_artis[i]
        dict_res['rock'][i]['url'] = url_artist[i]
        dict_res['rock'][i]['discription'] = discription_artis[i]
    return dict_res

def save_file(new_dict):
    with open("rock_groups.json", "w") as write_file:
        json.dump(new_dict, write_file, ensure_ascii=False)