'''Problem Statement: Logger Decorator
Objective:
You are tasked with creating a Python program that uses a decorator to log the execution details of any function. The decorator should:

Print the name of the function being executed.
Print the arguments passed to the function.
Print the return value of the function after execution.
Specifications:
Write a decorator function called logger that achieves the above objectives.

Apply the logger decorator to the following functions:

add(a, b) - This function returns the sum of two numbers.
multiply(a, b) - This function returns the product of two numbers.
When the decorated functions are called, ensure the logs are displayed in the following format:

Function 'add' was called with arguments (a=2, b=3)
It returned: 5

Similarly, the logs for multiply should look like this:

Function 'multiply' was called with arguments (a=4, b=5)
It returned: 20'''

def logger(func):
    """Decorator to log the function's execution details."""
    def wrapper(*args, **kwargs):
        # Log function name and arguments
        args_str = ", ".join(f"{arg}" for arg in args)
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        params = f"{args_str}, {kwargs_str}".strip(", ")
        print(f"Function '{func.__name__}' was called with arguments ({params})")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log the return value
        print(f"It returned: {result}")
        return result
    return wrapper


# Apply the logger decorator to the add and multiply functions
@logger
def add(a, b):
    return a + b

@logger
def multiply(a, b):
    return a * b


if __name__ == "__main__":
    # Test the decorated functions
    result1 = add(2, 3)
    result2 = multiply(4, 5)
