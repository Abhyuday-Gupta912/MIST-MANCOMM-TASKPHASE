# LINUX LUMINARIUM WRITEUPS

---

## MULTIPLE GLOBBING

### FLAG:

`pwn.college{gFYg2ee-hfk-QA4PQatzKIcI2ZO.QXycTO2EDLycTN0czW}`

### APPROACH USED:

```bash
cd /challenge/files
/challenge/run *p*
```

I navigated to the `/challenge/files` directory and used the glob pattern `*p*` to match all files containing the letter 'p'. The `*` wildcard matches any characters, so this pattern selected multiple files at once and passed them as arguments to `/challenge/run`.

---

## SPLIT-PIPING STDERR AND STDOUT

### FLAG:

`pwn.college{wPk12mihqrVaJNNYT2v8pgksIcj.dFDNwYDLycTN0czW}`

### APPROACH USED:

```bash
/challenge/hack > >(/challenge/planet) 2> >(/challenge/the)
```

I used process substitution to redirect stdout and stderr to different commands. `> >(/challenge/planet)` sends stdout to `/challenge/planet`, while `2> >(/challenge/the)` sends stderr (file descriptor 2) to `/challenge/the`. This allowed me to split the outputs simultaneously.

---

## SNOOPING ON CONFIGURATIONS

### FLAG:

`pwn.college{MSb6Bwdpjuu8_5bZd2FPGrMiDmV.QXyQTM3EDLycTN0czW}`

### APPROACH USED:

```bash
cat /home/zardus/.bashrc
export FLAG_GETTER_API_KEY=sk-359624371
flag_getter --key $FLAG_GETTER_API_KEY
```

I read zardus's `.bashrc` file using `cat` since it's world-readable by default. Found the API key at the end of the file, exported it to my environment, and then ran `flag_getter` with the stolen key to get the flag.
