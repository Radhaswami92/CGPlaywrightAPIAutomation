import os
import re
Dynamic_path_project_root= os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
project_path = re.escape(Dynamic_path_project_root)
