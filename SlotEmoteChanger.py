import os

filePath = "source\\DoSEC.py"

result = os.system(filePath)
if result == 0:
    print("Python script executed successfully.")
else:
    print("Error executing Python script.")
