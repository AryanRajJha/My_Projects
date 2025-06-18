# import subprocess
# import os

# script_path = os.path.abspath("C:\\Users\\HP\\Desktop\\Mental Health\\bdi.py")
# subprocess.Popen(['start', 'cmd', '/k', f'python "{script_path}"'], shell=True)


import subprocess
import os
import platform

script_path = os.path.abspath("C:\\Users\\HP\\Desktop\\Mental Health\\bdi.py")

if platform.system() == "Windows":
    subprocess.Popen(['start', 'cmd', '/k', f'python "{script_path}"'], shell=True)
elif platform.system() == "Darwin":  # macOS
    subprocess.Popen([
        'osascript', '-e',
        f'tell application "Terminal" to do script "python3 \\"{script_path}\\""'
    ])
else:  # Linux
    subprocess.Popen(['gnome-terminal', '--', 'python3', script_path])
