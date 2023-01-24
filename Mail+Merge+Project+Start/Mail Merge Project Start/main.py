#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("E:/Rajthilak/Python/Trial and error/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as f:
    names = f.readlines()

with open("E:/Rajthilak/Python/Trial and error/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as j:
    data = j.read()
    for txt in names:
        x = txt.strip()
        y = data.replace("[name]", x)
        with open("E:/Rajthilak/Python/Trial and error/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_" + x.rstrip() + ".txt", "w") as i:
            i.write(y)
            i.close()
 
