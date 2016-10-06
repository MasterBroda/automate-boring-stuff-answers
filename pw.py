PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print "Need an argument"
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print "Password for " + account + " copied to clipboard"

else:
    print "No password found for " + account
