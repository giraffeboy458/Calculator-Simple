#Hey person checking and hopefully not stealing my code. Don't touch these three lines, as they are used to run this program.
import math
import essential_modules
essential_modules.confirmation()

print('''Welcome to the Calculator: Simple program. 
      Operations:
      Addition: "add" or "+"
      Subtraction: "subt" or "-"
      Multiplication: "mult" or "*"
      Pure Division: "div" or "/" (don't even try dividing by zero)
      Quotient & Remainder Divison: "QR" or "//"
      Exponent: "exp" or "^" (please enter only integers, or you will get an inaccurate result.)
      Square Root: "sqrt" or "√"
      Factorial: "fact" or "!"(multiplies every natural number up until the number you input('''
      )
#Starts the infinite loop
while True:
    #Ask for continuing
    prompt = input('Do you wish to continue? "yes" or "no" ').lower()
    #Start the calculator if the answer is yes
    if prompt == 'yes':
        try:
            num1 = float(input('First number: '))
            oper = input('Operation: ')
            num2 = float(input('Second number: '))
            #Does a certain job depending on the operation
            if oper == 'add' or oper == '+':
                print(num1 + num2)
            elif oper == 'sub' or oper == '-':
                print(num1 - num2)
            elif oper == 'mult' or oper == '*':
                print(num1 * num2)
            elif oper == 'div' or oper == '/':
                print(num1 / num2)
            elif oper == 'QR' or oper == '//':
                print(num1 // num2)
                print(num1 % num2)
            elif oper == 'exp' or oper == '^':
                print(int(num1)**int(num2))
            elif oper == 'sqrt' or oper == '√':
                print(math.sqrt(num1))
                print('Number 2 is not required. If you were smart, you would know that')
            elif oper == 'fact' or oper == '!':
                print(math.factorial(num1))
                print('Number 2 is not required. Honestly, are you that dumb?')
            else:
                print('I will send you back to year 2 if you are being dumb.')
                continue
        except ZeroDivisionError:
            #Deals with dividing by zero
            print("Stop trying to get a zero divison error. WHat is wrong with you? You fool. I have already thought about this.")
            continue
        except ValueError:
            #Deals with wrong datatype
            print('Man, just enter a simple number. Is it that hard to follow instructions? I am 4 parallel universes ahead to your schemes.')
            continue
    elif prompt == 'no':
        print(
            "K bye, get snapped by Thanos or whatever, didn't ask + don't care + ratio"
        )
        break
    else:
        print('Please enter a valid prompt, like yes or no')
