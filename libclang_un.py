from clang.cindex import Index

index = Index.create()
tu = index.parse("hello.c")
for node in tu.cursor.walk_preorder():
    print(node.kind , node.spelling)