# A function that constructs and returns a new list using the elements of a given
# list that are greater than 5

def new_list(lst):
    result = []
    for i in lst:
        if i > 5:
            result.append(i)
    return result
            



def main():
    lst = [5,100,500,40.4,44,2.5,100,-10,200,4.98]
    
    print("Original list:", lst)
    print("New list:", new_list(lst))

main()
