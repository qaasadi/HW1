import numpy as np

def binary_search(array, query):
    c=0
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        c=c+1
        mid = (hi + lo) // 2
        val = array[mid]
        if val == query:
            return mid,c
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return mid,c


annual_salary=float(input("Enter the starting salary:"))
total_cost=1000000
semi_annual_raise=.07
portion_down_payment=0.25     #portion of the cost needed for a down payment
r=0.04                        #annual return

portion_down_payment_net=portion_down_payment*total_cost

saved_list=[0]
s=-1
arr_month = np.zeros((1,10001))
arr_portion = np.zeros((1,10001))
for i in range (0,10000): #0-10000
    current_savings=0             #amount that you have saved thus far
    month=0
    monthly_salary=annual_salary/12 
    portion_saved=i/10000
    while current_savings<(portion_down_payment_net-100):
        month=month+1
        
        if month%6==0:
            monthly_salary=monthly_salary+(monthly_salary*semi_annual_raise)
        current_savings=current_savings+portion_saved*monthly_salary+r*current_savings/12

    s=s+1
    arr_month[0,10001-(s+1)]=month
    arr_portion[0,s+1]=portion_saved


solve,c=binary_search(arr_month[0,:],float(36))
if solve==0:
    print ("It is not possible to pay the down payment in three years.")
else:
    solve2=arr_portion[0,10001-(solve)]
    print ("Best savings rate:" + str(solve2))
    print ("Steps in bisection search:" + str(c))


