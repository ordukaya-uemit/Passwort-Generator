import random
import string 

list_buchstaben = string.ascii_lowercase
list_zahlen = string.digits
list_sonderzeichen = string.punctuation
list_großbuchstaben = string.ascii_uppercase
list_all = []   
password_list = []
password = ""
 
while True:
    try:
        print("Bitte die folgenden Eingaben mit Ja oder Nein beantworten.")
        while True:
          sonderzeichen = input("Soll ihr Passwort Sonderzeichen enthalten? ")
          if sonderzeichen in ("ja", "nein"):
           break
        
          else:
           print("Ungültige Eingabe, bitte 'Ja' oder 'Nein' eingeben.")

        while True:
          ziffer = input("Soll ihr Passwort Ziffern enthalten? ")
          if ziffer in ("ja", "nein"):
           break
          else:
            print("Ungültige Eingabe, bitte 'Ja' oder 'Nein' eingeben.")

        while True:
          großbuchstaben = input("Soll ihr Passwort Großbuchstaben enthalten? ")
          if großbuchstaben in ("ja", "nein"):
           break
          else:
            print("Ungültige Eingabe, bitte 'Ja' oder 'Nein' eingeben.")

        while True:          
          passwortlänge = input("Wie viele Zeichen soll ihr Passwort sein? ")
          if passwortlänge.isdigit():
           passwortlänge = int(passwortlänge)
           break
          else:
            print("Ungültige Eingabe, bitte 'Ziffer' eingeben.")
        
 
        list_all.append(list_buchstaben)                
        
        if sonderzeichen.lower() == "ja":
            list_all.append(list_sonderzeichen)         
        if ziffer.lower() == "ja":
            list_all.append(list_zahlen)                
        if großbuchstaben.lower() == "ja":
            list_all.append(list_großbuchstaben)        
 
        for liste in list_all:                          
            password_list.append(random.choice(liste))  
                                                        
        
        while len(password_list) != passwortlänge:       
            password_list.append(random.choice(list_all  
            [random.randint(0, len(list_all)-1)]))       
                                                                                                       
 
        random.shuffle(password_list)                   
 
        for zeichen in password_list:                   
            password += str(zeichen)                    
        
        print(f"Das generierte Passwort ist: {password}")
        break              
        
    except ValueError:
        print("Keine gültige Eingabe, bitte eine Zahl für die Passwortlänge eingeben.")