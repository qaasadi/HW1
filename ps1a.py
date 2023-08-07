
annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))

portion_down_payment=0.25;      #portion of the cost needed for a down payment
current_savings=0;              #amount that you have saved thus far
r=0.04;                         #annual return
monthly_salary=annual_salary/12;

portion_down_payment_net=portion_down_payment*total_cost;
month=0;
while (current_savings<portion_down_payment_net):
    current_savings=current_savings+portion_saved*monthly_salary+r*current_savings/12;
    month=month+1;
    #print(current_savings)
    #print(month)




print ("number of months:" + str(month))
