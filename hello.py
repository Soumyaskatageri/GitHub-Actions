import platform
from datetime import datetime

print("=== Build Information ===")
print("Timestamp:", datetime.now())
print("Operating System:", platform.system())
print("Python Version:", platform.python_version())
print("Build Status: SUCCESS")