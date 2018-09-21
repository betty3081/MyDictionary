import sys
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from Dictionary import Dic_read
from Dictionary import Dic_search


while True:
     user_input = prompt("SEARCH WORD>", history=FileHistory("history.txt"),
     auto_suggest=AutoSuggestFromHistory(), )
     dic_source = Dic_read()
     if user_input == "...":
        break
     Dic_search(user_input,dic_source)
                 