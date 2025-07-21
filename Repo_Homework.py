# import pickle
#
# with open('data.pkl', 'rb') as f:
#     odd_numbers = pickle.load(f)
#
# div = [num for num in odd_numbers if num % 3 == 0]
#
# average = sum(div) / len(div)
# print(average)



# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
#
# dict_2 = {}
#
# for value in dict_1.values():
#     dict_2[value] = len(value)
#
# print(dict_2)




dict = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
def dict_func(d):
    for k, v in d.items():
        d[k] = [i for i in v if i % 2 == 1]
    return d

dict_func(dict)
