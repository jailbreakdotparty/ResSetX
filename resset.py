from sparserestore import backup, perform_restore
import plistlib
from pathlib import Path

def ressetX():
    width = input("Enter custom width: ")
    if not width:
        print("Defaulting to iPhone 14 Pro Max width (1230)...")
        width = 1320
    height = input("Enter custom height: ")
    if not height:
        print("Defaulting to iPhone 14 Pro Max height (2868)...")
        height = 2868

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

    input("PLEASE READ THIS. THE MODIFICATIONS THIS TOOL MAKES TO YOUR DEVICE CANNOT BE EASILY REVERTED.\nYOU MUST BE ABLE TO UNLOCK YOUR DEVICE AND ACCEPT THE TRUST POPUP TO MODIFY THE RESOLUTION AGAIN.\nWE WILL NOT BE HELD RESPONSIBLE FOR ANY DAMAGES.\nIF YOU DON'T KNOW EXACTLY WHAT YOU'RE DOING, IT IS RECCOMMENDED TO EXIT OUT OF THIS PROGRAM.\n\nPress Enter to apply, or Ctrl+C to exit.")

    perform_restore(backup=backupFiles, reboot=True)

print(r"""
    ______           _____      _  __   __
    | ___ \         /  ___|    | | \ \ / /
    | |_/ /___  ___ \ `--.  ___| |_ \ V / 
    |    // _ \/ __| `--. \/ _ \ __|/   \ 
    | |\ \  __/\__ \/\__/ /  __/ |_/ /^\ \
    \_| \_\___||___/\____/ \___|\__\/   \/

       Made by the jailbreak.party team
  We are NOT responsible if anything goes wrong!!
""")
ressetX()
print("Applied successfully! Rebooting device...")
