# Crypto

Some functions to do with crypanalysis

Since this is taking an extremely long time to
do anything, starting with some real simple stuff

The first idea was to jump in and try to write a 
cryptanalysis of simple substitution ciphers. This
is quite challenging even so.

There is a function to calculate letter frequencies
for English, using the entirety of the NLTK Brown
corpus.

To start working, you need to ciphertext examples,
and I couldn't find a library of those, so I
added functionality to generate my own, and
that's where the code has gotten to.

There is a function to generate a random substitution
alphabet, and a function to encrypt plaintext using that

Random paragraphs from the Brown corpus can then 
be encrypted using this.
