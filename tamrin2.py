# %%
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("hesam")
        returnd = func(*args, **kwargs)
        print("rezaei")
        return returnd

    return wrapper


@my_decorator
def test():
    return 12


# %%
print("hesam")
print("test GPG")
