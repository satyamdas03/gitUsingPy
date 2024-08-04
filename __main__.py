import sys
from pygit import init, hash_object, cat_file, update_index, write_tree, commit

def main(argv=sys.argv[1:]):
    if not argv:
        print("usage: pygit <command> [<args>]")
        return

    command = argv[0]

    if command == "init":
        init()
    elif command == "hash-object":
        if len(argv) != 2:
            print("usage: pygit hash-object <filename>")
            return
        with open(argv[1], "rb") as f:
            print(hash_object(f.read()))
    elif command == "cat-file":
        if len(argv) != 3:
            print("usage: pygit cat-file <type> <oid>")
            return
        print(cat_file(argv[2], argv[1]).decode())
    elif command == "update-index":
        if len(argv) != 3:
            print("usage: pygit update-index <filename> <oid>")
            return
        update_index(argv[1], argv[2])
    elif command == "write-tree":
        if len(argv) != 1:
            print("usage: pygit write-tree")
            return
        print(write_tree())
    elif command == "commit":
        if len(argv) != 3 and len(argv) != 4:
            print("usage: pygit commit <message> <tree-oid> [<parent-oid>]")
            return
        print(commit(argv[1], argv[2], argv[3] if len(argv) == 4 else None))
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
