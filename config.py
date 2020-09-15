# config.py is a required python configuration file that changes how XenText works.
# please do not configure until you know what each option does

# GENERAL configuration - PARSER/COMMAND LINE INTERFACE (CLI) CONFIG

# PARSER_LOCATION, change the location of the parser
# DISABLE_SCRIPT_EXECUTION, stop all execution of any scripts and default to interpreter mode

PARSER_LOCATION = "xent.py " # Add a space after the name or you'll have issues
DISABLE_SCRIPT_EXECUTION = "false" # Stop Xent from executing your scripts and run code only from the interpreter
EXPERIMENTAL_MODE = "true" # see beta features first, may bite!

# ---------------------------------------------------------------
# PLUGIN CONFIG
# declare any plugins here for example:
# INSTALLED_PLUGINS = ["plugin.py"]
# INSTALLED_PLUGINS = ["plugin.py", "anotherplugin.py"]
# or from path:
# INSTALLED_PLUGINS = ["test/hi.py"]


INSTALLED_PLUGINS = []


#----------------------------------------------------------------
# INFO VARS
# PRINT FOR DEBUGGING PURPOSES

INTERPRETER_VERSION = "2.0.2"
