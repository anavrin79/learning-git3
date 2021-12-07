shopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]

def get_index_1_tuple_element(given_tuple):
    """
    Stworzona po to aby pokazac jak działa lambda, robi ona to samo co wyrażenie lambda poniżej, czyli tak na prawdę wskazuje po którym elemencie krotki należy posortować listę krotek ...
    """
    return given_tuple[1]

sorted_items = sorted(shopping_items, key=get_index_1_tuple_element)
print(sorted_items)

#sortowanie - użyciem wyrażenia lambda
sorted_items = sorted(shopping_items, key=lambda given_tuple: given_tuple[0])
print(sorted_items)
help(get_index_1_tuple_element)