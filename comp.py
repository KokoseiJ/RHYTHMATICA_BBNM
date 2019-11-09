def compress(list):
    modlist = []
    meow = "/0"
    numb = 1
    for x in list:
        if x == "/":
            meow = meow[:-1*len(str(numb-1))] + str(numb)
            numb += 1
        else:
            if meow != "/0":
                modlist.append(meow)
            meow = "/0"
            numb = 1
            modlist.append(x)
    return modlist