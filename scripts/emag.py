import os
import sys

def check(current_directory):
    return os.path.isfile('esp32m_settings.json')

def create_lock(current_directory):
    with open('lock', 'w') as lock:
        return

def remove_lock(current_directory):
    try:
        os.remove('lock')
    except FileNotFoundError:
        print('Lock file does not exist, or is not found.')

def clean(current_directory):
    remove_lock(current_directory)
    try:
        os.remove('pcap.ds')
    except FileNotFoundError:
        print("PCAP file does not exist, or is not found.")
    try:
        os.remove('pcap(1).ds')
        os.remove('pcap(2).ds')
    except FileNotFoundError:
        return

def main():
    current_directory = os.getcwd()
    if check(current_directory):
        if len(sys.argv) != 2:
            print("Usage: python emag.py [lock|unlock|clean]")
        else:
            arg = sys.argv[1].lower()
            if arg == 'lock':
                create_lock(current_directory)
            elif arg == 'unlock':
                remove_lock(current_directory)
            elif arg == 'clean':
                clean(current_directory)
            else:
                print("Invalid Argument Supplied.")
                print("Usage: python emag.py [lock|unlock|clean]")
    else:
        print("Please run from device root directory.")

if __name__ == '__main__':
    main()