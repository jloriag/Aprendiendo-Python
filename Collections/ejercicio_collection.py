import sys
from collections import Counter

# Lee todo lo que pegues en consola hasta EOF (Ctrl+D en Linux/Mac, Ctrl+Z en Windows)
data = sys.stdin.read().splitlines()

number_shoes=data[0]
input_shoe_sizes=list(map(int,data[1].split()))
num_customer=int(data[2])

cust_purchase=[]
for i in range(num_customer):
    a,b= map(int,data[i+3].split())
    cust_purchase.append((a,b))

def remove_shoe_size(shoe_sizes, shoe_size):
    for i in range(len(shoe_sizes)):
        if shoe_sizes[i] == shoe_size: 
            shoe_sizes.remove(shoe_size)
            return True
    return False

def calculate_money_earned(cust_purchase):
    suma=0
    for clave,valor in cust_purchase:
        if (remove_shoe_size(input_shoe_sizes,clave)):
            suma+=valor
    return suma


print(calculate_money_earned(cust_purchase))