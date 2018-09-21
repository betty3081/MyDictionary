def Dic_read():
     my_file = open("DicLib.txt", "r")
     dic_list = my_file.readlines()
     my_file.close()
     return dic_list
