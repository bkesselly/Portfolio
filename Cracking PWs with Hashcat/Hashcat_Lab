# Hash Cracking Lab with Hashcat

For this lab, I used **Kali Linux** in a VM that was part of a **NAT Network**.

## **Purpose**
The purpose of this lab is to create a set of hashes and use a dictionary to crack these hashes.

---
## **Steps**

### **1. Create the Hashes**
Run the following command to create a new `.txt` file and populate it with hashes:

```sh
cat << EOF > target_hashes.txt
```

---

### **2. Open Hashcat**
Use the following command to view the help screen for Hashcat:

```sh
hashcat -h
```

---

### **3. Choose a Wordlist**
I prefer using the **rockyou** wordlist. To locate it, use:

```sh
locate rockyou.txt
```

Most of the time, `rockyou.txt` is compressed as `.gz`, so you need to extract it using:

```sh
gunzip rockyou.txt.gz
```

This command will unzip the file and generate the required `.txt` file for Hashcat.

---

### **4. Run Hashcat**
First, navigate back to the home directory:

```sh
cd ~
```

Then, run the following command to crack the password hashes from the `.txt` file created in Step 1:

```sh
hashcat -m 0 -a 0 -o cracked.txt target_hashes.txt /usr/share/wordlists/rockyou.txt
```

#### **Breakdown of Options:**
- `-m 0` → Tells Hashcat we are cracking **MD5** hash types.
- `-a 0` → Specifies a **dictionary attack**.
- `-o cracked.txt` → Saves cracked passwords to an output file.
- `target_hashes.txt` → The file containing the hashes.
- `/usr/share/wordlists/rockyou.txt` → The wordlist used for the attack.

---

### **5. Read the Cracked Hashes**
Once the attack is complete, view the cracked passwords by running:

```sh
cat cracked.txt
```

This will display the cracked passwords in the terminal.

---

### **Final Notes**
This lab demonstrates the fundamentals of **hash cracking** using Hashcat and a wordlist attack. Be sure to use this knowledge responsibly and ethically.

**Author:** *Brian Kesselly*
