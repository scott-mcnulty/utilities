import os
import sys

# default values
DEFAULT_MAIN_USER = "DEFAULT_USERNAME"
DEFAULT_MAIN_PASSWORD = "DEFAULT_PASSWORD"
DEFAULT_EDITION_USER = "pythoneditions"
DEFAULT_EDITION_PASSWORD = "welcome"
DEFAULT_EDITION_NAME = "python_e1"
DEFAULT_CONNECT_STRING = "localhost/orclpdb"

# values that will be used are the default values unless environment variables
# have been set as noted above
MAIN_USER = os.environ.get("CX_ORACLE_MAIN_USER", DEFAULT_MAIN_USER)
MAIN_PASSWORD = os.environ.get("CX_ORACLE_MAIN_PASSWORD",
        DEFAULT_MAIN_PASSWORD)
EDITION_USER = os.environ.get("CX_ORACLE_EDITION_USER",
        DEFAULT_EDITION_USER)
EDITION_PASSWORD = os.environ.get("CX_ORACLE_EDITION_PASSWORD",
        DEFAULT_EDITION_PASSWORD)
EDITION_NAME = os.environ.get("CX_ORACLE_EDITION_NAME",
        DEFAULT_EDITION_NAME)
CONNECT_STRING = os.environ.get("CX_ORACLE_CONNECT_STRING",
        DEFAULT_CONNECT_STRING)

# calculated values based on the values above
MAIN_CONNECT_STRING = "%s/%s@%s" % (MAIN_USER, MAIN_PASSWORD, CONNECT_STRING)
EDITION_CONNECT_STRING = "%s/%s@%s" % \
        (EDITION_USER, EDITION_PASSWORD, CONNECT_STRING)
DRCP_CONNECT_STRING = MAIN_CONNECT_STRING + ":pooled"