PrimeTeller
===========

This tool generates a short wordlist (9000) that contains your PrimeTel password. 

The input is the mac of the access point.

Usage:
------

    python primeTeller.py mac [outputFile]
    [outputFile] is optional
    
Example:
    
    python primeTeller.py E4:13:13:23:B5:2E passwords.list
    
How is this done:
-----------------

This is the POC for the vulnerability I discovered on my Primetel router at OCT/2015.

The latest 4 digits of the default password, for any Primetel router is derived from the MAC address.

The first 4 digis are Integer digits (0-9), that drops the entropy a lot. Passwords range is only 16 bits. (9000 passwords).

If a WPA handshake is captured it can be cracked in about 10 seconds on a basic laptop.

You can read more about it here: [http://nikos.glikis.net/uncategorized/primeteller/](http://nikos.glikis.net/uncategorized/primeteller/)