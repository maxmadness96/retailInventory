import os
import datetime
import retail_item

# Displays the current user's directory using os module
print("Programmer:", os.environ['USERPROFILE'])

# Displays current date and time
this_date = datetime.datetime.now()
current_time = this_date.strftime('%H:%M:%S')
current_date = this_date.strftime('%b %d, %Y')
print(current_date, '@', current_time)
print(' ')


def main():
    item_1 = retail_item.Retail("Jacket", "12", "$59.95")
    item_2 = retail_item.Retail("Designer Jeans", "40", "$34.95")
    item_3 = retail_item.Retail("Shirt", "20", "$24.95")

    # Retail item 1
    print('Retail Item 1: ')
    print(f'Description:  {item_1.get__item()}')
    print(f'Units in Inventory:  {item_1.get__units()}')
    print(f'Price:  {item_1.get__price()}\n')

    # Retail Item 2
    print('Retail Item 2: ')
    print(f'Description:  {item_2.get__item()}')
    print(f'Units in Inventory:  {item_2.get__units()}')
    print(f'Price:  {item_2.get__price()}\n')

    # Retail Item 3
    print('Retail Item 3: ')
    print(f'Description:  {item_3.get__item()}')
    print(f'Units in Inventory:  {item_3.get__units()}')
    print(f'Price:  {item_3.get__price()}')


if __name__ == '__main__':
    main()
