# IntPhys-verify-quadruplets

Download dev set from `www.intphys.com`:

```
wget https://download.intphys.com/dev.tar.gz
```

Extract it:

```
tar -xzvf dev.tar.gz
```

Verify dataset:

```
python verify_matched_quadruplets.py dev
```

It should return:

```
dev/O1
30it [01:43,  3.45s/it]
Success: 1.0
dev/O2
30it [01:49,  3.63s/it]
Success: 1.0
dev/O3
30it [01:45,  3.52s/it]
Success: 1.0
```



