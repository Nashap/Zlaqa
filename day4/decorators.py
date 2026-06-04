'''Write 3 custom decorators (timer, logger, auth_required).'''
import time
def timer(fun):
    '''measure execution time of function'''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"Execution Time: {execution_time}s")
        return result
    return wrapper
def logger(fun):
    '''log the function name and arguments when called'''
    def wrapper(*args, **kwargs):
        print(fun.__name__)
        print(fun(*args, **kwargs))
        result = fun(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper
def auth_required(fun):
    '''Allow access only if the user is authenticated'''
    def wrapper(user,*args, **kwargs):
        if user["authenticated"]:
            return fun(user,*args, **kwargs)
        else:
            print("Access Denied")
    return wrapper

@timer
@logger
def rev_list(l):
    """
    reverse a string
    """
    return l[::-1]


@auth_required
def view_profile(user):
    """
    Display user profile.
    """
    print(f"Welcome {user['name']}")


def main():
    my_list = [1, 2, 3, 4, 5]
    print(rev_list(my_list))
    user = {
        "name": "Nasha",
        "authenticated": True
    }
    view_profile(user)
main()