import os
from os.path import expanduser
from core.Support import getGridTime

REPAIR_ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_PATH = os.path.join(REPAIR_ROOT, "data")
REPAIR_TOOL_FOLDER = os.path.join(REPAIR_ROOT, "repair_tools")
WORKING_DIRECTORY = os.path.join("/tmp/")
OUTPUT_PATH = os.path.join(REPAIR_ROOT, "results/")

MAVEN_BIN = expanduser("~/deps/Maven/apache-maven/bin")

JAVA7_HOME = expanduser("/usr/lib/jvm/java-1.7.0/bin/")
JAVA8_HOME = expanduser("/usr/lib/jvm/java-1.8.0-openjdk/bin")
JAVA_ARGS = "-Xmx4g -Xms1g"

LOCAL_THREAD = 1
GRID5K_MAX_NODE = 50
##In minutes
TOOL_TIMEOUT = "180"
#Format: HH:MM ## the fuction getGridTime calculates the timeout of the grid taking into account an overhead (expressed as percentage)
GRID5K_TIME_OUT = getGridTime(TOOL_TIMEOUT, overhead=0.33)
