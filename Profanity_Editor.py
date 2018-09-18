import urllib

def read_text():
    text = open(r"C:\Users\rahaf\OneDrive\Desktop\rahaf.txt")
    contents = text.read()
    print(contents)
    text.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection=urllib.urlopen()
    output=connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly")
    
    
    
    
read_text()
    
    
    
