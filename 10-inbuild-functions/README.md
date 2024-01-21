# isinstance() function


# variable length args
- function with *args
  - Take data as a tuple.
  - ```
    def positional_args_sum(*args):
        # expressions
      ```
  - Driver program.
  - ```
    positional_args_sum(10, 20, 30, 40, 50, 'abc', 'xyz')
    ```
- function with **args 
  - Take data as a dict.
  - ```
    def named_args_func(**args):
        # expressions
    ```
  - Driver program.
  - ```
    named_args_func(first='hello', mid='India', last='Good Morning')
    ```

# Lambda functions
- These are small anonymous functions.
- 'lambda' keyword is used to define lambda expression.
```
    lambda arguments: expression
```
- The function can have any number of arguments.
- But lambda expressions are syntactically restricted to single expression.


# map(function, *iterables) function
- executes the specified function for each item in an iterable.
- we can use this function to create a new list by adding two lists.
- ```
res = list
  ```