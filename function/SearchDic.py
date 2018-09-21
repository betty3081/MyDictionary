import sys
def Dic_search(user_input,dic_source):
    print ("YOUR WORD:"+user_input)
    dic_length = 0
    while True:
             if user_input == dic_source[dic_length].strip("\n"):
                 print (dic_source[dic_length+1])
                 break
             elif dic_length < len(dic_source)-1:
                 dic_length += 1
             else:
                 print("can't be found")
                 break