import json
import base64
import random
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet
import getpass
import os
import threading
import difflib
import string
import secrets
import pyperclip
import time
from inputimeout import inputimeout, TimeoutOccurred
import keyboard as kb
import sys
import subprocess


def install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requirements.txt"])



divider = "-----------------------------------------------------------------------------------------------------------------------\n"
lockImg = """                                    
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠟⠉⠀⠀⠀⠈⠙⠿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀
                ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
                ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀ ⣸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
                ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
                ⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
checkImg = """                               
                  ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣷⣶⣴⣾⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⣀⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣄⠀⠀⠀⠀
                  ⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀
                  ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀
                  ⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
                  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠈⢻⣿⣿⣿⣿⣿⣿⣿
                  ⢿⣿⣿⣿⣿⣿⣿⣿⡿⠻⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿
                  ⢈⣿⣿⣿⣿⣿⣿⣯⡀⠀⠈⠻⣿⣿⣿⠟⠁⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁
                  ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠈⠛⠁⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
                  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                  ⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁
                  ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀
                  ⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀
                  ⠀⠀⠀⠀⠉⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠉⠁⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⠿⢿⡻⠿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
vaultImg = """
                                          !wdEEEEEEEEEEEEEEEEEEEEEEEEEEEEdw~   
                                        M@@ZzzzzzzzzzzzzzzzzzzzzzzzzzzzzZ@@6` 
                                        \@@: !vvxvvvvvvvvvvvvvvvvvvvvvxv~ :@@L 
                                        x@@` 0@@@@@@@@@@@@@@@@@@@@@@@@@@Q `@@c 
                                        x@@` $@@@@@@@@@@@@@@@@@@@@@@@@@@Q `@@c 
                                        x@@` $@@@@@@@@@@@@@@@@@@@@@@@@#Tr `@@c 
                                        x@@` $@@@@#I)!,,~L6@@@@@@@@@@@m   `@@c 
                                        x@@` $@@@v`L$@###M!-6@@@@@@@@@3   `@@c 
                                        x@@` $@@)`8@x`  ,d@zT@@@@@@@@@@MT `@@c 
                                        x@@` $@@ r@3            !@@@@@@@Q `@@c 
                                        x@@` $@@r`Q@\`  _Z@z}#@@@@@@@@0-` `@@c 
                                        x@@` $@@@)`T8@B##Z~-d@@@@@@@@@m   `@@c 
                                        x@@` $@@@@Bz*:,,!xd@@@@@@@@@@@E`  `@@c 
                                        x@@` $@@@@@@@@@@@@@@@@@@@@@@@@@@Q `@@c 
                                        x@@` $@@@@@@@@@@@@@@@@@@@@@@@@@@Q `@@c 
                                        x@@` $@@@@@@@@@@@@@@@@@@@@@@@@@@Q `@@c 
                                        \@@: !LLLLLLLLLLLLLLLLLLLLLLLLLL> :@@L 
                                        `d@@MwwwwwwwwwwwwwwwwwwwwwwwwwwwwM@@E` 
                                          ~z6Q@@@@@@$0$$$$0$$0$$0$@@@@@@B6z>   
                                            ,EEEEEd              ZEEEEE!                    
"""

# Global Variables
timeoutGlobalCode = "*TIMEOUT*"

def main():
    # RUN PROGRAM
    # Check if vault exists
    try:
        file = open("password_database.mmf", "r+")
        file.close()
    except:
        # If failed to open
        os.system("cls" if os.name == "nt" else "clear")
        print(vaultSetup())


    # RUN LOGIN
    os.system("cls" if os.name == "nt" else "clear")
    print(lockImg)
    hashed_pass = False
    cSALT, cVERIFIER, dataBase = readFiles()
    time_wait=2
    while not hashed_pass:
        entered_pass = getpass.getpass("Enter Master Key: ")
        hashed_pass = verify_password(
            entered_pass, cSALT, cVERIFIER
        )  # Require password to be entered
        if not hashed_pass:
            print("Incorrect master password. Try again after {} seconds.\n".format(time_wait))
            time.sleep(time_wait)
            time_wait=time_wait*2

    if hashed_pass:
        del entered_pass
        pwd_manager_main_loop(hashed_pass, dataBase)
        del hashed_pass
        del cSALT
        del cVERIFIER
        del dataBase


