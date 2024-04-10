import os
import zipfile
from termcolor import colored
import argparse
import sys

def extract_zip(zip_filename, wordlist_filename):
    if not os.path.exists(zip_filename):
        print(colored("\n[!] File " + zip_filename + " was not found.", 'red'))
        exit()
    print(colored("\n[+] Analyzing File: ", 'blue'), zip_filename)
    
    if zip_filename[-3:] != "zip":
        print(colored("\n[!] Make Sure It is a .zip File.\n", 'red'))
        exit()
    
    if not os.path.exists(wordlist_filename):
        print(colored("\n[!] File " + wordlist_filename + " Was Not Found.", 'red'))
        exit()
    
    found = False  # Flag to track if password is found
    with open(wordlist_filename, "rb") as passwords:
        passwords_list = passwords.readlines()
        total_passwords = len(passwords_list)
        my_zip_file = zipfile.ZipFile(zip_filename)
        for index, password in enumerate(passwords_list):
            try:
                my_zip_file.extractall(path="Extracted Files", pwd=password.strip())
                print(colored("[+] Password Found: ", 'cyan'), password.decode().strip())
                found = True  # Set flag to True if password is found
                break
            except:
                print(colored(f"Password: {password.decode().strip()} ", 'white'), end='\r')
                continue

    if not found:
        print(colored("[!] Password Not Found", 'red'))  # Print this message if no password is found

def main():
    parser = argparse.ArgumentParser(description="ZIP Cracker")
    parser.add_argument("--zip", help="Path To The ZIP File.", required=True)
    parser.add_argument("--wordlist", help="Path To The Wordlist File.", required=True)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args()
    extract_zip(args.zip, args.wordlist)


if __name__ == "__main__":
    main()
