# small utilities, no deps

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def clamp(value, low, high):
    return max(low, min(value, high))

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

if __name__ == "__main__":
    print(clamp(9, 0, 22))
