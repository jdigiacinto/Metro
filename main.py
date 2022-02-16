'''
main.py

Authors: Jimmie DiGiacinto, Joseph Teniente, Christian Degollado,
Nikolaus Herrera, Grant Carrell

Purpose: To allow the user to connect to a specified LDAP server and
upload, download, delete, and move files. The client will incorporate end-to-end
encryption and other methods to verify confidentiality and file integrity.
'''
#PACKAGE IMPORTS


#WELCOME TO METRO
print("Welcome to Metro LDAP file management client.\n")


#PROMPT USER FOR THE SERVER IP ADDRESS
serverIP = input("Please specify the IP address of the server you're accessing:  ")


validIP = False

#CHECKS IF SUPPLIED IP ADDRESS IS VALID
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


checkIP(serverIP)


#VERIFY THAT THE IP ADDRESS IS VALID, THEN PRINT STATUS MESSAGE
if(validIP == True):
    print("Accessing LDAP server " + serverIP)
else:
    print("Error. Please enter a valid IP address.\n")



