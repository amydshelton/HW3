
def melons_sold(file_name):
    delineation = "******************************************"
    print delineation

    f = open(file_name)

    #set mellon tallies to 0 to begin with
    melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}

    #get data out of file
    for line in f:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    f.close()

    #here are our melon prices, stored in a dictionary
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

    #set total revenue to 0 to begin with
    total_revenue = 0

    #calculate total revenue for each melon type
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at $%0.2f each for a total of $%0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)

    print delineation

def sales_report(file_name):
    delineation = "******************************************"
    print delineation

    f = open(file_name)

    #set sales figures equal to 0 to begin with
    online_sales = 0
    salespeople_sales = 0

    #calculate how much sales were online vs. not
    for line in f:
        data = line.split(",")
        sales_channel =  data[2]
        sale_amt = data[3]
        if sales_channel == "ONLINE":
            online_sales += float(sale_amt)
        else:
            salespeople_sales += float(sale_amt)

    #print results
    print "Salespeople generated $%0.2f in revenue." % salespeople_sales
    print "Internet sales generated $%0.2f in revenue." % online_sales

    #decide who sold more and print a statement about that
    if salespeople_sales > online_sales:
        print "Guess there's some value to those salespeople after all."
    elif online_sales > salespeople_sales:
        print "Time to fire the sales team! Online sales rule all!"
    else:
        print "Online sales and sales from salespeople were equal!"

    print delineation




def main():
    melons_sold("orders_by_type.csv")

    sales_report("orders_with_sales.csv")

   
if __name__ == "__main__":
    main()
