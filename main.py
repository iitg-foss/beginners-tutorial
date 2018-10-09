from src.search import main
from test.test import test
import sys

if len(sys.argv) > 1 and sys.argv[1] == 'test':

    test()

else:

    folderName = input("Enter dir path(default is ./test/test_corpus):\n")

    query = input("Enter search query:\n")

    results = main(folderName, query)

    for result in results:
        print("Found in file: " +
              result[0] +
              " at line " +
              str(result[1]) +
              ": " +
              result[2] +
              "\n")
