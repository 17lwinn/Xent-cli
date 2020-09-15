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
# declare any plugin folders and these will be ran on script execution
#EXAMPLE: INSTALLED_PACKAGES = ["util.main", "util.process"]
#each plugin must be properly coded to work with the most recent zent version
INSTALLED_PACKAGES = ["xent.main"]

#----------------------------------------------------------------