# Shebang-add
A Python script to add a Shebang to an existing script.

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