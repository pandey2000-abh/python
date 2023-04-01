def enter_product():
    buyingData={}
    enterDetails=True
    while enterDetails:
        details = input("press A to add product and Q to quite: ")
        if details=='A':
            product = input("enter product:")
            quantity = int(input("enter the quantity:"))
            buyingData.update({product:quantity})
        elif details == 'Q':
            enterDetails =False
        else:
            print("please select a correct option")
    return buyingData
    
    def getPrice(product,quantity):
    priceData={
        'Biscuit':3,
        'Bread':2,
        'Apple':3,
        'onion':3,
        'Coke':3
    }
    subtotal = priceData[product]*quality
    print(product+ ':$' +str(priceData[product])+ 'x' +str(quality)+ '=' +str(subtotal))
    return subtotal
    
    def getDiscount(billAmount,membership):
    discount = 0
    if billAmount >=25:
        if membership == 'Gold':
            billAmount = billAmount*0.80
            discount = 20
        elif membership == 'Silver':
            billAmount = billAmount*0.90
            discount = 10
        elif membership == 'Bronze':
            billAmount = billAmount*0.95
            discount = 5
            print(str(discount)+'% off for'+membership+"membership on total amount:$"+str(billAmount))
        else:
            print("no discount on amount less than $25")
    return billAmount
    
    def makeBill(buyingData,membership):
    billAmount = 0
    for key,value in buyingData.items():
        billAmount += getPrice(key,value)
        billAmount = getDiscount(billAmount,membership)
        print("The discount amount is $" +str(billAmount))
        
buyingData = enter_product()
membership = input("Enter customer membership: ")
makeBill(buyingData,membership)
        
