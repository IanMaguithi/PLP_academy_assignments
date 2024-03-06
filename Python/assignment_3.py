def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        price = price * 0.8
        return price
    else:
        return price
    
if __name__ == "__main__":
    price = int(input("Enter the price: "))
    discount_percent = int(input("Enter the discount percent: "))
    print(calculate_discount(price, discount_percent))  
