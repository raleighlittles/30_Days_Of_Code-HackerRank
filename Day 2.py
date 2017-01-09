meal_cost = input()

tip_percent = raw_input()

tax_percent = raw_input()

total_cost = float(tip_percent)/100 * float(meal_cost) + float(tax_percent)/100 * float(meal_cost) + float(meal_cost)

print "The total meal cost is", int(round(total_cost)), "dollars."