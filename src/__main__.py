from time import time

from src.app import main

if __name__ == "__main__":
    start_time = time()
    main()
    print("# --- %s seconds ---" % (time() - start_time))
