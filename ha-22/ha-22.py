# ---------------------------- Task 1 --------------------------------
def file_reader():
    with open("text.txt", "r", encoding="utf-8") as files:
        for file in files:

            a, b = file.strip().split(",")
            if int(a) < 0 or int(b) < 0:
                raise ValueError("The number must be positive")
            else:
                print(int(a) / int(b))


file_reader()


# ---------------------------- Task 2 --------------------------------

def other_reader():
    try:
        with open("text.txt", "r", encoding="utf-8") as files:
            for file in files:

                a, b = file.strip().split(",")

                try:
                    print(f"Division {a} by {b} = {int(a) / int(b)}")
                except ValueError:
                    print("Value is not a number")
                    return

                except ZeroDivisionError:
                    print("Can't divide by 0")
                    return

    except FileNotFoundError:
        print("FIle not found")
    finally:
        print("The function worked")


other_reader()
