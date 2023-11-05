# Shebang-add
A Python script to add a Shebang to an existing script.

# Usage:
Run:
```Shell
./Shebang_add.py test.py Python
```
This will add the Python Shebang "#!/usr/bin/env python3" to the file "test.py". There are also shebangs for Shell, Zsh and Bash available. For adding a custom interpreter just enter the Shebang like:
```Shell
./Shebang_add.py test.py #!/usr/bin/env python3
```

If you want to mark the file as executable, you can add the option "-e" or run the following command:
```Shell
./Shebang_add.py test.py Python -e
```

# Modifying:
You can modify many things by adding the config-file it's called "config.json"
## Language:
To change the language, edit the config file and change **"defaultLanguage"**
```json
    "defaultLanguage": "English",
```
from **"English"** to **"German"**. Currently only English and German are available.
## Executable:
For changing the Default of the **"-e"** option you can change **"executable"** to **true**.
```json
    "executable": false,
```
Now you don't have to add **-e True**
