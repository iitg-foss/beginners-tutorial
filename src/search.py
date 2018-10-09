from .utils import Folder, File


def main(folderName, query):

    if folderName:
        searchFolder = Folder(folderName)
    else:
        searchFolder = Folder("./test/test_corpus")

    results = searchFolder.searchEveryFile(query)

    return results
