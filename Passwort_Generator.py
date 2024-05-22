import random
 
list_buchstaben = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
list_zahlen = (0,1,2,3,4,5,6,7,8,9)
list_sonderzeichen = ("!","\\",",","§","$","%","&","/","(",")","=","?",".","-","_","<",">","{","}","[","]")
list_großbuchstaben = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
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