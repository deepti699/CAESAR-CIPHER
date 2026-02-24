alphabet  =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

direction = input("type encode to encrypt and decode to de-crypt")

text = input("type your message")

shift = int(input("enter the number of times to be shifted"))

def encrypt (original_text,shift_amount):

     up = " "
     for letter in original_text:


         shift_ted = alphabet.index(letter) + shift_amount

         up += alphabet(shift_ted)

      print(up)

def de_crypt (original_text,shift_amount):
   
        up = " "

        for letter in original_text:

             shift_ted = alphabet.index(letter) - shift_amount
      
              up += alphabet(shift_ted)

        print(up)

if direction == "encode":

   encrypt(text,shift)

else:

    decrypt(text,shift)

print("do you want to continue??..yes or no??")

y = input()

if y == "yes":

  direction = input("type encode to encrypt and decode to de-crypt")

  text = input("type your message")

  shift = int(input("enter the number of times to be shifted"))

  if direction == "encode":

     encrypt(text,shift)

  else:

      decrypt(text,shift)

else:

  print("byeee")

   

  

  

  












       







         


















