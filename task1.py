import os
grocery = []

def clear():
    os.system('clear')

def add_product():
    clear()
    flag = 0
    while flag == 0:
        try:
            id_no = int(input('Enter the ID: '))
            name = input('Enter the grocery item: ')
            uom = input('Enter the unit of measurement: ')
            price = int(input('Enter the price per KG: '))
            currency = input('Currency: ')
            quantity = int(input('Enter the quantity: '))
            weight = int(input('Enter the weight: '))
            normalized_price = float(input('Minimum price: '))
            normalized_uom = input('Minimum unit of measurement(eg:gm): ') 
            variety = input('Enter the specific verity: ')
            country_of_origin = input('Enter the country_of_origin: ')
            stock_item = input('Enter the stock item: ')
            total_quantity = int(input('Enter the total quantity: '))
            stock_weight = int(input('Enter the stock weight: '))
            brand_name = input('Enter the brand name: ')
            categories = input('Enter the category: ')
            flag = 1
        except:
            print('Invalid character, please enter valid character')
            
        grocery_dict = {
            'id_no':id_no,
            'name':name,
            'uom':uom,
            'price':price,
            'currency':currency,
            'quantity':quantity,
            'weight':weight,
            
            'normalized':{
            'normalized_price':normalized_price,
            'normalized_uom':normalized_uom
            },
            'variety':variety,
            'country_of_origin':country_of_origin,
            
            'stock':{
            'stock_item':stock_item,
            'total_quantity':total_quantity,
            'stock_weight':stock_weight
            },
            'brand_name':brand_name,
            'categories':[categories]
        }
        grocery.append(grocery_dict)
        print(grocery)
        
def display_stock():
    clear()
    print('GROCERY DATA')
    for i in grocery:
        print(f"{i['name']} : {i['price']} : ")





def main():
    clear()
    while True:
        print('\nOptions')
        print('1.Add product: ')
        print('2.display stock')
        print('3.Quit')
    
        choice = int(input('Enter the choice: '))
        
        if choice == 1:
            add_product()
        elif choice == 2:
            display_stock()
        elif choice == 3:
            break
        else:
            print('Choose correct option')
        
        

if __name__ == "__main__":
    main()