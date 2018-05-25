import random
import os
i = random.randrange(19) + 1 
website="https://raw.githubusercontent.com/andreaspreuss/ascii-bash-splash/art/"+ str(i) + ".txt"
os.system("curl " +  website)
