
import os
import re


class Folder:

    def __init__(self, path):
        self.path = path
        self.name = path.split('/')[-1]

    def searchEveryFile(self, query):

        searchResults = []

        for dirname, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                file = File(os.path.join(dirname, filename))
                result = file.search(query)
                if result:
                    searchResults.extend(file.search(query))

        return searchResults


class File:

    def __init__(self, path):
        self.path = path
        self.name = path.split('/')[-1]

    def search(self, query):

        searchResults = []

        with open(self.path, 'r') as file:
            lines = file.read().split("\n")
            searchResults.extend([
                [self.name, i+1, line.replace(query, query.upper())]
                for i, line in enumerate(lines) if query.casefold() in line.casefold()])

        return searchResults

