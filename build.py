"""Script to build program into executable."""

import subprocess

def main():
    """Invoke pyinstaller."""
    try:
        # PyInstaller command to build the executable
        cmd = [
            'pyinstaller',
            'AHEPA Raffle.spec'
        ]

        # Run PyInstaller
        subprocess.check_call(cmd)

        print("Build successful.")
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Build failed: {exc}")

if __name__ == '__main__':
    main()
