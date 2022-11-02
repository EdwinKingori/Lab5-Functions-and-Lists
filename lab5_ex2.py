def list_product(lst):
    result = 1
    for i in lst:
        result= result * i
    return result


def main():
    lst = [5, 2.5, 100, -10]
    print(lst)
    print(list_product(lst))
    
main()
