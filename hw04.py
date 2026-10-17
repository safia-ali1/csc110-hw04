# ------------------------------------------------------
#        Name: (Safia)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ This code looks at a sentence from the user.
        The first if statement checks if the secret word is in the sentence
        and the second if statement checks if dog/Dog is in the sentence.
        If neither statements are true, it prints try again.  """
    sentence=input("Give me a sentence:")
    
    if secret_word in sentence:
     print ("You used the secret word!")
     return
     
    elif  "dog" in sentence or "Dog" in sentence:
     print ('You used the word "dog" or the word "Dog"!')
     return
     
    
    else :
     print ("Try again")
     
    pass
    


# Task 2
def check_greater():
    """ This code looks at two integers from the user
        and if the first integer is bigger it prints first is greater
        but if the second integer is bigger it prints second is greater.
        If neither is bigger,it prints try again """
    num1=int(input("Give me a first integer: "))
    num2=int(input("Give me a second integer: "))
             
    if num1>num2:
        print("First is Greater")
        return
    elif num2>num1:
        print("Second is Greater")
        return
    else:
        print("Try again")
        return
    pass


# Task 3
def get_special_numbers():
    
    """ this code looks at all numbers between 1 and 41(not including 41)
        and if it is an even number,not a multiple of 3 or a multiple of 5,
        it discards the number and
        continues the loop with the next number until it reaches 40. """

    for i in range(1,41):
    
        if i%2==0:
         continue
        elif i%3!=0:
         continue
        elif i%5==0:
         continue
        else:
         print(i)   
    
    pass

# Task 4.a
def my_for_loop():
    """ Add your docstring """
    word=(input("Give me a string:"))

   
    if len(word)>5 or len(word)<2:
         print("bad word")
         return
    
    elif " " in word:
         print("bad word")
         return

    for letter in word:
       if letter in "AEIOUaeiou": 
         print("letter", letter, "is a vowel")
         
       else:
         print("letter", letter, "is a consonant")

    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    while True:
        choice=input("Choose one option: a, b, or c:")
        if choice=='a':
         continue
        elif choice=='b':
         print("Goodbye")
         return
        elif choice=='c':
         sys.exit()
        else:
         print("try again")
         continue

    pass

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
