import requests


def superheroes(superheroes_list):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    input_dict = response.json()
    output_dict = {}
    for name in superheroes_list:
        for i in range(len(input_dict)):
            if input_dict[i]['name'] == name:
                output_dict[input_dict[i]['powerstats']['intelligence']] = input_dict[i]['name']
    return f'Самый умный супергерой: {output_dict[max(output_dict.keys())]}, intelligence = {max(output_dict.keys())}'


my_superheroes = ['Hulk', 'Captain America', 'Thanos']

print(superheroes(my_superheroes))