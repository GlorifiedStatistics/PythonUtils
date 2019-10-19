# PythonUtils
A set of utility functions I can easily download and import in python

### Parameter Info
For future reference so I don't have to keep writing it taking up space:
- Operating on circular lists/dictionaries currently has undefined behavior.
- Some common parameters:
    "comparators": can be set to a list of lists, where each sub-list contains at least three elements:
        - first, the type of the first object being compared
        - second, the type of the second object being compared
        - third, a function, taking two args and *args, that returns a boolean based on whether or not
            the first argument is equal to the second argument
        - Any extra elements are passed to the function as args
        Default: None
    "ordered": if True, the lists and all sublists need to be in the same order.
        Default: False
    "typeless_lists": if True, then lists need not be of the same type, only some type of list.
        Default: False
    "remove_used": if True, then elements in l2 are removed from inspection as they are taken up by elements in l1
        For example - if remove_used is False, then [a, a, a, a] would be equal to [a,], but if it were True,
            this would not be the case
        Default: True

### Methods
#### list_to_string(l)
    Converts the given list of strings into a single string by appending them all together. Calls the str() built-in
    function on every element inside l, so a string is always created.
