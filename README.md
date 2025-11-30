# sni-checker
Checks access to HTTPS server defined by IP using different SNI names from the "names.txt" file  

### Using

1. Install Python version 3.10 or higher.
2. Download the "sni-checker.py" script.
3. Create a file named "names.txt" containing a list of SNI entries, one per line.
4. Place the "names.txt" file in the same folder as the sni-checker.py file.
5. Define correct server IP inside the script.
6. Execute the script (linux console: 'python3 ./sni-checker.py').
7. View the results!

Generates file "checked-(date-time).txt containing all successfully checked names.