def pwd_manager_main_loop(hashed_pass, contents):
    os.system("cls" if os.name == "nt" else "clear")
    db = json.loads(decrypt_data(contents, hashed_pass).decode("utf-8"))
    timedOut = False
    while not timedOut:
        os.system("cls" if os.name == "nt" else "clear")
        print(checkImg)
        print(divider)
        user_cmd = print(
            "\n• (a): \t add a new password \n• (s): \t search a  password \n• (m): \t modify an existing password \n• (r): \t read all passwords \n• (d): \t delete a password \n• (g): \t generate random password \n• (c): \t change the master password \n• (e): \t exit\n"
        )
        user_cmd = timeoutInput("Choose from above options: ")
        print("\n")

        # Ensure user input is lowercase
        if user_cmd != timeoutGlobalCode:
            user_cmd = user_cmd.lower()

        # Add Profile
        if user_cmd == "a":
            timedOut = addNewProfile(hashed_pass, db)

        # READ PROFILE
        if user_cmd == "s":
            timedOut = findSpecificProfile(hashed_pass, db)

        # READ ALL PROFILES
        if user_cmd == "r":
            timedOut = readProfilesAll(hashed_pass, db)

        # EDIT PROFILE
        if user_cmd == "m":
            timedOut = editPassword(hashed_pass, db)

        # DELETE PROFILE
        if user_cmd == "d":
            timedOut = deletePassword(hashed_pass, db)

        # GENERATE PASSWORD
        if user_cmd == "g":
            timedOut = generatePwd(hashed_pass, db)
        
        # CHANGE MASTER PASSWORD
        if user_cmd == "c":
            timedOut = changeMasterPwd(hashed_pass, db)

        # EXIT PROGRAM AND RETURN TO TERMINAL
        if user_cmd == "e":
            os.system("cls" if os.name == "nt" else "clear")
            timedOut = True

        # EXIT BECAUSE OF TIMEOUT
        if user_cmd == timeoutGlobalCode:
            timeoutCleanup()
            timedOut = True
            
    # CLEANUP SENSITIVE INFO ON TIMEOUT
    del hashed_pass
    del contents
    del db
    
def ui_run():
    global window
    window = Tk()
    window.title("Los Pollos Hermanos Password Manager")
    window.config(padx=50, pady=50)

    global canvas
    canvas = Canvas(width=200, height=200)
    logo_img = PhotoImage(file="D:/USS/codes/passwordManager/logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(column=1, row=0)


def changeMasterPwd(hashed_pass, db):
    # CHANGE MASTER PASSWORD
    displayHeader("CHANGE MASTER PASSWORD")
    password_provided = getpass.getpass("What would you like your master password to be (type and submit (.c) to cancel)? ")
    if password_provided != ".c" and password_provided != "" and password_provided != " " and password_provided != timeoutGlobalCode:
        password = password_provided.encode()  # Convert to type bytes
        salt = os.urandom(random.randint(16, 256))
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
        )
        hashed_entered_pass = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
        try:
            i = -1
            domains = list(db.keys())
            for e in db:
                i = i + 1

                # decrypt the username and password with the original master password
                username = str(
                    decrypt_data(
                        bytes(db[domains[i]]["username"], encoding="utf-8"), hashed_pass
                    ).decode("utf-8")
                )

                password = str(
                    decrypt_data(
                        bytes(db[domains[i]][ "password"], encoding="utf-8"),
                        hashed_pass,
                    ).decode("utf-8")
                )

                # encrypt and save them with then new master password
                db[domains[i]] = {
                    "username": str(encrypt_data(username, hashed_entered_pass).decode("utf-8")),
                    "password": str(encrypt_data(password, hashed_entered_pass).decode("utf-8")),
                }

                del e
                del username
                del password

            del domains
            file = open("SALT.txt", "wb")
            file.write(salt)
            file.close()
            del salt

            file = open("VERIFIER.txt", "wb")
            file.write(encrypt_data("entered_master_correct", hashed_entered_pass))
            file.close()
            
            # finally overwrite the database file with everything encrypted with the new password
            overwrite_db(encrypt_data(json.dumps(db), hashed_entered_pass).decode("utf-8"))
            del hashed_entered_pass
            del hashed_pass
            os.system("cls" if os.name == "nt" else "clear")
            print("Master password changed successfully! Log in again to access the password manager.")
            timeoutInput("\nPress enter to logout..")
            return True
        except:
            print("Could not change master password (Error code: 01)")
            userContinue = timeoutInput("\nPress enter to return to menu...")
            if userContinue != timeoutGlobalCode:
                return False
            else:
                return True
    else:
        if password_provided != timeoutGlobalCode:
            userContinue = timeoutInput("\nPress enter to return to menu...")
            if userContinue != timeoutGlobalCode:
                return False
            else:
                return True
        else:
            return True
    

