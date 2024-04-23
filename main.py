#Code by bigmohammad
#---------------------
#Youtube: bigmohammad
#---------------------
#Instagram: bigmohammad.official

import requests
import socket
import whois
import tldextract
from colorama import init, Fore
import os
import sys

def clear_screen():
    # Clear the screen based on the operating system
    if sys.platform.startswith('win'):  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')

def get_website_info():
    try:
        # Clear the screen at the start of the program
        clear_screen()

        while True:
            # Get user input for the website URL
            website_url = input(Fore.BLUE + "Enter the website URL: ")

            # If user just presses Enter, exit the loop
            if website_url.strip() == "":
                break

            # Send a GET request to the website
            response = requests.get(website_url)
            
            # Get the server's IP address using the registered domain
            registered_domain = tldextract.extract(website_url).registered_domain
            ip_address = socket.gethostbyname(registered_domain)
            
            # Get domain information using whois
            domain_info = whois.whois(website_url)
            
            # Extract owner name and hosting provider from domain information
            owner_name = domain_info.get('registrant_name', 'Unknown')
            hosting_provider = domain_info.get('registrar', 'Unknown')
            
            # Print website information in green color
            print(Fore.GREEN + "Website URL:", website_url)
            print("IP Address:", ip_address)
            print("Page Title:", response.text.split('<title>')[1].split('</title>')[0])
            print("Owner Name:", owner_name)
            print("Hosting Provider:", hosting_provider)
            print(Fore.RESET)  # Reset color back to default
            
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error retrieving website information: {e}")
        print(Fore.RESET)  # Reset color back to default
    except whois.parser.PywhoisError as e:
        print(Fore.RED + f"Error retrieving domain information: {e}")
        print(Fore.RESET)  # Reset color back to default

if __name__ == "__main__":
    # Initialize colorama for cross-platform support
    init()

    # Call the function to start
    get_website_info()
