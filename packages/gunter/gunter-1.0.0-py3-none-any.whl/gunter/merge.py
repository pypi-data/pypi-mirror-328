from gunter.util import merge
import argparse

def main(*args):
    parser = argparse.ArgumentParser(description="GTRMerge - Merge 2 GTR Files")
    parser.add_argument("-1", "--gtr1", required=True, help="Path to the first GTR file")
    parser.add_argument("-2", "--gtr2", required=True, help="Path to the second GTR file")
    parser.add_argument("-o", "--out", required=True, help="Path to the output file")

    args = parser.parse_args(args)
    
    with open(args.gtr1, "r", encoding="utf-8") as f:
        g = f.read().splitlines()
    with open(args.gtr2, "r", encoding="utf-8") as f:
        h = f.read().splitlines()

    out = "\n".join(merge(g, h))
    with open(args.out, "w+", encoding="utf-8") as f:
        f.write(out)

if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])