def addNewProfile(hashed_pass, db):
    # ADD PROFILE
    displayHeader("ADD A PROFILE")
    print("Type and submit (.c) to cancel.")
    add_domain = timeoutInput("Website domain name: ")
    if add_domain != ".c" and add_domain != timeoutGlobalCode:
        add_user = timeoutInput("Username: ")
    if add_user != ".c" and add_user != timeoutGlobalCode: 
        add_password = getpass.getpass("Password: ")
    if add_domain != ".c" and add_domain != timeoutGlobalCode and add_user != timeoutGlobalCode and add_password != timeoutGlobalCode:
        db[add_domain] = {
            "username": str(encrypt_data(add_user, hashed_pass).decode("utf-8")),
            "password": str(encrypt_data(add_password, hashed_pass).decode("utf-8")),
        }
        overwrite_db(encrypt_data(json.dumps(db), hashed_pass).decode("utf-8"))
        print("Created " + add_domain + " profile successfully!")
    if add_domain == ".c":
        print("Operation canceled.")
        return False
    if add_domain == timeoutGlobalCode or add_user == timeoutGlobalCode or add_password == timeoutGlobalCode:
        return True


def findSpecificProfile(hashed_pass, db):
    displayHeader("FIND A PROFILE")
    print("Type and submit (.c) to cancel.")
    read_domain = timeoutInput("What's the domain you're looking for? ")
    if read_domain != ".c" and read_domain != timeoutGlobalCode:
        try:
            domains = list(db.keys())
            matches = difflib.get_close_matches(read_domain, domains)
            if matches:
                print("\nClosest match:\n")
                i = 1
                for d in matches:
                    domain_info = db[d]
                    username = str(
                        decrypt_data(
                            bytes(domain_info["username"], encoding="utf-8"),
                            hashed_pass,
                        ).decode("utf-8")
                    )
                    print("PROFILE " + str(i) + ": " + d)
                    del d
                    print("Username: " + username + "\n")
                    del domain_info
                    del username
                    i = i + 1
                userContinue = timeoutInput("\nSelect the password to be copied to your clipboard (ex: 1), or type (.c) to cancel: ")
                if userContinue.isdigit() == True:
                    if int(userContinue) > 0:
                        try:
                            password = str(
                                decrypt_data(
                                    bytes(db[str(matches[int(userContinue) - 1])]["password"], encoding="utf-8"),
                                    hashed_pass,
                                ).decode("utf-8")
                            )
                            print("\n" + copyToClipboard(password))
                            del password
                        except:
                            print("\nUnable to find profile corresponding to " + str(userContinue) + ".")
                    else:
                        print("\nThere are no profiles corresponding to that number.")
                if userContinue.isdigit() == False:
                    if userContinue != timeoutGlobalCode:
                        return False
                    else:
                        return True
            else:
                print("Could not find a match. Try viewing all saved profiles.")
        except:
            print("Error finding profile.")
        userContinue = timeoutInput("\nPress enter to return to menu...")
        if userContinue != timeoutGlobalCode:
            return False
        else:
            return True
    if read_domain == ".c":
        print("Operation canceled.")
        print("\nReturning to Menu")
        return False
    if read_domain == timeoutGlobalCode:
        return True


def editPassword(hashed_pass, db):
    displayHeader("EDIT A PROFILE")
    edit_domain = timeoutInput("Website domain name (submit (.c) to cancel): ")
    if edit_domain != ".c" and edit_domain != timeoutGlobalCode:
        try:
            domain_info = db[edit_domain]
            curr_user = str(
                decrypt_data(
                    bytes(domain_info["username"], encoding="utf-8"), hashed_pass
                ).decode("utf-8")
            )
            curr_password = str(
                decrypt_data(
                    bytes(domain_info["password"], encoding="utf-8"), hashed_pass
                ).decode("utf-8")
            )

            edit_user = timeoutInput("New Username (press enter to keep the current: " + curr_user + "): ")
            if edit_user == ".c" or edit_user == " " or edit_user == "":
                edit_user = curr_user
            if edit_user == timeoutGlobalCode:
                return True

            edit_password = timeoutInput("New Password (press enter to keep the current: " + curr_password + "): ")
            if edit_password == ".c" or edit_password == " " or edit_user == "":
                edit_password = curr_password
            if edit_password == timeoutGlobalCode:
                return True

            db[edit_domain] = {
                "username": str(encrypt_data(edit_user, hashed_pass).decode("utf-8")),
                "password": str(
                    encrypt_data(edit_password, hashed_pass).decode("utf-8")
                ),
            }
            overwrite_db(encrypt_data(json.dumps(db), hashed_pass).decode("utf-8"))
            print("Updated " + edit_domain + " profile successfully!")
            del edit_domain
            del curr_user
            del edit_user
            del curr_password
            del edit_password
            del db
            userContinue = timeoutInput("\nPress enter to return to menu...")
            if userContinue != timeoutGlobalCode:
                print("Returning to menu")
                return False
            else:
                return True
        except:
            print("This domain does not exist, changing to adding to new profile")
            userContinue = timeoutInput("\nPress enter to return to menu...")
            if userContinue != timeoutGlobalCode:
                print("Returning to menu")
                return False
            else:
                return True
    if edit_domain != timeoutGlobalCode:
        print("Returning to menu")
        return False
    else:
        return True


