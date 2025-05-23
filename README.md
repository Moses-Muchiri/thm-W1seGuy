# TryHackMe: W1seGuy - XOR Decryption Writeup

## Room URL
[https://tryhackme.com/room/w1seguy](https://tryhackme.com/room/w1seguy)

## Description

The W1seGuy room is a reverse engineering and crypto challenge focused on XOR encryption. The goal is to decrypt a hex-encoded, XOR-encrypted string where we know the plaintext starts with a common pattern (`THM{`) and ends with `}`.

---

## Key Concepts

- **XOR Encryption:** A symmetric encryption method where each byte of the message is XORed with a key byte.
- **Known Plaintext Attack:** We know what the message starts and ends with (`THM{...}`), which we use to derive parts of the XOR key.
- **Repeating Key:** The key is shorter than the message and repeats throughout encryption.

---

## Provided Python Script

We a following Python script to:
1. Derive the key using the known start (`THM{`) and end (`}`) of the flag.
2. Decrypt the full message using the full key.

## Usage Example
Step 1: Run the script with the encrypted message and assumed key length(It's explicitly stated that the key has 5 characlers so you could use the script as is or comment out the corresponding line.)
```bash
python3 app.py 48656c6c6f54684d7b536d6172744765793132337d 5
```
Step 2: Script Output
```bash
Derived start of the key: S0m3
Derived end of the key: G3y!
Fully derived key: S0m3G3y!
Decrypted message: THM{SmartKey123}
```

## Final Flag
```bash
THM{SmartKey123}
```

