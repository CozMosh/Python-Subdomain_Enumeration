# Python-Subdomain_Enumeration Tool 

## Objective

The Subdomain Scanner project was developed to identify live subdomains for a given domain using multithreaded HTTP requests. It automates reconnaissance tasks commonly used in penetration testing and bug bounty hunting by scanning a list of possible subdomains and reporting which are active. This tool aids in surface mapping and enhances understanding of potential attack vectors in web applications.

### Skills Learned

- Implementation of multithreading in Python for efficient network scanning.
- Understanding of HTTP requests and error handling using the requests library.
- Proficiency in automating cybersecurity reconnaissance techniques.
- Familiarity with domain structures and common subdomain enumeration practices.
- Practical exposure to ethical hacking methodologies.

### Tools Used

- Python’s requests library for sending **HTTP** requests.
- Python threading module for **concurrent** processing.
- Custom subdomain wordlist **(subdomains.txt)** for testing.
- Basic file I/O for logging results to **discovered_subdomains.txt**.


## 🛠 Step-by-Step Code Breakdown

### **Step 1**: Define the Target Domain
```python
domain = 'youtube.com'
```

Step 2: Load Subdomains from a Wordlist
You need a file (subdomains.txt) containing potential subdomain names like www, mail, api, etc.
```python
with open('subdomains.txt') as file:
subdomains = file.read().splitlines()
```

Step 3: Prepare a List to Store Discovered Subdomains
```python
discovered_subdomains = []
```

Step 4: Create a Lock for Thread Safety
This prevents multiple threads from writing to the list at the same time.
```python
lock = threading.Lock()
```

Step 5: Define the Function to Check Each Subdomain
```python
def check_subdomain(subdomain):
url = f'http://{subdomain}.{domain}'
try:
requests.get(url)
except requests.ConnectionError:
pass
else:
print("[+] Discovered subdomain:", url)
with lock:
discovered_subdomains.append(url)
```

Step 6: Create and Start Threads for Each Subdomain
```python
threads = []

for subdomain in subdomains:
thread = threading.Thread(target=check_subdomain, args=(subdomain,))
thread.start()
threads.append(thread)
```

Step 7: Wait for All Threads to Finish
```python
for thread in threads:
thread.join()
```

Step 8: Save the Discovered Subdomains to a File
```python
with open("discovered_subdomains.txt", 'w') as f:
for subdomain in discovered_subdomains:
print(subdomain, file=f)
```

## 🛠 File Structure
```
│
├── subdomains.txt # Your wordlist of potential subdomains
├── discovered_subdomains.txt # Output file containing discovered subdomains
└── scanner.py # Your Python script
```

## 🛠 Command to run the Script
```
python3 script_name.py
```

## ⚠️ Disclaimer

This tool is intended for **educational and authorized testing purposes only**.  
Do not use it to scan domains or networks without explicit permission.  
Unauthorized scanning of domains can be illegal and unethical.


## 👤 Author

Made with curiosity and caffeine ☕  
**Gumbo**  
[GitHub Profile](https://github.com/ritzsec)








