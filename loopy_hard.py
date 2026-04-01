import re


def market_revenue(transactions):

    total = 0
    
    for i in transactions:
        if not i:
            total = 0
        else:
            total +=(i[1]*i[2])

    # TODO: calculate total revenue

    return total


def longest_unique_word(sentence):

    # TODO
   
    return sorted(sentence.split(), key=len)[-1] if sentence != '' else ''
    
    # return ''.join([word for word in sentence.split() if len(word) == max(len(word) for word in sentence.split())])




def two_sum(nums, target):
    import random
    # TODO
    num1 = random.choice(nums)
    num2 = random.choice(nums)
    while num1+ num2 != target:
        num1 = random.choice(nums)
        num2 = random.choice(nums)
    else:
        return [nums.index(num1),nums.index(num2)] if nums.index(num1) < nums.index(num2) else [nums.index(num2),nums.index(num1)] 
        
    
        


def peak_temperatures(temps):

    

    # TODO

    return [element for index,element in enumerate(temps) if index < (len(temps)-1) and temps[index-1]<element>temps[index+1]]


def email_filter(emails):

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    valid = []
    invalid = []

    # TODO

    for email in emails:
        if re.search(pattern,email):
            valid.append(email)
        else:
            invalid.append(email)
    return {
        "valid": valid,
        "invalid": invalid
    }


def stock_profit(prices):

    # TODO
    return max(prices[prices.index(min(prices)):])-min(prices)


def inventory_projection(stock, daily_sales):

    # TODO
    for index, element in enumerate(daily_sales,1):
        stock -=element
        if stock <= 0:
            return f'Inventory will run out on day {index}.'
    return f"Inventory lasts entire period. Remaining stock: {stock}"