import sys

def main(timestamp):
    print("timestamp: {}".format(timestamp))
    assert False, {timestamp}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Give exactly 1 arguments")
        sys.exit(1)
    main(sys.argv[1])
