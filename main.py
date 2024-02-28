from typing import List, Union
import time 

def numbers(file: str) -> List[int]:
    '''
    Function to make list of numbers from file
    '''
    with open(file, 'r') as output_file:
        content = output_file.read()
        ls = content.split()
        list_numbers = []
        
        for i in ls:
            if i.isdigit() or (i[1:].isdigit() and i[0] == '-'):
                list_numbers.append(int(i))
                 
        return list_numbers
    

def min_number(numbers: List[int]) -> int:
    '''
    Function to find min number in list.
    '''
    res = numbers[0] + 1
    for i in numbers:
        if i < res:
            res = i
        
    return res


def max_number(numbers: List[int]) -> int:
    '''
    Function to find man number in list.
    '''
    res = numbers[0] - 1
    for i in numbers:
        if i > res:
            res = i
        
    return res


def length(numbers: List[int]) -> int:
    '''
    Custom function for length search (you can use built-in function len())
    '''
    counter = 0
    for i in numbers:
        counter += 1
    
    return counter


def suma(numbers: List[int]) -> int:
    '''
    Custom function for sum search (you can use built-in function sum())
    '''
    suma = 0
    for i in numbers:
        suma += i
    
    return suma


def mediana(numbers: List[int]) -> Union[int, float]:
    '''
    Function to find median value in list.
    '''
    if length(numbers) % 2 == 0:
        med1 = numbers[(length(numbers) // 2) - 1]
        med2 = numbers[length(numbers) // 2]
        res = (med1 + med2) / 2
    
    else:
        res = numbers[length(numbers) // 2]
        
    return res


def average(numbers: List[int]) -> Union[int, float]:
    '''
    Function to find average value in list.
    '''
    res = suma(numbers) / length(numbers)
    return round(res, 2)


def increase(numbers: List[int]) -> List[int]:
    '''
    Function to find the largest sequence of increasing numbers.
    '''
    res = []
    ls = []
    start = numbers[0] - 1
    for i in numbers:
        if i > start:
            ls.append(i)
        else:
            if length(res) < length(ls):
                res = ls
            ls = [i]
        if i == numbers[-1] and length(res) < length(ls):
            res = ls
            
        start = i  
    return res  


def decrease(numbers: List[int]) -> List[int]:
    '''
    Function to find the largest sequence of decreasing numbers.
    '''
    res = []
    ls = []
    start = numbers[0] + 1
    for i in numbers:
        if i < start:
            ls.append(i)
        else:
            if length(res) < length(ls):
                res = ls
            ls = [i]
        if i == numbers[-1] and length(res) < length(ls):
            res = ls
            
        start = i  
    return res  
    

if __name__ == '__main__':
    try:
        ls = numbers(file=input('Path to file: '))
        start_time = time.time()
        
        print(f"Min Number: {min_number(numbers=ls)}")
        print(f"Max Number: {max_number(numbers=ls)}")
        print(f"Median: {mediana(numbers=ls)}")
        print(f"Average: {average(numbers=ls)}")
        print(f"Increase: {increase(numbers=ls)}")
        print(f"Decrease: {decrease(numbers=ls)}")
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Running time: {round(elapsed_time, 2)} seconds")
    except Exception as e:
        print(f"Error: {e}")
    
