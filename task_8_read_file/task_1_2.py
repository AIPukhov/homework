def food_catalog(file_name):
    cook_book = {}
    with open(file_name) as file_object:
        for line in file_object:
            shop_name = line.strip()
            ingredients = []
            for _ in range(int(file_object.readline())):
                ingredients_tmp = file_object.readline().split('|')
                dict_tmp = dict(ingredient_name=ingredients_tmp[0].strip(),
                                quantity=int(ingredients_tmp[1].strip()),
                                measure=ingredients_tmp[2].strip())
                ingredients.append(dict_tmp)
            cook_book[shop_name] = ingredients
            file_object.readline()
    return cook_book


cook_book = food_catalog('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for item in cook_book[dish]:
            key = item['ingredient_name']
            measure = item['measure']
            quantity = item['quantity'] * person_count
            if key in result:
                result[key]['quantity'] += quantity
            else:
                result[key] = {'measure': measure, 'quantity': quantity}
    return result


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1))
print(get_shop_list_by_dishes(['Омлет'], 2))
