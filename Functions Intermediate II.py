
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
sports_directory['soccer'][1]='Sami'
students[2]['last_name']='Daraghmeh'
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

print("Updated Values:")
print("x:", x)  
print("students:", students)  
print("sports_directory:", sports_directory)  
print("z:", z)  

def iterateDictionary(some_list):
    print("\nIterating through students:")
    for dictionary in some_list:
        output = ', '.join([f"{key} - {value}" for key, value in dictionary.items()])
        print(output)

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    print(f"\nValues for key '{key_name}':")
    for dictionary in some_list:
        print(dictionary[key_name])

iterateDictionary2('first_name', students)  
iterateDictionary2('last_name', students)   


def printInfo(some_dict):
    print("\nPrinting info from dojo:")
    for key, values in some_dict.items():
        print(f"{len(values)} {key.upper()}")
        for value in values:
            print(value)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
