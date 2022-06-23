```
::::::::::::::::::::::::::::::::::::::::::::::::::::
:'######:::'######::'##::::'##:'########:::'######::
'##... ##:'##... ##: ##:::: ##: ##.... ##:'##... ##:
 ##:::..:: ##:::..:: ##:::: ##: ##:::: ##: ##:::..::
. ######::. ######:: #########: ########:: ##:::::::
:..... ##::..... ##: ##.... ##: ##.. ##::: ##:::::::
'##::: ##:'##::: ##: ##:::: ##: ##::. ##:: ##::: ##:
. ######::. ######:: ##:::: ##: ##:::. ##:. ######::
:......::::......:::..:::::..::..:::::..:::......:::
```
SSHRC is a python script designed to run at shell startup (hence the rc at the end) and provide the user with options to launch an SSH session or go to local shell.

I originally made this to serve as a "home screen" for my iSH shell on my jailbroken iPad since none of the terminals I tried display my SSH sessions correctly.
# Installation

Literally WYSIWYG. This script uses UNIX commands, so if you want it to work on Windows or any other NT-Like system, changing a few lines wouldn't hurt

To install this script, you must edit it to point to your hosts.json file on Line 13. You could optionally hide the JSON file by putting a dot in the beginning of the filename or you could put it in a different directory.

The default hosts.json file has everything you need to start a basic SSH session. **MAKE SURE TO EDIT IT BEFORE STARTING SSHRC**. The file is self-explanatory and gives you clear instructions on how to put your details in.

Passwords are not supported. This is because your security could potentially be compromised if your hosts.json file gets leaked, and because the ssh client doesn't support inline passwords for the same reason.

After modifying your scripts and placing your files, place
```sh
python3 sshrc.py # or whatever it's named on your system
```
at the bottom of your shell profile/rc (bashrc, zshrc...)

# Preview

The preview is text-based.

```
::::::::::::::::::::::::::::::::::::::::::::::::::::
:'######:::'######::'##::::'##:'########:::'######::
'##... ##:'##... ##: ##:::: ##: ##.... ##:'##... ##:
 ##:::..:: ##:::..:: ##:::: ##: ##:::: ##: ##:::..::
. ######::. ######:: #########: ########:: ##:::::::
:..... ##::..... ##: ##.... ##: ##.. ##::: ##:::::::
'##::: ##:'##::: ##: ##:::: ##: ##::. ##:: ##::: ##:
. ######::. ######:: ##:::: ##: ##:::. ##:. ######::
:......::::......:::..:::::..::..:::::..:::......:::
0 - Friendly Name:
    user@example.com:22
Enter a number (0-0) or press enter to go to shell: 
```