
def list_multiply (lst):
    result = []
    for i in lst:
        result.append(i*2)
    return result


def main ():
    lst = [5, 2.5, 100, -10]
    print(lst)
    print(list_multiply(lst))
    print(lst)
main()
