"""
Test Code	                                    Output
inventory = Inventory(2)                        not enough room in the inventory
inventory.add_item("potion")                    2
inventory.add_item("sword")                     Items: potion, sword.
print(inventory.add_item("bottle"))             Capacity left: 0
print(inventory.get_capacity())
print(inventory)
"""
class Inventory:

    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        current_capacity = len(self.items) - self.__capacity
        return f"Items: {', '.join(self.items)}.\nCapacity left: {current_capacity}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
