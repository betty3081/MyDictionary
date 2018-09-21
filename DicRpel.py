import sys
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from function.SearchDic import Dic_search
from function.ReadDic import Dic_read


while True:
     user_input = prompt("SEARCH WORD>", history=FileHistory("history.txt"),
     auto_suggest=AutoSuggestFromHistory(), )
     dic_source = Dic_read()
     if user_input == "...":
        break
     Dic_search(user_input,dic_source)
                 