DSA 

Most efficient way to put an element at an index:
https://stackoverflow.com/questions/14494747/how-to-add-images-to-readme-md-on-github
![alt text](images/image.png)

When to use dict of lists and when to use list of lists(you will see this in graphs where you need to create adj lists)

When the keys of the dictionary are 0, 1, ..., n, a list will be faster, since no hashing is involved. As soon as the keys are not such a sequence, you need to use a dict.
https://stackoverflow.com/questions/15990456/list-of-lists-vs-dictionary

when you want to search an element from a list consider using a set too, as search operation in **set** is O(1) as it uses hashtable internally