import sys
import time

def main(epoch):
    print("timestamp: {}".format(epoch))
    gmtime = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(epoch)))
    print("Commit pushed at: {}".format(gmtime))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Give exactly 1 arguments")
        sys.exit(1)
    main(sys.argv[1])
