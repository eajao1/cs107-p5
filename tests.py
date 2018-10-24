# Public tests for project 5
import unittest
from stacks import *

# Note that this function takes a lambda as its argument.  It
# executes that lambda and--if it returns without an
# exception--this function returns False, otherwise this returns
# True.
def raises(f):
    try:
        f()
        return False
    except Exception:
        return True

class TestStacks(unittest.TestCase):
    # Write more tests here
    def test_push(self):
        s = make_stack(2)
    
        push(s,1)
        self.assertEqual(s[0], 1)
        self.assertEqual(s[1], [1, None])
        self.assertEqual(s[2], 2)
        push(s,2)
        self.assertEqual(s[0], 2)
        self.assertEqual(s[1], [1, 2])
        self.assertEqual(s[2], 2)
        push(s,3)
        self.assertEqual(s[0], 3)
        self.assertEqual(s[1], [1, 2, 3, None])
        self.assertEqual(s[2], 4)

        #my tests:
        my_stack = make_stack(4)
        push(my_stack,1)
        
        self.assertEqual(my_stack[0], 1)
        self.assertEqual(my_stack[1], [1, None, None, None])
        self.assertEqual(my_stack[2], 4)
        

    def test_copyStackA(self):
        ex1 = [1, [235], 1]
        x = copyStack(ex1)
        self.assertEqual(x[2], 1)

        #my tests:
        birthday_stack = [3, [11, 27, 1998, None], 4]
        twin = copyStack(birthday_stack)
        
        self.assertEqual(twin[0], 3)
        self.assertEqual(twin[1], [11, 27, 1998, None])
        self.assertEqual(twin[2], 4)


        my_example = [2, [1, 2, None, None, None, None], 6]
        copy_example = copyStack(my_example)

        self.assertEqual(copy_example[0], 2)
        self.assertEqual(copy_example[1], [1, 2, None, None, None, None])
        self.assertEqual(copy_example[2], 6)
        

        exampleToo = [3, [10,20,30], 3]
        copyToo = copyStack(exampleToo)

        self.assertEqual(copyToo[0], 3)
        self.assertEqual(copyToo[1], [10,20,30])
        self.assertEqual(copyToo[2], 3)
        
    def test_copyStackB(self):
        ex1 = [1, [235], 1]
        x = copyStack(ex1)
        self.assertEqual(x[0], 1)

        #my tests:

        #In this series of tests, I am making sure that if I change the array in
        #the return value from copyStack(s), those changes are not reflected in s.
        
        birthday_stack = [3, [11, 27, 1998, None], 4]
        twin = copyStack(birthday_stack)
        twin[1][1] = 28
        self.assertEqual(birthday_stack, [3, [11, 27, 1998, None], 4])
        
        my_example = [2, [1, 2, None, None, None, None], 6]
        copy_example = copyStack(my_example)
        copy_example[1][4] = 5
        self.assertEqual(my_example, [2, [1, 2, None, None, None, None], 6])

        exampleToo = [3, [10,20,30], 3]
        copyToo = copyStack(exampleToo)
        copyToo[1][2] = 50
        self.assertEqual(exampleToo, [3, [10,20,30], 3])
        

        
    def test_pop(self):
        ex1 = [1, [235], 1]
        self.assertEqual(pop(ex1), 235)

        #my tests:
        birthday_stack = [3, [11, 27, 1998, None], 4]
        self.assertEqual(pop(birthday_stack), 1998)
        self.assertEqual(birthday_stack, [2, [11, 27, None, None], 4])

        exampleToo = [3, [10,20,30], 3]
        self.assertEqual(pop(exampleToo), 30)
        self.assertEqual(exampleToo, [2, [10,20,None], 3])

        
    def test_toArray(self):
        ex1 = [1, [235], 1]
        self.assertEqual(toArray(ex1),[235])


        #my tests:
        birthday_stack = [3, [11, 27, 1998, None], 4]
        self.assertEqual(toArray(birthday_stack),[11, 27, 1998])

        my_example = [2, [1, 2, None, None, None, None], 6]
        self.assertEqual(toArray(my_example),[1, 2])
        
        exampleToo = [3, [10,20,30], 3]
        self.assertEqual(toArray(exampleToo),[10,20,30])
        
    def test_reverse(self):
        ex1 = [2, [1,2], 2]
        reverse(ex1)
        self.assertEqual(ex1[1], [2,1])

        #my tests:
        birthday_stack = [3, [11, 27, 1998, None], 4]
        reverse(birthday_stack)
        self.assertEqual(birthday_stack[1], [1998,27,11, None])
        
        my_example = [2, [1, 2, None, None, None, None], 6]
        reverse(my_example)
        self.assertEqual(my_example[1], [2,1,None, None, None, None])

    
        exampleToo = [3, [10,20,30], 3]
        reverse(exampleToo)
        self.assertEqual(exampleToo[1], [30,20,10])
        self.assertEqual(exampleToo[0], 3)
        self.assertEqual(exampleToo[2], 3)

    def test_merge(self):
        x = [2, [1,3, None, None], 4]
        merge(x,[1,[2],1])
        self.assertEqual(x[1], [1,2,3,None])
        self.assertEqual(x[0], 3)

        #my tests:
        birthday_stack = [3, [11, 27, 1998, None], 4]
        merge(birthday_stack,[1,[2],1])
        self.assertEqual(birthday_stack[1], [2,11,27,1998])
        self.assertEqual(birthday_stack[0], 4)
        
        my_example = [2, [1, 2, None, None, None, None], 6]
        exampleToo = [3, [10,20,30], 3]

        merge(my_example, exampleToo)
        self.assertEqual(my_example[1], [1, 2, 10, 20, 30, None])
        self.assertEqual(my_example[0], 5)
        

unittest.main()
