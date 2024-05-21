import random
 
list_buchstaben = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
list_zahlen = (0,1,2,3,4,5,6,7,8,9)
list_sonderzeichen = ("!","\"","§","$","%","&","/","(",")","=","?",",",".","-","_","<",">","{","}","[","]")
list_großbuchstaben = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
list_all = []   #Liste startet leer
password_list = []
password = ""
 
while True:
    try:
        print("Bitte die folgenden Eingaben mit Ja oder Nein beantworten.")
        sonderzeichen = input("Soll ihr Passwort Sonderzeichen enthalten? ")
        ziffer = input("Soll ihr Passwort Ziffern enthalten? ")
        großbuchstaben = input("Soll ihr Passwort Großbuchstaben enthalten? ")
        passwortlänge = int(input("Wie viele Zeichen soll ihr Passwort sein? "))
 
        list_all.append(list_buchstaben)                #Wir nutzen auf jeden Fall kleinbuchstaben
        
        if sonderzeichen.lower() == "ja":
            list_all.append(list_sonderzeichen)         #Füge sonderzeichen hinzu
        if ziffer.lower() == "ja":
            list_all.append(list_zahlen)                #Füge Zahlen hinzu
        if großbuchstaben.lower() == "ja":
            list_all.append(list_großbuchstaben)        #Füge Buchstaben hinzu
 
        for liste in list_all:                          #Wir haben jetzt eine anzahl X an listen in list_all
            password_list.append(random.choice(liste))  #jetzt gehen wir einmal in jede Liste und fügen einen Zufälligen Wert aus der Lsite ans PW
                                                        #Das Garantiert, dass jeder gewählte Wert mind. 1 mal im PW vorkommt
        
        while len(password_list) != passwortlänge:       #Während die PW noch nicht die laenge erreicht hat
            password_list.append(random.choice(list_all  #Erweitere die liste password_list
            [random.randint(0, len(list_all)-1)]))       #Wähle einen zufallswert
                                                         #aus der Lsite all mit dem Index
                                                         #Zufälliger Wert zwischen 0 und d. Anzahl an Listen in list_all
                            
                                                        
 
        random.shuffle(password_list)                   #Mische die Liste (weil ja aktuell am Anfang garantiert die 4 Werte sind)
 
        for zeichen in password_list:                   #Gehe die password_list zeichen für Zeichen durch
            password += str(zeichen)                    #Füge dem string password das aktuelle Zeichen hinzu
        
        print(f"Das generierte Passwort ist: {password}")
        break              
        
    except ValueError:
        print("Keine gültige Eingabe")