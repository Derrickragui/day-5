

productdetails=     [{"Name": "Omo 2kg", "Price": 200 ,"Description":"White"},
                     {"Name": "Sugar 1kg","Price":120,"Description":"Kabras"},
                     {"Name":"Kiwi","Price": 100,"Description":"Black"},
                     {"Name":"Teabags","Price": 150,"Description":"Ketepa"}]

for products in productdetails:
    exclusiveprice = float (products['Price'])
    vatTax = 0.16
    inclusivePrice = exclusiveprice+exclusiveprice*vatTax

    print(products['Name'],inclusivePrice,products['Description'])
    

