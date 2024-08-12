import random
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'password-holder.txt')

lowerchars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperchars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
specialchars = ['!','~','`','!','#','$','%','^','&','*','_']
numerricchars = ['1','2','3','4','5','6','7','8','9','0']

print("""
\033[32m
########     ###     ######   ######  ##      ##  #######  ########  ########         
##     ##   ## ##   ##    ## ##    ## ##  ##  ## ##     ## ##     ## ##     ##        
##     ##  ##   ##  ##       ##       ##  ##  ## ##     ## ##     ## ##     ##        
########  ##     ##  ######   ######  ##  ##  ## ##     ## ########  ##     ##        
##        #########       ##       ## ##  ##  ## ##     ## ##   ##   ##     ##        
##        ##     ## ##    ## ##    ## ##  ##  ## ##     ## ##    ##  ##     ##        
##        ##     ##  ######   ######   ###  ###   #######  ##     ## ########         
 ######   ######## ##    ## ######## ########     ###    ########  #######  ########  
##    ##  ##       ###   ## ##       ##     ##   ## ##      ##    ##     ## ##     ## 
##        ##       ####  ## ##       ##     ##  ##   ##     ##    ##     ## ##     ## 
##   #### ######   ## ## ## ######   ########  ##     ##    ##    ##     ## ########  
##    ##  ##       ##  #### ##       ##   ##   #########    ##    ##     ## ##   ##   
##    ##  ##       ##   ### ##       ##    ##  ##     ##    ##    ##     ## ##    ##  
 ######   ######## ##    ## ######## ##     ## ##     ##    ##     #######  ##     ## 

           
                                                                 """)

platform = input("\033[37mWhat would you like to use this password for?\n")
platform = platform.upper()
print("\033[32mCreating password for " + platform)

password_first = random.choice(lowerchars) + random.choice(upperchars) + random.choice(specialchars) + random.choice(numerricchars) 
password_second = random.choice(lowerchars) + random.choice(upperchars) + random.choice(specialchars) + random.choice(numerricchars)
password_third = random.choice(numerricchars) + random.choice(lowerchars) + random.choice(upperchars) + random.choice(specialchars)
storedPass = password_first + password_second + password_third
password = platform + ": " + "\033[32m" + password_first + password_second + password_third

if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        pass

updated_lines = []
with open(file_path, 'r') as passwordHolder:
    lines = passwordHolder.readlines()
    platform_found = False
    for line in lines:
        if line.startswith(platform + ":"):
            updated_lines.append(f"{platform}: {storedPass}\n")
            platform_found = True
        else:
            updated_lines.append(line)
    if not platform_found:
        updated_lines.append(f"{platform}: {storedPass}\n")

with open(file_path, 'w') as passwordHolder:
    passwordHolder.writelines(updated_lines)

print("\033[32mStoring password in notepad...")
print("\033[37mYour password for " + platform + " is: \033[32m" + storedPass)
print("\033[37m")