def readProfilesAll(hashed_pass, db):
    displayHeader("READING ALL PROFILES")
    try:
        i = 0
        domains = list(db.keys())
        for e in db:
            i = i + 1
            username = str(
                decrypt_data(
                    bytes(db[e]["username"], encoding="utf-8"), hashed_pass
                ).decode("utf-8")
            )
            print("PROFILE " + str(i) + ": " + e)
            print("Username: " + username)
            del e
            del username
            print(divider)
        if i == 0:
            print("No saved profiles")
        if i > 0:
            userContinue = timeoutInput("\nSelect the password to be copied to your clipboard (ex: 1), or type (.c) to cancel: ")
            if userContinue.isdigit() == True:
                if int(userContinue) > 0:
                    try:
                        password = str(
                            decrypt_data(
                                bytes(db[str(domains[int(userContinue) - 1])]["password"], encoding="utf-8"),
                                hashed_pass,
                            ).decode("utf-8")
                        )
                        print("\n" + copyToClipboard(password))
                        del password
                    except:
                        print("\nUnable to find profile corresponding to " + str(userContinue) + ".")
                else:
                    print("\nThere are no profiles corresponding to that number.")
            if userContinue.isdigit() == False and userContinue != timeoutGlobalCode:
                return False
            if userContinue == timeoutGlobalCode:
                return True            
    except:
        print("Could not load all profiles")
    userContinue = timeoutInput("\nPress enter to return to menu...")
    if userContinue != timeoutGlobalCode:
        print("Returning to menu")
        return False
    else:
        return True


def deletePassword(hashed_pass, db):
    displayHeader("DELETE A PROFILE")
    del_domain = timeoutInput("Write the exact saved domain name (type (.c) to cancel): ")
    if del_domain != ".c" and del_domain != timeoutGlobalCode:
        try:
            del db[del_domain]
            overwrite_db(encrypt_data(json.dumps(db), hashed_pass).decode("utf-8"))
            print("Deleted " + del_domain + " profile successfully!")
            userContinue = timeoutInput("\nPress enter to return to menu...")
            if userContinue != timeoutGlobalCode:
                print("Returning to menu")
                return False
            else:
                return True
        except:
            print("Unable to find " + del_domain)
            userContinue = timeoutInput("\nPress enter to return to menu...")
            if userContinue != timeoutGlobalCode:
                print("Returning to menu")
                return False
            else:
                return True
    else:
        if del_domain != timeoutGlobalCode:
            print("Returning to menu")
            return False
        else:
            return True


def generatePwd(hashed_pass, db):
    displayHeader("GENERATE RANDOM PASSWORD")
    pass_length = str(timeoutInput("Password length (type (.c) to cancel): "))
    if pass_length != ".c" and pass_length != timeoutGlobalCode:
        try:
            if int(pass_length) < 6:
                pass_length = str(12)
                print("\nPasswords must be at least 6 characters long. A Random 12 character long password has been generated.")
            print(copyToClipboard(str(generate_password(int(pass_length)))))
            userContinue = timeoutInput("\nPress enter to return to menu...")
            if userContinue != timeoutGlobalCode:
                print("Returning to menu")
                return False
            else:
                return True
        except:
            print("Unable to generate password.")
            userContinue = timeoutInput("\nPress enter to return to menu...")
            if userContinue != timeoutGlobalCode:
                print("Returning to menu")
                return False
            else:
                return True
    else:
        if pass_length != timeoutGlobalCode:
            print("Returning to menu")
            return False
        else:
            return True


