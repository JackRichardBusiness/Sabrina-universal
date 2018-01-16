from firebase import firebase
import os
database = firebase.FirebaseApplication('https://sabrina-415a1.firebaseio.com')
latestRelease = database.get('houseOS/', 'raspBer')
if os.path.exists("raspVer.txt"):
    currentVersion = open('raspVer.txt', 'r+')
    if currentversion.read() == latestVersion:
        os.system('python3 Sabrina/sabrina.py')
    else:
        os.system('sudo apt-get update')
        os.system('sudo apt-get upgrade')
        os.system('sudo apt-get dist-upgrade')
        currentVersion.write(latestVersion)
        currentVersion.close()
        os.system('python3 Sabrina/sabrina.py')
else:
    currentVersion = open('raspVer.txt', 'w')
    currentVersion.write('1017')
    currentversion.close()
    os.system('python3 director.py')
