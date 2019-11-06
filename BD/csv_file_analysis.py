from functools import reduce


fname = r"C:\arun\study\GitHub\python\BD\data\retail_db_order_items.txt"

with open(fname) as file:
	c = file.readlines()
	

print("Using map filter")
	
filtered_c = list(filter( lambda r: r.split(",")[1] == "2" ,c))
get_amounts = list(map(lambda r: r.split(",")[4] ,filtered_c))
total_amount = reduce(lambda accum, elem: float(accum) + float(elem) ,get_amounts)

print("{} \n {} \n {}".format(list(filtered_c), list(get_amounts), total_amount))



print("Using list compr")

new_total_amount = sum([float(l.split(",")[4]) for l in c if l.split(",")[1] == "2"])
print(new_total_amount)