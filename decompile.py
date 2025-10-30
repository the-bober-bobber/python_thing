import pygetsource
import marshal

file_to_decompile = 'Mario_executable.pyc'

try:
    with open(file_to_decompile, 'rb') as f:
        # Skip the 16-byte .pyc header
        f.seek(16)  
        code_obj = marshal.load(f)

    source_code = pygetsource.getsource(code_obj)

    with open('Mario_executable.DECOMPILED.py', 'w') as out_f:
        out_f.write(source_code)

    print(f"Success! Decompiled code saved to 'Mario_executable.DECOMPILED.py'")

except Exception as e:
    print(f"Decompilation failed: {e}")
    print("This file might be encrypted or use unsupported features.")