# Emoji Cipher Challenge — Writeup

## Challenge Context

This challenge involved a file named `book.txt`, which contained nothing but emojis arranged in paragraphs and dialogue-like lines. The structure suggested that it might be an encoded novel. The task was to determine the name of the book and its author.

The hint mentioned **frequency analysis**, implying that each emoji represented one English letter — a **monoalphabetic substitution cipher**.

## Step 1: Inspecting the File

Opening the file revealed structured text with paragraph breaks and em dashes, suggesting that the content was a continuous narrative rather than random characters. This pointed toward an English literary text that had been converted into emojis using a one-to-one substitution scheme.

## Step 2: Frequency Analysis

A frequency count of the emojis was the logical first step. In English, letters follow a well-known frequency pattern, roughly:

E, T, A, O, I, N, S, H, R, D, L, U, C, M, F, Y, W, G, P, B, V, K, X, Q, J, Z.

The top few emojis in the file were:

| Rank | Emoji |   Count |
| ---- | :---: | ------: |
| 1    |  😍   | 141,404 |
| 2    |  🤡   | 100,184 |
| 3    |  😙   |  93,102 |
| 4    |  🥶   |  91,348 |
| 5    |  👂   |  81,363 |

The assumption was that these corresponded respectively to E, T, A, O, and I.

## Step 3: Substitution and Partial Decoding

Using this mapping, I replaced the most frequent emojis with their estimated English letters. The initial output contained recognizable word structures but was not fully readable yet. Some sections resembled:

> STATEDG, PDUCP BUMV CUDDIFAN MACE ...

This confirmed that the direction was correct and that manual refinement would likely reveal meaningful text.

## Step 4: Refinement of the Mapping

By analyzing likely word structures and letter pair patterns, I made several swaps to improve the text:

- Swapping Y and W corrected instances of the word “WITH”.
- Swapping F and G revealed words such as “GOLD POINTS” and “STRONG”.

After these adjustments, the decoded output began with:

> “STATELY, PLUMP BUCK MULLIGAN CAME FROM THE STAIRHEAD, BEARING A BOWL OF LATHER ON WHICH A MIRROR AND A RAZOR LAY CROSSED.”

## Step 5: Identifying the Book

A quick search of this sentence showed that it is the opening line of _Ulysses_ by **James Joyce**. This confirmed that the encoded text was a direct emoji-to-letter substitution of that book.

## Final Answer

**Book:** _Ulysses_
**Author:** _James Joyce_
**Cipher Type:** Emoji-based monoalphabetic substitution
**Technique Used:** Frequency analysis with iterative refinement

## Python Script Used

```python
import sys, re
from collections import Counter

freq_order = "ETAOINSHRDLUCMFWYGPBVKXQJZ"

emoji_order_guess = None
mapping = {}

def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def find_emojis(s):
    pat = re.compile(r'[\U0001F300-\U0001FAFF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF]')
    return pat.findall(s)

def build_mapping(text, top=26):
    global emoji_order_guess, mapping
    ems = find_emojis(text)
    counts = Counter(ems).most_common(top)
    emoji_order_guess = [e for e,_ in counts]
    mapping = {e:l for e,l in zip(emoji_order_guess, freq_order)}

def substitute(text):
    return ''.join(mapping.get(ch, ch) for ch in text)

def main():
    if len(sys.argv) < 2:
        print("usage: python emoji_subst_decode.py book.txt")
        return
    txt = read_text(sys.argv[1])
    build_mapping(txt, top=26)
    preview = substitute(txt[:8000])
    print(preview)

if __name__ == "__main__":
    main()
```
