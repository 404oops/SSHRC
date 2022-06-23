import os, time, json
from colorama import Fore, Back, Style
print(Fore.BLUE + """::::::::::::::::::::::::::::::::::::::::::::::::::::
:'######:::'######::'##::::'##:'########:::'######::
'##... ##:'##... ##: ##:::: ##: ##.... ##:'##... ##:
 ##:::..:: ##:::..:: ##:::: ##: ##:::: ##: ##:::..::
. ######::. ######:: #########: ########:: ##:::::::
:..... ##::..... ##: ##.... ##: ##.. ##::: ##:::::::
'##::: ##:'##::: ##: ##:::: ##: ##::. ##:: ##::: ##:
. ######::. ######:: ##:::: ##: ##:::. ##:. ######::
:......::::......:::..:::::..::..:::::..:::......:::""" + Style.RESET_ALL)

with open("hosts.json", 'r') as file: hosts = json.loads(file.read())

for i in hosts:
    print(f"""{Fore.GREEN}{list(hosts).index(i)} - {i}:
    {Fore.CYAN}{hosts[i]["Host"]}:""" + hosts[i]['Port'])
x = input(f"{Fore.LIGHTBLUE_EX}Enter a number (0-{len(list(hosts)) - 1}) or press enter to go to shell: {Style.RESET_ALL}")
try: int(x)
except ValueError: exit()
try: list(hosts)[int(x)]
except IndexError:
  print("You selected the wrong number, exiting...")
  exit()
reference = hosts[list(hosts)[int(x)]]
os.system("clear")
os.system(f"ssh {reference['Host']} -p {reference['Port']}")