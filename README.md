# Enigma
A cryptography software for my final project. Transforms a file/input into a random encrypted code of arbitrary number. The catch is it would not produce the same code everytime, even with the same input. Misleadingly labeled as 'Hash-code/ function' at the software's documentation as back then I am yet to know what a hash code actually is.

Hash Function


This program is a hash function program called "Enigma" in reference to the German enigma machine, which is a ww2 encryption machine that produce different codes for the same text.

This program is similar if not improved. This program will produce different set of encrypted codes even for the same text. The amount of possible variation is arbitrary, but it is set as every odd number between 15 and 15555.

A number too large may crash the program, and even number may make the program easier to decipher.

The max length of text is also arbitrary, but it is set as 10^10 max possible characters.

The program first asks the user to input the text if the user wants to encrypt a text.

The program works by then converting the text to ASCII code, and the to binary. It is then combined. E.g. 1100110 101100 to 1100110101100

To separate it again the program needs to know one is the 7 and 6 digits and in which order

Therefore, a sequence is made behind the code

1100110101100 become 110011010110010 (notice the added 10 and the end)

‘1’ to indicate 7 digits while ‘0’ for 6 digits

To indicate which number is the actual code and the sequence, another code is added.

110011010110010 become 1100110101100102

The ‘2’ indicates that the last 3 values are not the code.

It is then timed by a secret number produced by the rand function.

e.g. if the secret code is 3

1100110101100102 become 3300330303300306

And then add the secret value behind

3300330303300306 become 33003303033003063 (notice the added ‘3’)

The secret code is randomly generated, and this program will only time the code by the value as different combinations have been tested and resulted in a crash.

The encrypted (hash) code is then stored in “morse.txt”

The decryption function is basically reversing the encryption function.

The secret code is then taken from the back and the rest of the code will be divided by the secret code.

Then the code is translated back.
