foldS1      = [0,       0,      1920,   1080]
foldS2      = [1920,    0,      3840,   1080]
foldTVF1    = [674,     1,      1246,   1017]
foldTVF2    = [2594,    1,      3166,   1017]
foldTVS1    = [899,     162,    1304,   882 ]
foldTVS2    = [2819,    162,    3224,   882 ]


def foldRegReturn (foldName):
    if   (foldName == "S1"):
        return foldS1
    elif (foldName == "S2"):
        return foldS2
    elif (foldName == "TVF1"):
        return foldTVF1
    elif (foldName == "TVF2"):
        return foldTVF2
    elif (foldName == "TVS2"):
        return foldTVS1
    elif (foldName == "TVS2"):
        return foldTVS2
    else:
        print ("Error. Folder name not found.")


def regSize ():
    # return size of list
    return 6
