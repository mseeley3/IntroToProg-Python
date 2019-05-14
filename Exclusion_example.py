# --------------------------------#
# Title: "Exclusion Example"
# Dev: mseeley3
# Date: 5/13/19
# Changelog: (Who, When, What)
# mseeley3,5/13/19, Created Script
# find gihub repository here: https://github.com/mseeley3/IntroToProg-Python
# --------------------------------#

# -------------Input/Output----------- #

# create an object to store the ASCII art
bulbasaur = """
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       \.\\
       ____      |___._.  |       __               \ `.
     .'    `---""       ``"-.--"'`  \               .  \\
    .  ,            __               `              |   .
    `,'         ,-"'  .               \             |    
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .'\'   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / \ `        `.    .      .'/
 j|:D  \          `--'  ' ,'_  . .         `.__, \   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  """""'                    '
bulbasaur_2 = """"                                  
 '.                                 .    `.   _,..  ')
  \,_   .    .                _,-'/    .. `,'   __
    ) \`._        ___....----"'  ,'   .'  \ |   '  \  .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'
 `"^--'..'   '-`-^-'"--    `-^-'`.''"""""'.,^.`.'

# display the art
print(bulbasaur)
print(bulbasaur_2)

# display welcome message and question to user
print("Welcome to the Pokemon Center. This is a Bulbasaur. How many would you like?")

# -------------Processing------------- #
while(True):
    try:
        # the int() requires the user to input a number
        number = int(input())
        print("Your " + str(number) + " bulbasaurs are waiting for you at the Pokemon Center.")
        break

    # if the user inputs something other than a whole number (integer)
    # python will be unable to run the int() function and the script will fail
    # capture this failure with the except construct
    except:
        # tell the user what is wrong with their input
        print("Please provide a whole number.")
