import os
from pathlib import Path
home = str(Path.home())
os.chdir(home)
if not os.path.exists("blogs"):
    os.makedirs("blogs")