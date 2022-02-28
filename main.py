'''
main.py

Authors: Jimmie DiGiacinto, Joseph Teniente, Christian Degollado,
Nikolaus Herrera, Grant Carrell

Purpose: To allow the user to connect to a specified LDAP server and
upload, download, delete, and move files. The client will incorporate
end-to-end encryption and other methods to verify confidentiality and
file integrity.
'''
#PACKAGE IMPORTS
import ldap

#WELCOME TO METRO
print("Welcome to Metro LDAP file management client.\n")


#PROMPT USER FOR THE SERVER IP ADDRESS
def promptIP():
    serverIP = input("Please specify the Domain or IP address of the server you're accessing:  ")
    return serverIP


validIP = False

#CHECKS IF SUPPLIED IP ADDRESS IS VALID
'''
def checkIP(ip):
    try:
        octets = ip.split('.')
        n = 0

        if(len(octets) == 4):
            for octet in octets:
                validIP = True if (int(octet) >= 0
                                   and int(octet) < 256) else False
                n += 1
            return validIP

    except ValueError:
        return False # at least one octet cannot be converted to int.

    except (AttributeError, TypeError):
        return False # address is not a string.

while True:
    serverIP = promptIP()
    checkIP(serverIP)
'''

#VERIFY THAT THE IP ADDRESS IS VALID, THEN PRINT STATUS MESSAGE
'''
if(validIP == True):
    print("Accessing LDAP server " + serverIP)
else:
    print("Error. Please enter a valid IP address.\n")
'''

def main():
    server = str(promptIP())
    who = ""
    cred = ""

    keyword = "metro"

    try:
        l = ldap.open(server)
        l.simple_bind_s(who, cred)
        print("Successfully bound to server.\n")
    except:
        print("uh oh")
