# ResSetX
Set screen resolution on all iOS versions.

## Disclaimer
This tool can very easily mess up your device. Unlike ResSet16 and other MDC tools, this will persist across reboots. If you can't unlock the device, you can't change it back.

## Usage
1. Install `pymobiledevice3` in your Python environment.
2. Run `resset.py` with your device plugged in.
3. Enter the width and height you'd like to set (it'll default to 14 Pro Max resolution if you don't enter anything).
4. Read the warning, and press Enter to apply. Your device will reboot.
5. Profit?

## Credits
- [Skadz](https://github.com/skadz108) for writing this script.
- [Lemin's backup system writeup](https://gist.github.com/leminlimez/c602c067349140fe979410ef69d39c28#managed-preferences-domain) for the idea.
- [JJTech/the TrollRestore authors](https://github.com/JJTech0130/TrollRestore) for SparseRestore and its backup code.
