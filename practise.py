import csv

products={}

class prac:

    def p_add(self):
        id=input("Enter p_id: ")
        name=input("Enter p_name: ")
        price=input("Enter p_price: ")
        products[id]={"name":name, "price":price}
        return print(f"{id}:", products[id])
    
    def p_list(self):
        print("product list: ")

        for id,product in products.items():
            print(f"id: {id}, name: {product['name']}, price: {product['price']}")
        
    def p_del(self):
        id=input("Enter p_id to delete: ")

        if id in products:
            del products[id]
            print("Product deleted successfully")

        else:
             print("Product not found" )
    
    def p_update(self):
        id=input("Enter p_id for update: ")

        if id in products:
            products[id]['name']=input("Enter new name for update :")
            products[id]['price']=input("Enter new price for update :")
            print("Successfully updated")

        else:
            print("Product not found" )

    def p_csv(self):

        try:
            with open('products.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['id', 'name', 'price'])

                for id, product in products.items():
                    writer.writerow([id, product['name'], product['price']])
                    
            print("Products saved to 'products.csv'")
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}")

    
p1=prac()
print("1:product_add")
print("2:product_list")
print("3:product_delete")
print("4:product_update")
print("5:product_CSV")
print("6:for exit")
while True:
    x = int(input("C1hose 1 option BT 1 to 5: "))
    if x == 1:
        p1.p_add()

    elif x == 2:
        p1.p_list()

    elif x == 3:
        p1.p_del()

    elif x == 4:
        p1.p_update()

    elif x == 5:
            p1.p_csv()

    elif x >= 6:
            print("invalid option")
            break
        
         