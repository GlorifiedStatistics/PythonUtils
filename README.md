# PythonUtils
A set of utility functions I can easily download and import in python

### Parameter Info
For future reference so I don't have to keep writing it taking up space:  
- Operating on circular lists/dictionaries currently has undefined behavior.  
- Some common parameters:  
    &nbsp;&nbsp;&nbsp;&nbsp;"comparators": can be set to a list of lists, where each sub-list contains at least three elements:  
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - first, the type of the first object being compared  
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - second, the type of the second object being compared  
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - third, a function, taking two args and *args, that returns a boolean based on whether or not the first argument is equal to the second argument  
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Any extra elements are passed to the function as args  
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Default: None  
   &nbsp;&nbsp;&nbsp;&nbsp; "ordered": if True, the lists and all sublists need to be in the same order.  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Default: False  
   &nbsp;&nbsp;&nbsp;&nbsp; "typeless_lists": if True, then lists need not be of the same type, only some type of list.  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     Default: False  
   &nbsp;&nbsp;&nbsp;&nbsp; "remove_used": if True, then elements in l2 are removed from inspection as they are taken up by elements in l1  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   For example - if remove_used is False, then [a, a, a, a] would be equal to [a,], but if it were True, this would not be the case  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Default: True  

### Methods
#### list_to_string(l)
Converts the given list of strings into a single string by appending them all together. Calls the str() built-in
function on every element inside l, so a string is always created.

#### linearize_list(l):
Converts l to be a list containing no sub-lists.
If l is not a list, l is converted into a list of size 1.
All empty lists are ignored.
Dictionaries are not considered lists.

#### is_list(l):
Checks iterability and indexing to make see if l is a list

#### is_sublist(l1, l2, proper=False, ordered=False, typeless_lists=False, remove_used=True, comparators=None)
Returns True if l1 is a sublist of l2. If proper is True, then l1 must be a proper sublist of l2.

#### is_subdict(d1, d2, proper=False, ordered=False, typeless_lists=False, remove_used=True, comparators=None)
Returns True if d1 is a subdict of d2. If proper is True, then d1 must be a proper subdict of d2.

#### cmp_list(l1, l2, ordered=False, typeless_lists=False, remove_used=True, comparators=None)
Returns true if l1 and l2 contain the same elements.
Dictionaries by default are compared using the cmp_dicts function, with the same parameters as this function.

#### cmp_dict(d1, d2, ordered=False, typeless_lists=False, remove_used=True, comparators=None)
Returns True if the dictionaries d1 and d2 are equivalent.

#### diff_list(l1, l2, ordered=False, typeless_lists=False, remove_used=True, comparators=None)
Returns all of the elements in l1 that are not in l2 (ie: l1 - l2).

#### diff_dict(d1, d2, ordered=False, typeless_lists=False, remove_used=True, comparators=None)
Returns all of the elements in d1 that are not in d2 (ie: d1 - d2).
