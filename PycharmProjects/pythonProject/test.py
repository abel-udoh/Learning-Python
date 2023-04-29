"""name= input("What is your name please: ")
print(f"Hi, your name is {name}")
occupation = input("What do you do? ")
print(f"Great, you are a {occupation}")
print("This is guessing game, if you guess right, there is a price for you")
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed")

print('#pythoniscool')
__import__("os").write(1, "#pythoniscool\n".encode("UTF-8"))
import string
print(string.ascii_uppercase)

print("Ada is {} years old." .format(12))
new_string = "Ada is {} {} "
print(new_string.format("Twelve", "Years Old"))


def uniq_add(my_list=[]):
    if my_list is not None:
        return sum(set(my_list))


if __name__ == '__main__':
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))


    def common_elements(set_1, set_2):
        return (set_1 & set_2)


    if __name__ == '__main__':
        set_1 = {"Python", "C", "Javascript"}
        set_2 = {"Bash", "C", "Ruby", "Perl"}
        c_set = common_elements(set_1, set_2)
        print(sorted(list(c_set)))


def common_elements(set_1, set_2):
    return set_1 & set_2


if __name__ == '__main__':
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))

def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2


if __name__ == '__main__':
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set))

def number_keys(a_dictionary):
    return len(a_dictionary)


if __name__ == '__main__':
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys)

def mutiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, list(my_list)))"""


class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

b = Base()
print(b.id)