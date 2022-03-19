# E-Aadhaar PDF password list generator
## _Generate possible wordlist for cracking E-Aadhaar's PDF hash_

> This is script is based on the password convention on E-Aadhaar. The password for the pdf would be combination of the first 4 letters of name in CAPITAL and the year of birth (YYYY) as password. So, this would just exploit the way they implemented the default password mechanism and not actual Aadhaar. Also please note this works only if you found any person's E-Aadhaar which is already downloaded.

### How it works?
You can open the PDF if you know the name of the person and the year they born, but what if you have access to E-Aadhaar PDF but protected with default password and you don't to whom it does belong?

We create all the possible 4 letter characters and then append with the year based on user input. Example, the password template file named `default.txt` in this repository contains all the possible combination of Alphabetical Characters `A-Z` in the first 4 letters. i.e., `AAAA` to `ZZZZ`. If the user knows partial letters or year, they can use that to limit the wordlist based on their requirements. 

### Features

- Create a wordlist that surely contains a password to crack the hash, even if you don't know name or year
- Customize wordlist if you know the full name or partial name
- Customize wordlist if you whether know the year or not

This is a very lightweight and simple that helps to create the wordlist, once done you could use that in John (JohnTheRipper) 

### Usage

>Clone this repository
```
git clone https://github.com/sathyanarayanab/E-Aadhaar-PDF-password-list-generator.git
```
> Head to the cloned directory
```
cd E-Aadhaar-PDF-password-list-generator
```
> Run the `main.py` file
```
python main.py
```
```
    
1. Enter the name or leave it empty to use default wordlist
   ➡ You can also enter partial name up to your knowledge, if you know the person but not sure
   ➡ If left empty it prompts for output filename
   
2. Enter the Start year 
   ➡ You can also leave it empty if unknown
   
3. Enter the End year 
   ➡ You can also leave it empty if unknown
   
```