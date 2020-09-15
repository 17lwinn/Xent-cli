# Xent-cli

The official CLI and interpreter for the Xentext langauge.

------------------------------

# to download:

Download as a ZIP or clone this repository to use, you must have python3 and the argparse module (in the standard library)

this comes with the python edition of XenText

------------------------------

# command line flags

Xent comes with a selection of command line flags. You execute them with the start command-

```python
python3 main.py <flags>
```

-`-h` - view help text
-`--version` - view CLI version
-`-r <scriptname/path>` - run a .xt file through the lexer

if you want to enter the interpreter, just run 
```python
python3 main.py
```

-------------------------------

# interpreter commands

Type any Xent code into the interpreter and it will save to a file, this file is deleted later on.

1. `run()` - run any code you typed in earlier
2. `forcerun()`- run any code WITHOUT UNLINKING THE FILE
3. `exit()` - exit the interpreter/unlink all session files
4. `moomoo()` - :D we brought a cow!

---------------------------------

# configuration file

Xent reads CLI configuration from **config.py**, which must exist for the CLI to run. You can use the 
following sample to save hassle:

```python
PARSER_LOCATION = "xent.py " # Add a space after the name or you'll have issues
DISABLE_SCRIPT_EXECUTION = "false" # Stop Xent from executing your scripts and run code only from the interpreter
INSTALLED_PACKAGES = [] # packages ( quick complex, leave it to the experts!)
```
---------------------------------

# plugins

xentext plugins are small python files that are run on execution

these are declared in config.py under INSTALLED_PACKAGES and can change your xentext
experience. It can be anything from colouring to just printing text the 'proper' way

To install a plugin, go to [our registry](https://github.com/ProTech-IT-Solutions/xentext-addon-registry) and then run this command:

you must have EXPERIMENTAL_MODE set to 'true' to do this!

```
python3 main.py -i <folder name>
```

go into the folder and make a mental note of the path to the main file. Then go to config.py and link it by the array like this:

```
INSTALLED_PACKAGES = ["pathtopackage/mainfile.py"]
```

run a script, it should be ready to go!, you can use multiple files like this:

```
INSTALLED_PACKAGES = ["path/main.py", "anotherpath/file.py"]
```

---------------------------------
# making an addon

Go to [our registry](https://github.com/ProTech-IT-Solutions/xentext-addon-registry) and then follow the instructions in the wiki

---------------------------------

# quite obvious small print

> &copy; 2020 17lwinn/XentDevs
> &copy; 2020 Jonyk56 ( Creator )