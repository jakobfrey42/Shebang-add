# Shebang-add
A Python script to add a Shebang to an existing script.

This is my first public repository and not all features are fully implemented yet. If there are any bugs, please let me know, e.g. via the Issues tab on GitHub.

# Usage:
Run:
```Shell
./Shebang_add.py test.py Python
```
This will add the Python Shebang "#!/usr/bin/env python3" to the file "test.py". There are also shebangs for Shell, Zsh and Bash available. For adding a custom interpreter just enter the the Path:
```Shell
./Shebang_add.py test.py /usr/bin/env python3
```

If you want to mark the file as executable, you can add the option "-e" or run the following command:
```Shell
./Shebang_add.py test.py Python -e True
```

# Installation:
If you want to run my script from any directory in the terminal, there are two ways to install it.
## 1. The Package Manager (Linux)
If you are on Debian-based Distributions you can download the .deb-file in the GitHub-releases. Then just run:
```bash
sudo apt install <filename>
```
Unfortunately there is no rpm-file yet. But in the future I will create and upload it. That's the easiest way to install it, but I might forget to update the package after changing something. Then please contact me.

## 2. Manually Installation:
you can also do it Manually just copy the file **"shebang-add"** to **"/usr/bin/"**. Then you have to create the directory **"shebang-add"** in **"/etc/"** and copy **"config.json"** to **"/etc/shebang-add/"**. The last thing you have to do is to edit the path of the config-file in **"shebang-add"** 
# Modifying:
You can modify many things by adding the config-file it's called "config.json"

## Language:
To change the language, edit the config file and change **"defaultLanguage"**
```json
    "defaultLanguage": "German",
```
from **"English"** to **"German"**. Currently only English and German are available.

## Executable:
For changing the default of the **"-e"** option you can change **"executable"** to **true**.
```json
    "executable": true,
```
Now you don't have to add **-e True**.
## Notifications:
the **"notifications"**-key controls whether the program asks you if you want to use a custom interpreter. If it is set to **true** and you run
```bash
./Shebang_add.py test.py /my/custom/interpreter
```
he will ask you if you really want to add the interpreter.
If it is set to **false** he will never ask you again.

## DefaultInput:
This Option isn't implemented yet. It will control the default input if **"notifications"** is set to **true**.