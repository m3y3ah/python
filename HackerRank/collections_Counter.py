import collections as co
num_of_shoes=input()
shoe_sizes = co.Counter(map(int, input().split()))
num_of_customers=int(input())
money_earned=0
for  customer in range(num_of_customers) :
    customers_size, price=map(int,input().split(" "))
    if customers_size in shoe_sizes.keys() and shoe_sizes[customers_size] >0 :
            shoe_sizes[customers_size]-=1
            money_earned+=price
print(money_earned)