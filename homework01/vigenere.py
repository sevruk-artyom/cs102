def f1(m: str, k: str) -> str:
    if m.isupper():
        k *= len(m) // len(k) + 1
        a = ''.join([chr((ord(j) + ord(k[i])) % 26 + ord('A')) for i, j in enumerate(m)])
        return a
    else:
        k *= len(m) // len(k) + 1
        b = ''.join([chr((ord(j) - ord(k[i])) % 26 + ord('a')) for i, j in enumerate(m)])
        return b

print(f1("ATTACKATDAWN", "LEMON"))

def f2(n: str, k: str) -> str:
    if n.isupper():
        k *= len(n) // len(k) + 1
        c = ''.join([chr((ord(j) - ord(k[i])) % 26 + ord('A')) for i, j in enumerate(n)])
        return c
    else:
        k *= len(n) // len(k) + 1
        d = ''.join([chr((ord(j) - ord(k[i])) % 26 + ord('a')) for i, j in enumerate(n)])
        return d

print(f2("LXFOPVEFRNHR", "LEMON"))





