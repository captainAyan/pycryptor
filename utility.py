
def filenotalreadyadded(v, files):
    for path in files:
        if v == path:
            return False
    return True


def getfilenamefromfilepath(file_path):
    split_list = file_path.split("/")
    return split_list[len(split_list) - 1]


def getdirectorypathfromfilepath(file_path):
    split_list = file_path.split("/")
    dir_path = ""

    for i in range(len(split_list)-1):
        dir_path += split_list[i]+"/"

    return dir_path


def getfileextensionfromfilename(file_name):
    split_list = file_name.split(".")
    return split_list[len(split_list)-1]

