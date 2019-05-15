
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28

### TODO: Declare the Pants Class 

### TODO: write an __init__ function to initialize the attributes

### TODO: write a change_price method:
#    Args:
#        new_price (float): the new price of the shirt
#    Returns:
#        None

### TODO: write a discount method:
#    Args:
#        discount (float): a decimal value for the discount. 
#            For example 0.05 for a 5% discount.
#
#    Returns:
#        float: the discounted price
class Pants:
    def __init__(self, pant_color, pant_waist_size, pant_length, pant_price):
        self.color = pant_color
        self.waist_size = pant_waist_size
        self.length = pant_length
        self.price = pant_price

    def change_price(self, new_price):
        self.price = float(new_price)
        
    def discount(self, discount):
        return float(self.price * (1 - discount))

def main():
    new_pant = Pants('red',8,27,9.28)
    print(new_pant.color)
    print(new_pant.waist_size)
    print(new_pant.length)
    print(new_pant.price)

if __name__ == "__main__":
    main()