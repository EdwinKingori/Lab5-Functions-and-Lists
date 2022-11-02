Python 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
lst = [5, 2.5, 100, -10]
5 in lst
True
10 in lst
False
lst*2+['hello', 0]
[5, 2.5, 100, -10, 5, 2.5, 100, -10, 'hello', 0]
[5, 2.5, 100, -10, 5, 2.5, 100, -10, 'hello', 0]
[5, 2.5, 100, -10, 5, 2.5, 100, -10, 'hello', 0]
lst[1:3]
[2.5, 100]
lst[1] = "yuz"
lst.append('one')
lst.insert(1,100)
lst = [5, 2.5, 100, -10]
lst.insert(1,100)
lst.index(100)
1
lst.count(100)
2
lst.remove(100)
lst.reverse()
print(lst)
[-10, 100, 2.5, 5]
lst.sort()
print(lst)
[-10, 2.5, 5, 100]
lst.insert(1,2,200)
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#18>", line 1, in <module>
TypeError: insert expected 2 arguments, got 3
lst.insert(2,200)
print(lst)
[-10, 2.5, 200, 5, 100]
lst.sort()
print(lst)
[-10, 2.5, 5, 100, 200]
