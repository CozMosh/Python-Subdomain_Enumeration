# Subdomain_Enum.py 

# Importing the necessary modules
import requests
import threading

# Define the target domain to scan subdomains for
domain = 'youtube.com'

# Load subdomain names from a wordlist (subdomains.txt) to test against the main domain
# Each subdomain will be checked to see if it resolves to an actual site
with open('subdomains.txt') as file:
    subdomains = file.read().splitlines()

# A list to store discovered subdomains (those that are actually live)
discovered_subdomains = []

# Using a Lock to ensure thread safety when writing to the discovered_subdomains list
lock = threading.Lock()

# Function to check if a given subdomain exists for the target domain
def check_subdomain(subdomain):
    # Construct the full URL to check
    url = f'http://{subdomain}.{domain}'
    
    try:
        # Send an HTTP GET request to check if the subdomain is live
        requests.get(url)
    except requests.ConnectionError:
        # If there's a connection error (subdomain not found), we pass
        pass
    else:
        # If the subdomain is live (no connection error), print it and add it to the discovered list
        print("[+] Discovered subdomain:", url)
        with lock:
            discovered_subdomains.append(url)

# A list to keep track of all threads for checking subdomains
threads = []

# Iterate through each subdomain in the wordlist
# For each subdomain, start a new thread to check if it exists
for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()  # Start the thread
    threads.append(thread)  # Add the thread to the list for later use

# Wait for all threads to finish their work (subdomain checks)
for thread in threads:
    thread.join()

# Once all threads have completed, save the discovered subdomains to a file
with open("discovered_subdomains.txt", 'w') as f:
    # Print each discovered subdomain to the file
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)
