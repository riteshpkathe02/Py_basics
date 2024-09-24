stocks = {"info":[600,630,620], "ril":[1430,1490,1567], "mtl":[234,180,160]}
import statistics as st
def print_all():
    for k,v in stocks.items():
        print(f"{k}==>{v}==>avg: ",st.mean(v))

def add():
    stock = input("Enter the stock ticker to add: ")    
    prices = input("Enter prices of the stock")
    prices=float(prices)

    if stock in stocks:
        stocks[stock].append()
    else:
        stocks[stock]=[prices]
    print_all()

def main():
    op = input("Enter operation(print, add): ")
    if op.lower()=='add':
        add()
    elif op.lower()=='print':
        print_all()
    else:
        print("Invalid Action")    

if __name__=='__main__':
    main()