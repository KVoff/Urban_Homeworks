class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'Product_7_1.txt'
    def get_products(self):

        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                products = file.read()
            return products
        except FileNotFoundError:
            return ''

    def add(self, *products):
        list_products = self.get_products().split('\n')

        list_products_names = set()
        for i in list_products:
            product_name = i.split(', ')[0]
            list_products_names.add(product_name)


        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for i in products:
                if i.name in list_products_names:
                    print(f'Продукт {i.name} уже сть в магазине')
                else:
                    file.write(str(i) + '\n')
                    list_products_names.add(i.name)





s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)
print(s1.get_products())
