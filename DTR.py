import os
import subprocess

def main():
    # Initialising Aria2c
    print("Initialising Aria2c")
    print("Aria2 Loaded, Please wait.....")
    
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print instructions for the user
    print("#" * 66)
    print("                        Instructions:")
    print("1) Put your Torrent File in this Folder")
    print("2) Put the name of your torrent file here (without the {.torrent})")
    print("3) Press Enter!")
    print("#" * 66)
    
    # Prompt the user for the torrent name
    torrent_name = input("Torrent Name: ")
    print(f"Torrent {torrent_name}.torrent Loaded, calling Aria2 (Please Wait)....")
    
    print("Aria2 Loaded, starting download.....")
    print("If program asks for network or firewall permissions, please allow")
    
    # Call the aria2c executable with the torrent file
    try:
        result = subprocess.run(['deps.exe', f'--torrent-file={torrent_name}.torrent'], check=True)
        if result.returncode == 0:
            print("Download started successfully!")
        else:
            print(f"Download failed with return code: {result.returncode}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while starting the download: {e}")
    
    # Clear the terminal screen again
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print end-of-job message
    print("End-Of-Job")
    print("Thanks for using DTR by stratosvomvos for downloading your file!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

