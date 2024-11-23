from sparserestore import backup, perform_restore
from pathlib import Path
import plistlib
import os
import yaml

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def custom():
    width = input("Enter custom width: ")
    if not width:
        print("Defaulting to iPhone 14 Pro Max width (1290)...")
        width = 1290
    height = input("Enter custom height: ")
    if not height:
        print("Defaulting to iPhone 14 Pro Max height (2796)...")
        height = 2796

    data = {
        "canvas_width": int(width),
        "canvas_height": int(height)
    }
    
    resset_path = Path.joinpath(Path.cwd(), 'ressetX.plist')

    with open(resset_path, 'wb') as out_fp:
        plistlib.dump(data, out_fp)

    contents = open(resset_path, "rb").read()

    backupFiles = backup.Backup(files= [
        backup.Directory("", "ManagedPreferencesDomain"),
        backup.Directory("mobile", "ManagedPreferencesDomain"),
        backup.ConcreteFile("mobile/com.apple.iokit.IOMobileGraphicsFamily.plist", "ManagedPreferencesDomain", contents=contents)
    ])

    input("PLEASE READ THIS. THE MODIFICATIONS THIS TOOL MAKES TO YOUR DEVICE CANNOT BE EASILY REVERTED.\nYOU MUST BE ABLE TO UNLOCK YOUR DEVICE AND ACCEPT THE TRUST POPUP TO MODIFY THE RESOLUTION AGAIN.\nWE WILL NOT BE HELD RESPONSIBLE FOR ANY DAMAGES.\nIF YOU DON'T KNOW EXACTLY WHAT YOU'RE DOING, IT IS RECOMMENDED TO EXIT OUT OF THIS PROGRAM.\n\nPress Enter to apply, or Ctrl+C to exit.")

    perform_restore(backup=backupFiles, reboot=True)
    
    print("Applied successfully! Rebooting device...")
    
def preset():
    
    print("To view all devices and their names, check the 'devices.yaml' file in the ResSetX folder.\n")
    
    device_name = input("Which device would you like to choose? (e.g., 'iPhone 16 Pro Max'): ").strip()
    
    try:
        with open('ResSetX/devices.yaml', 'r') as file:
            data = yaml.safe_load(file)
        
        if device_name in data:
            dimensions = data[device_name]
            width = dimensions.get("Width")
            height = dimensions.get("Height")

            data = {
                "canvas_width": int(width),
                "canvas_height": int(height)
            }
            
            resset_path = Path.joinpath(Path.cwd(), 'ressetX.plist')

            with open(resset_path, 'wb') as out_fp:
                plistlib.dump(data, out_fp)

            contents = open(resset_path, "rb").read()

            backupFiles = backup.Backup(files= [
                backup.Directory("", "ManagedPreferencesDomain"),
                backup.Directory("mobile", "ManagedPreferencesDomain"),
                backup.ConcreteFile("mobile/com.apple.iokit.IOMobileGraphicsFamily.plist", "ManagedPreferencesDomain", contents=contents)
            ])

            input("PLEASE READ THIS. THE MODIFICATIONS THIS TOOL MAKES TO YOUR DEVICE CANNOT BE EASILY REVERTED.\nYOU MUST BE ABLE TO UNLOCK YOUR DEVICE AND ACCEPT THE TRUST POPUP TO MODIFY THE RESOLUTION AGAIN.\nWE WILL NOT BE HELD RESPONSIBLE FOR ANY DAMAGES.\nIF YOU DON'T KNOW EXACTLY WHAT YOU'RE DOING, IT IS RECOMMENDED TO EXIT OUT OF THIS PROGRAM.\n\nPress Enter to apply, or Ctrl+C to exit.")

            perform_restore(backup=backupFiles, reboot=True)
            
            print("Applied successfully! Rebooting device...")

        else:
            print(f"Device '{device_name}' not found.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}") 

while True:
    print(r"""
    ______           _____      _  __   __
    | ___ \         /  ___|    | | \ \ / /
    | |_/ /___  ___ \ `--.  ___| |_ \ V / 
    |    // _ \/ __| `--. \/ _ \ __|/   \ 
    | |\ \  __/\__ \/\__/ /  __/ |_/ /^\ \
    \_| \_\___||___/\____/ \___|\__\/   \/

    Made by the jailbreak.party team
We are NOT responsible if anything goes wrong!!""")

    print("""
    1. Set a Custom Resolution (Higher Brick Potential).
    2. Set another iPhone's Resolution on your phone.
    """)
    
    user_choice = input("Choose an option (1 or 2): ")
         
    if user_choice == "1":
        custom()
        break
    elif user_choice == "2":
        preset()
        break
    else:
        clear_console()
