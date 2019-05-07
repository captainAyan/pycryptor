
# colors for elements
# color_primary = "#546de5"
# color_primary_dark = "#303952"
# color_accent_dark = "#596275"
# color_success = "#32ff7e"
# color_danger = "#e15f41"
# color_warning = "#f5cd79"
# color_info = "#18dcff"
# color_white = "#ffffff"

color_primary = "#7d5fff"
color_primary_dark = "#3d3d3d"
color_accent_dark = "#4b4b4b"
color_success = "#32ff7e"
color_danger = "#ff4d4d"
color_warning = "#ffaf40"
color_info = "#18dcff"
color_white = "#ffffff"


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



