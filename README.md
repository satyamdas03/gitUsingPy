# pygit

A simple implementation of Git using Python.

## Commands

- `init` - Initialize a new repository.
- `hash-object <filename>` - Hash an object and store it in the object database.
- `cat-file <type> <oid>` - Display the content of an object.
- `update-index <filename> <oid>` - Add a file to the index.
- `write-tree` - Write the current index as a tree object.
- `commit <message> <tree-oid> [<parent-oid>]` - Commit a tree object.

## Example Usage

```sh
$ pygit init
$ pygit hash-object example/sample.txt
$ pygit cat-file blob <oid>
$ pygit update-index example/sample.txt <oid>
$ pygit write-tree
$ pygit commit "Initial commit" <tree-oid>
```
