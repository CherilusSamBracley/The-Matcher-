from pyfiglet import*
from termcolor import colored
import subprocess
import time

#Powered by Cherilus Sam Bracley
#December 30, 2020


class MATCHER:
    def __init__(self):
        self.module_name="Matcher"
        self.module_name_style= figlet_format(self.module_name)
        self.module_creator="Sam Bracley C"
        self.module_creator_contact="cherilussambracley@gmail.com"
        self.message="WELCOME TO THE"

        #WE SHOW THE MESSAGE AND THE MODULE NAME ON THE SCREEN WITH SOME OTHERS STUF
        print(self.message, self.module_name_style)

        print(colored("Creator name :", 'yellow'), self.module_creator, "\n")
        print(colored("Creator contact :", 'yellow'),self.module_creator_contact)

        self.functions=dict({
            colored("start    ", 'green'):" :to start the module \n",
          colored("clear  ", 'green'): "   :to clear the terminal \n",
          colored("exit    ", 'green'):"  :to leave the module \n ",
          colored("list    ", 'green'):"  :show you the command(s)list \n "
          
        })

        for a,b in self.functions.items():
            print("\n ",  a,b)


        self.START_MODULE=True

        while(self.START_MODULE):
            self.RESQUET=input(colored( "MATCHER>", 'blue' ))

            self.COMMAND_LIST=['start', 'exit', 'clear', 'list']


            if(self.RESQUET in self.COMMAND_LIST):
                pass
            else:
                error_msg="Command not found to see the command(s) use the list command {list}" 
                print(colored(error_msg, 'red').center(100))
                

            if(self.RESQUET == self.COMMAND_LIST[0]):
                print("You have two (2) sequences, twice to perform the test on these sequences \n")
        

                
                input_one=input("Please enter the first sequence \n")
                
                input_two=input("Please enter the second sequence \n")
               

                print("Waiting...")

                time.sleep(3)
                
                if(input_one == input_two):
                    print( colored("The sequences are the same", 'green'))
                            
                else:
                    
                    print( colored("The sequences are not the same", 'red'))



      
                
            if(self.RESQUET == self.COMMAND_LIST[1]):
                break


            if(self.RESQUET == self.COMMAND_LIST[2]):
                subprocess.call('clear',shell=True )


            if(self.RESQUET == self.COMMAND_LIST[3]):
                print(self.module_name_style)
                for a,b in self.functions.items():
                    print("\n ",  a,b)
                

start=MATCHER()
