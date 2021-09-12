encryption = {"A": "!","B": "@","C": "#","D" : "$","E":"%","F":"^","G":"&","H":"*","I":"+","J":"=","K":">","L":"<","M":"~","N":"`","O":"?","P":"]","Q":":","R":";","S":"|","T":"-","U":"_","V":"{","W":"}","X":"[","Y":"'","Z":'"',"a":")","b":"(","c":"2","d":"1","e":"3","f":"4","g":"5","h":"6","i":"7","j":"8","k":"9","l":"J","m":"W","n":"Y","o":"V","p":"d","q":"t","r":"U","s":"K","t":"i","u":"z","v":"Q","w":"C","x":"r","y":"h","z":"b"," ": " ",".":".",":" :"e"}

outfile = open("info_security.txt",'r')

encrypt_file = outfile.read()

outfile.close()


encrypted_file = open("encrypted.txt","w")

for character in encrypt_file:

    for character in encrypt_file:
        encrypted_file.write(encryption[character])

encrypted_file.close()
        
    