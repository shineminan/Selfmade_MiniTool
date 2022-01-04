import os

def single_folder_deletion(folder, keyword,loc):
    x, y = loc.replace("(", "").replace(")", "").split(":")
    deletelist = []
    notcontain = 0
    contain = 0
    print(list(folder.split("\\"))[-1] + " is being check")

    for filename in os.listdir(folder):
        purefilename = list(filename.rsplit(".", 1))[0]
        aa = purefilename[int(x):]
        if keyword in purefilename:
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

def multiple_folder_deletion(folder, keyword,loc):
    subfolders = os.listdir(folder)
    paths_list = []
    for name in subfolders:
        subfolderpath = folder + '\\' + name
        paths_list.append(subfolderpath)
    for path in paths_list:
        print("." * 200)
        single_folder_deletion(path, keyword, loc)
    print("All Done!")


infoinput = input("Paste the folder address; The keyword to search; The index of location of the keyword, eg: (:5) ,(5-10) , (10:); Single folder deletion(1) or multiple deletion(2):   ")
folder, keyword, loc, index = infoinput.split(",")
# x, y = loc.replace("(", "").replace(")", "").split(":")
#
# print(x, y)
#


if int(index) == 1:
    single_folder_deletion(folder, keyword,loc)
elif int(index) == 2:
    multiple_folder_deletion(folder, keyword)
else:
    print("Duck you, totally wrong input!!!")

    # C:\Users\shine\Desktop\Levi_Conley,.1,(-2:),1
