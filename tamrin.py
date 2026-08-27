# %%
print("hesam")
print("this is tamrin for git and test for merge")
print("this is a test for cherry-pick")


# %%
class person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f"name is {self.name} and age is {self.age} and job is {self.job}"


# %%
def add(num_1, num_2):
    return num_1 + num_2


def multy(num_1, num_2):
    return num_1 * num_2


# %%

add("hesam", " rezaeifard")
# %%
multy(5, 5)
multy(10, 10)


# %%
def my_generator(num):
    for i in range(num):
        yield i**4


# Comment in the master
# B
# D
#Test For Pull request