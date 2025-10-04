# Spiral Cipher — Solution Walkthrough

## Challenge Overview

The provided ciphertext was:

```
taskphaWL_PL4sOingpYefdngaP{_diddL40ap}y5rn_s1m37
```

The problem description indicated that this was a **Spiral Cipher** challenge.

The objective was to recover the exact original flag by reversing the spiral writing pattern used to encrypt it.

---

## Step 1: Determining the Structure

The ciphertext was **49 characters long**, which equals 7×7 — suggesting that the text was placed into a **7×7 grid** before being read in a spiral sequence.

---

## Step 2: Constructing the Grid

I arranged the ciphertext row-wise into a 7×7 matrix as follows:

```
t a s k p h a
W L _ P L 4 s
O i n g p Y e
f d n g a P {
_ d i d d L 4
0 a p } y 5 r
n _ s 1 m 3 7
```

This step assumed a left-to-right filling order, with each subsequent group of seven characters forming a new row.

---

## Step 3: Reading in Spiral Order

The next step was to traverse the grid **clockwise**, starting from the top-left corner and proceeding inwards in a spiral pattern. Reading the characters in this order produced the following text:

```
taskphase{4r73m1s_n0_fOWL_PL4YPL5y}paddingpadding
```

The tail section beyond the closing brace was clearly non-essential filler, serving only to complete the 7×7 grid.

---

## Step 4: Extracting the Flag

After trimming the extra padding, the flag is exactly:

```
taskphase{4r73m1s_n0_fOWL_PL4YPL5y}
```

---

## Final Answer

**Flag:** `taskphase{4r73m1s_n0_fOWL_PL4YPL5y}`

---
