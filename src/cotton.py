# this is a comment !
def main():
    print("this is basically what i did in my holiday")
    listao = ["sdasd", "dsfdsfads", "dfdsfads", 10, ["list inside a list", 12], 50]
    texto = "dfjadsfois"
    nro = 10.5
    bigger = 0
    smaller = None
    for index in range(10):
        x = input("enter a number pls")
        if x < smaller or smaller == None:
            smaller = x
        if x > bigger:
            bigger = x

    print("bigger number: {0} \nsmaller number: {1}".format(bigger, smaller))