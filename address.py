book={} #Created empty dictionary
book['Rohanyaa'] = {
    'name':'Rohan',
    'address':'Solapur',
    'phone':98789263
}
book['Tushyaa'] = {
    'name':'Tushar',
    'address':'Nagar',
    'phone':987892654
}

import json
s=json.dumps(book)

with open(r"C:\Users\PC1\Desktop\Python_Basics\book.txt","w") as f:
    f.write(s)