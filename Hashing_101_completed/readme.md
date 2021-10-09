# Hashing_101 

```bash
Plaintext - Data before encryption or hashing, often text but not always as it could be a photograph or other file instead.

Encoding - This is NOT a form of encryption, just a form of data representation like base64 or hexadecimal. Immediately reversible.

Hash - A hash is the output of a hash function. Hashing can also be used as a verb, "to hash", meaning to produce the hash value of some data.

Brute force - Attacking cryptography by trying every different password or every different key

Cryptanalysis - Attacking cryptography by finding a weakness in the underlying maths

```


# What's a hash function?
Hash functions are quite different from encryption. There is no key, and it’s meant to be impossible (or very very difficult) to go from the output back to the input.

A hash function takes some input data of any size, and creates a summary or "digest" of that data. The output is a fixed size. It’s hard to predict what the output will be for any input and vice versa. Good hashing algorithms will be (relatively) fast to compute, and slow to reverse (Go from output and determine input). Any small change in the input data (even a single bit) should cause a large change in the output.

The output of a hash function is normally raw bytes, which are then encoded. Common encodings for this are base 64 or hexadecimal. Decoding these won’t give you anything useful.

Why should I care?
Hashing is used very often in cyber security. When you logged into TryHackMe, that used hashing to verify your password. When you logged into your computer, that also used hashing to verify your password. You interact indirectly with hashing more than you would think, mostly in the context of passwords.

What's a hash collision?
A hash collision is when 2 different inputs give the same output. Hash functions are designed to avoid this as best as they can, especially being able to engineer (create intentionally) a collision. Due to the pigeonhole effect, collisions are not avoidable. The pigeonhole effect is basically, there are a set number of different output values for the hash function, but you can give it any size input. As there are more inputs than outputs, some of the inputs must give the same output. If you have 128 pigeons and 96 pigeonholes, some of the pigeons are going to have to share.

MD5 and SHA1 have been attacked, and made technically insecure due to engineering hash collisions. However, no attack has yet given a collision in both algorithms at the same time so if you use the MD5 hash AND the SHA1 hash to compare, you will see they’re different. The MD5 collision example is available from https://www.mscs.dal.ca/~selinger/md5collision/ and details of the SHA1 Collision are available from https://shattered.io/. Due to these, you shouldn't trust either algorithm for hashing passwords or data.


# Here's a quick table of the most Unix style password prefixes that you'll see.
```bash
Prefix	Algorithm
$1$	md5crypt, used in Cisco stuff and older Linux/Unix systems
$2$, $2a$, $2b$, $2x$, $2y$	Bcrypt (Popular for web applications)
$6$	
sha512crypt (Default for most Linux/Unix systems)
```
