import os

def single_folder_deletion(folder, keyword):
    print(list(folder.split("\\"))[-1] + " is being check")
    deletelist = []
    notcontain = 0
    contain = 0
    for filename in os.listdir(folder):
        if keyword in filename:
            contain += 1
            deletelist.append(filename)
        else:
            notcontain += 1
    print("The not:contain ratio is " + str(notcontain) + ":" + str(contain))
    # print("Are you sure you want to delete files which contain " + "< " + keyword + " >" + " ?   Y/N")
    yn = input("Are you sure you want to delete files which contain " + "< " + keyword + " >" + " ?   Y/N:    ")
    if yn == "y" or yn == "Y":
        for deletename in deletelist:
            os.remove(folder + "\\" + deletename)
        print("Totally " + str(contain) + " files are deleted")

def multiple_folder_deletion(folder, keyword):
    subfolders = os.listdir(folder)
    paths_list = []
    for name in subfolders:
        subfolderpath = folder + '\\' + name
        paths_list.append(subfolderpath)
    for path in paths_list:
        print("." * 200)
        single_folder_deletion(path, keyword)
    print("All Done!")

infoinput = input("Paste the folder address here seperated by a coma with indication of single folder deletion(1) or multiple deletion(2): ")
folder, keyword, index = (infoinput.split(","))
if int(index) == 1:
    single_folder_deletion(folder, keyword)
elif int(index) == 2:
    multiple_folder_deletion(folder, keyword)
else:
    print("Duck you, totally wrong input!!!")

    # C:\Users\shine\Desktop\aa, .1, 2
