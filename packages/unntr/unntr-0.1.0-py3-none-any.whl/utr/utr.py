import os,sys
def replace(i, o, f):
    with open(f, 'w') as f:
        lines = f.read().replace(o, i)
    os.remove(f)
    with open(f, 'w') as f:
        f.write(lines)
def main():
    if len(sys.argv) > 4:
        print("usage: ufr <file> <old text> <new text>")
        sys.exit(1)
    try:
        replace(sys.argv[3], sys.argv[2], sys.argv[1])

    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
