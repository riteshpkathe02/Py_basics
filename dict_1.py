pop =  {"china": 143, "india":136, "usa": 32, "pak":21}

def print_all():
    for country, p in pop.items():
        print(f"{country}==>{p}")

def add():
    country = input("Enter country name to add : ")
    country = country.lower() #lowercase the string
    if country in pop:
        print("Country already exists in dataset. Terminating")
        return
    
    p = float(input(f"Enter the population for {country}"))
    pop[country]=p #Adds new key-value pair to dicionary
    print_all()

def remove():
    country = input("Enter country name to remove : ")
    country = country.lower() #lowercase the string
    if country not in pop:
        print("Country doesn't exist in dataset. Terminating")
        return
    del pop[country]
    print_all()

def query():
    country = input("Enter country name to search : ")
    country = country.lower() #lowercase the string
    if country not in pop:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {pop[country]} crore")

def main():
    op = input("Enter operation(add, remove, query or print): ")
    if op.lower() =='add':
        add()
    elif op.lower()=='remove':
        remove()
    elif op.lower()=='query':
        query()
    elif op.lower()=='print':
        print_all()

if __name__ == '__main__':
    main()