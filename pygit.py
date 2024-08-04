import hashlib
import os

def init():
    os.makedirs(".pygit/objects", exist_ok=True)
    print("Initialized empty pygit repository in .pygit")

def hash_object(data, obj_type="blob"):
    obj = obj_type.encode() + b' ' + str(len(data)).encode() + b'\x00' + data
    oid = hashlib.sha1(obj).hexdigest()
    with open(f".pygit/objects/{oid}", "wb") as out:
        out.write(obj)
    return oid

def cat_file(oid, expected="blob"):
    with open(f".pygit/objects/{oid}", "rb") as f:
        obj = f.read()
    obj_type, _, content = obj.partition(b'\x00')[0].split()
    if obj_type.decode() != expected:
        raise ValueError(f"Expected {expected}, got {obj_type.decode()}")
    return content

def update_index(filename, oid):
    with open(".pygit/index", "a") as f:
        f.write(f"{oid} {filename}\n")

def write_tree():
    with open(".pygit/index") as f:
        entries = f.read().splitlines()
    tree = b""
    for entry in entries:
        oid, filename = entry.split()
        with open(filename, "rb") as f:
            data = f.read()
        tree += b'blob ' + oid.encode() + b' ' + filename.encode() + b'\x00' + data
    return hash_object(tree, "tree")

def commit(message, tree_oid, parent=None):
    commit = f"tree {tree_oid}\n"
    if parent:
        commit += f"parent {parent}\n"
    commit += f"\n{message}\n"
    return hash_object(commit.encode(), "commit")
