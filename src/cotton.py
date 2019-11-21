# this is a comment !
def main():
    print("this is basically what i did in my holiday")
    listao = ["sdasd", "dsfdsfads", "dfdsfads",
              10, ["list inside a list", 12], 50]
    texto = "dfjadsfois"
    nro = 10.5
    bigger = 0
    smaller = 0
    x = 0
    print(listao)
    print(texto)
    print(nro)

    for i in range(10):
        x = input("enter a number pls: ")
        if smaller == 0 or x < smaller:
            smaller = x
        elif int(x) > bigger:
            bigger = x

    print("biggest number: {0} \nsmaller number: {1}".format(bigger, smaller))
