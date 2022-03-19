import datetime
x = datetime.datetime.now()

def getname():
    formatname(input("\nEnter the known name: ")) # Gets the name from user and call the formartname() function

def formatname(name):
    if(len(name) == 0): # If no name is given, it name paramater in getyear() function is set to 1
        print("\nNo Name entered using default wordlist, please be noted that it may huge take some time to generate and as well as cracking")
        getyear(1)
    else:
        name = name[0:4]  # If the user inputs full name, we will just take first 4 letters
        name = name.upper() # Converting the input to uppercase
        if name.isalpha(): # Allows only if the first 4 characters is alphabetics.
            getyear(name)
        else:
            print("\nPlease enter only alphabetical characters") # If not, prompt the user to enter name again
            getname()

def getyear(name):
    startyear= input("\nEnter the start year: ")
    if startyear.isdecimal() or len(startyear)==0:
        if len(startyear)!=4 or int(startyear)<=1899 or int(startyear)>x.year: # Allows only if the year contains 4 digits, start year is after 1899 and also after the current year or uses the default year 1900
            startyear= defaultstartyear()
    else:
        startyear = defaultstartyear() 
    endyear= input("\nEnter the end year: ")
    if endyear.isdecimal():
        if len(endyear)!=4 or int(endyear)<1899 or int(endyear)>x.year:# Allows only if the year contains 4 digits, end year is after 1899 and also after the current year or uses the current year
            print(f"\nInvalid end year, using default value {x.year}")
            endyear= defaultendyear()
    else:
        endyear = defaultendyear()
    createwordlist(name,startyear,endyear) # create wordlist

def defaultstartyear():
    print("\nInvalid start year, using default value 1900")
    return 1900

def defaultendyear():
    print(f"\nInvalid end year, using default value {x.year}")
    return x.year




def createwordlist(name,startyear,endyear):
    if name == 1:# If name is 1, which was given in formatname() use the deault wordlist
        try:
            template_file = open('default.txt','r')
            filename = input("\nEnter the output filename : ")
            file = open(filename+".txt",'w')
            for i in template_file:
                for j in range(int(startyear),int(endyear)+1):
                    file.write(i.strip()+str(j)+"\n")
            print(f"\nSuccess, wordlist generated with the filename {filename}.txt")
        except:
            print("\nNo default text file found, please download default text file or enter the 4 digit starting letters.")
            exit()
    else: # Else create new wordlist with given name
        file = open(name+'.txt','w')
        if len(name)!=4: # If the user did not know all the 4 letters, autocompleting with possible letters
            try:
                template_file = open('default.txt','r')
                print(f"\nPartial name is entered, creating wordlist with name that might start with {name}.")
                for i in template_file:
                    for j in range(int(startyear),(int(endyear)+1)):
                        if i.strip().startswith(name):
                            file.write(i.strip()+str(j)+"\n")
                print(f"\nSuccess, wordlist generated with the filename {name}.txt")
            except:
                print("\nNo default text file found, please download default text file or enter the 4 digit starting letters.")
                exit()
        else: # If the user entered all the 4 letters, just append the year in string
            for i in range (int(startyear),(int(endyear)+1)):
                file.write(name+str(i)+"\n")
            print(f"\nSuccess, wordlist generated with the filename {name}.txt")

getname() # Trigger the whole script by calling the getname() function