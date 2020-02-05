from time import ctime

def get_number_input(prompt):
    value = None
    while type(value) != float:
        try:
            value = float(input(prompt))
            return value    
        except KeyboardInterrupt:
           exit()
        except ValueError as e:
            print('Invalid Input')
            print(ctime(), e, file = ERROR_FILE)
        


def main():
    while True:
        client_name = input('What is the customers\'s name?: ')
        if not client_name:
            break

        while True:
            product_name = input('What is the product\'s name?: ')
            if not product_name:
                break

            product_qty = get_number_input(f'how many {product_name} was purchased?: ')

            product_price = get_number_input(f'how much is {product_name}?: ')
            
            print(f'THIS {client_name} {product_name} {product_qty} {product_price}', file = REGISTER)

if __name__ == '__main__':
    # superGlobal
    ERROR_FILE = open('error_log.txt', 'a')
    REGISTER = open('register.txt', 'a')

    main()

    ERROR_FILE.close()
    
