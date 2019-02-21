Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list("Sabaragamuwa")
['S', 'a', 'b', 'a', 'r', 'a', 'g', 'a', 'm', 'u', 'w', 'a']
>>> example = list("Sabaragamuwa")
>>> example
['S', 'a', 'b', 'a', 'r', 'a', 'g', 'a', 'm', 'u', 'w', 'a']
>>> example[7:]= list("baby")
>>> example
['S', 'a', 'b', 'a', 'r', 'a', 'g', 'b', 'a', 'b', 'y']
>>> example[5:]=list("good")
>>> example
['S', 'a', 'b', 'a', 'r', 'g', 'o', 'o', 'd']
>>> num= [4,5,6]
>>> num
[4, 5, 6]
>>> num[1:1]=[2,6,8,9]
>>> num
[4, 2, 6, 8, 9, 5, 6]
>>> num[1:2]=[]
>>> num
[4, 6, 8, 9, 5, 6]
>>> num[1:5]=[]
>>> num
[4, 6]
>>> 
