"""
Test Code	                                            Output
catalogue = Catalogue("Furniture")                      ["Chair", "Carpet"]
catalogue.add_product("Sofa")                           Items in the Furniture catalogue:
catalogue.add_product("Mirror")                         Carpet
catalogue.add_product("Desk")                           Chair
catalogue.add_product("Chair")                          Desk
catalogue.add_product("Carpet")                         Mirror
print(catalogue.get_by_letter("C"))                     Sofa
print(catalogue)
"""
class Catalogue:

    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name):
        self.product_name = product_name
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter):
        self.list = [idx for idx in Catalogue.products if idx[0].lower() == first_letter.lower()]
        #self.list = [idx for idx in self.products if idx.startswith(first_letter)]
        return self.list

    def __repr__(self):
        joined_string = '\n'.join(sorted(Catalogue.products))
        return f"Items in the {self.name} catalogue:\n{joined_string}"

"""
        def __repr__(self):
        result = ''
        joined_string = "\n".join(sorted(self.products))
        result += f"Items in the {self.name} catalogue:\n{joined_string}"
        return result
"""

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)