#Removing elements that are less than 5 in a list

def list_remove(lst):
    result = [lst]
    for i in lst:
        if i<5:
            lst.remove(i)
    return result
    


def main():
     lst = [5, 2.5, 100, -10]
     print(lst)
     print(list_remove(lst))
     print(lst)

main()
