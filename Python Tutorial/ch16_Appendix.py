# 16.1.3 The Interactive Startup File

"""
import os
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup_file = fobj.read()
    exec(startup_file)

print(filename)
"""

# 16.1.4 The Customization Modules
"""
import site
print(site.getusersitepackages())
"""