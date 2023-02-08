import InsectClass


def main():
    my_insect = InsectClass.Insect()
    print("This side is up:", my_insect.get_flight())

    print("I am going to have the insect fly 10 times:")
    for count in range(10):
        my_insect.flight()

        print("My insect flew (miles):", my_insect.get_flight())


main()
