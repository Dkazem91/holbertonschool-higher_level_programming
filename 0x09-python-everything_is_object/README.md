## 0x09. Python - Everything is object

**What you should learn from this project**

       At the end of this project you are expected to be able to explain
       to anyone, without the help of Google:

* Why Python programming is awesome (don’t forget to tweet today, with the
  hashtag #pythoniscool :))
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address
  in the CPython implementation)
* What is mutable and immutable
* What are the builtin mutable types
* What are the builtin immutable types
* How does Python pass variables to functions

**0. Who I am?**

     What function would you use to print the type of an object? Write the
     name of the function in the file, without the ()

**1. Where are you?**

     How to get variable identifier (which is the memory address in the
     CPython implementation)? Write the name of the function in the file,
     without the ()

**2. Right count**

     In the following code, do a and b point to the same object?
     Answer with Yes or No.

     >>> a = 89
     >>> b = 100

**3. Right count =**

     In the following code, do a and b point to the same object?
     Answer with Yes or No.

     >>> a = 89
     >>> b = 89

**4. Right count =**

     In the following code, do a and b point to the same object?
     Answer with Yes or No.

     >>> a = 89
     >>> b = a

**5. Right count =+**

     In the following code, do a and b point to the same object?
     Answer with Yes or No.

     >>> a = 89
     >>> b = a + 1

**6. Is equal**

     What should those 3 lines print:

     >>> s1 = "Holberton"
     >>> s2 = s1
     >>> print(s1 == s2)

**7. Is the same**

     What should those 3 lines print:

     >>> s1 = "Holberton"
     >>> s2 = s1
     >>> print(s1 is s2)

**8. Is really equal**

     What should those 3 lines print:

     >>> s1 = "Holberton"
     >>> s2 = "Holberton"
     >>> print(s1 == s2)

**9. Is really the same**

     What should those 3 lines print:

     >>> s1 = "Holberton"
     >>> s2 = "Holberton"
     >>> print(s1 is s2)

**10. And with a list, is it equal**

      What should those 3 lines print:

      >>> l1 = [1, 2, 3]
      >>> l2 = [1, 2, 3]
      >>> print(l1 == l2)

**11. And with a list, is it the same**

      What should those 3 lines print:

      >>> l1 = [1, 2, 3]
      >>> l2 = [1, 2, 3]
      >>> print(l1 is l2)

**12. And with a list, is it really equal**

      What should those 3 lines print:

      >>> l1 = [1, 2, 3]
      >>> l2 = l1
      >>> print(l1 == l2)

**13. And with a list, is it really the same**

      What should print those 3 lines:

      >>> l1 = [1, 2, 3]
      >>> l2 = l1
      >>> print(l1 is l2)

**14. List append**

      What does this script print?

      l1 = [1, 2, 3]
      l2 = l1
      l1.append(4)
      print(l2)

**15. List add**

      What does this script print?

      l1 = [1, 2, 3]
      l2 = l1
      l1 = l1 + [4]
      print(l2)

**16. Integer incrementation**

      What does this script print?

      def increment(n):
      	  n += 1
      a = 1
      increment(a)
      print(a)

**17. List incrementation**

      What does this script print?

      def increment(n):
      	  n.append(4)

      l = [1, 2, 3]
      increment(l)
      print(l)

**18. List assignation**

      What does this script print?

      def assign_value(n, v):
      	  n = v

      l1 = [1, 2, 3]
      l2 = [4, 5, 6]
      assign_value(l1, l2)
      print(l1)

**19. Copy a list object**

      Write a function def copy_list(l): that returns a copy of a list.

* The input list can contain any type of objects
* Your file should be maximum 3-line long (no documentation needed)
* You are not allowed to import any module

**20. Tuple or not?**

      a = ()
      Is 'a' a tuple? Answer with Yes or No.

**21. Tuple or not?**

      a = (1, 2)
      Is 'a' a tuple? Answer with Yes or No.

**22. Tuple or not?**

      a = (1)
      Is 'a' a tuple? Answer with Yes or No.

**23. Tuple or not?**

      a = (1, )
      Is 'a' a tuple? Answer with Yes or No.

**24. Richard Sim's special #0**

      What does this script print?

      a = (1)
      b = (1)
      a is b

**25. Richard Sim's special #1**

      What does this script print?

      a = (1, 2)
      b = (1, 2)
      a is b

**26. Richard Sim's special #2**

      What does this script print?

      a = ()
      b = ()
      a is b

**27. Richard Sim's special #3**

      >>> id(a)
      139926795932424
      >>> a
      [1, 2, 3, 4]
      >>> a = a + [5]
      >>> id(a)

**28. Richard Sim's special #4**

      >>> a
      [1, 2, 3]
      >>> id (a)
      139926795932424
      >>> a += [4]
      >>> id(a)