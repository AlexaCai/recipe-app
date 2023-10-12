class ShoppingList(object):
    # Method to create a list
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    # Method to add an item to the list and ensure a same item doesn't get added twice
    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
        else:
            print("You tried to add " + item + " in the list, but this item is already in it, so has not been added again")

    # Method to remove an item from the list
    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)

    # Method to view item(s) in the list
    def view_list(self):
        print("--------------")
        print(self.list_name + " contains the following items:")
        for item in self.shopping_list:
            print(item)


# Create an object
pet_store_list = ShoppingList("Pet Store Shopping List")

# Add items to the shopping list
pet_store_list.add_item("dog")
pet_store_list.add_item("food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Remove an item from the shopping list
pet_store_list.remove_item("flea collars")

# Add "frisbee" again to the shopping list to ensure it won't be added twice in the list (test)
pet_store_list.add_item("frisbee")

# View the entire shopping list
pet_store_list.view_list()