def readFiles():
    with open("SALT.txt", "rb") as readfile:
        content1 = readfile.read()
        readfile.close()
    cSALT = content1

    with open("VERIFIER.txt", "rb") as readfile:
        content2 = readfile.read()
        readfile.close()
    cVERIFIER = content2

    file_path = "password_database.mmf"
    file = open(file_path, "rb")
    content3 = file.read()
    dataBase = content3

    return cSALT, cVERIFIER, dataBase


def displayHeader(title):
    os.system("cls" if os.name == "nt" else "clear")
    print(checkImg)
    print(divider)
    print(str(title) + "\n")


# Clear clipboard after 30 seconds
def clear_clipboard_timer():
    kb.wait('ctrl+v')
    time.sleep(0.1) # Without sleep, clipboard will automatically clear before user actually pastes content
    pyperclip.copy("")


# Put string in clipboard
def copyToClipboard(input_to_copy):
    pyperclip.copy(str(input_to_copy))
    del input_to_copy
    threading.Thread(target=clear_clipboard_timer).start()
    return "Password was saved to clipboard. It will be removed from your clipboard as soon as you paste it."


# TIMEOUT
def timeoutCleanup():
    os.system("cls" if os.name == "nt" else "clear")
    print(lockImg)
    print(
        "\n\nYour session expired. For your security, the program has automatically exited. All submitted data is still saved."
    ) 
    sys.exit


def timeoutInput(caption):
    try:
        user_input = inputimeout(prompt=caption, timeout=90)
    except TimeoutOccurred:
        user_input = timeoutGlobalCode
        timeoutCleanup()
    return(user_input)


# CRYPTOGRAPHY FUNCTIONS

# Generate random password - user cannot request passwords that are less than 6 characters
# use secrets instead of random (secrets is safer)
def generate_password(length=12):
    if length < 6:
        length = 12
    uppercase_loc = secrets.choice(string.digits)  # random location of lowercase
    symbol_loc = secrets.choice(string.digits)  # random location of symbols
    lowercase_loc = secrets.choice(string.digits)  # random location of uppercase
    password = ""
    pool = string.ascii_letters + string.punctuation  # the selection of characters used
    for i in range(length):
        if i == uppercase_loc:  # this is to ensure there is at least one uppercase
            password += secrets.choice(string.ascii_uppercase)
        elif i == lowercase_loc:  # this is to ensure there is at least one uppercase
            password += secrets.choice(string.ascii_lowercase)
        elif i == symbol_loc:  # this is to ensure there is at least one symbol
            password += secrets.choice(string.punctuation)
        else:  # adds a random character from pool
            password += secrets.choice(pool)
    return password


def encrypt_data(input, hashed_pass):
    message = input.encode()
    f = Fernet(hashed_pass)
    encrypted = f.encrypt(message)
    return (encrypted)


def decrypt_data(input, hashed_pass):
    f = Fernet(hashed_pass)
    decrypted = f.decrypt(input)
    return (decrypted)


def verify_password(password_provided, cSALT, cVERIFIER):
    verifier = cVERIFIER
    # Hash password for later comparison
    password = password_provided.encode()  # Convert to type bytes
    salt = cSALT
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
    )
    hashed_entered_pass = base64.urlsafe_b64encode(
        kdf.derive(password)
    )  # Can only use kdf once

    try:
        pass_verifier = decrypt_data(verifier, hashed_entered_pass)
        if pass_verifier == b"entered_master_correct":
            return hashed_entered_pass
    except:
        return False

def vaultSetup():
    pas_len =0
    while pas_len<12 :
        os.system("cls" if os.name == "nt" else "clear")
        print(vaultImg)
        print("\nVAULT SETUP\n\nCould not find password_database.mmf in local directory, continuing to vault setup.")
        password_provided = getpass.getpass("What would you like your master password to be? (Minimum length:12 characters)  ")
        pas_len = len(password_provided)
    password = password_provided.encode() # Convert to type bytes
    salt = os.urandom(32)
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
    )
    hashed_entered_pass = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once

    file = open("SALT.txt", "wb")
    file.write(salt)
    file.close()
    del salt

    file = open("VERIFIER.txt", "wb")
    file.write(encrypt_data("entered_master_correct",hashed_entered_pass))
    file.close()

    file = open("password_database.mmf", "w+")
    file.write(str(encrypt_data("{}",hashed_entered_pass).decode('utf-8')))
    file.close()
    del hashed_entered_pass

    input("Your password vault was created. Access it using the main.py file. Press ENTER to continue to login...")
    
# PROFILE OPERATIONS
def overwrite_db(new_contents):
    file = open("password_database.mmf", "w+")
    file.write(new_contents)
    file.close()


if __name__ == "__main__":
    main()
