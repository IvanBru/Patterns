from abc import ABC, abstractmethod

class Page(ABC):

    def get_page(self):
        pass

class SimplePage(Page):
    classname = "SimplePage"

    def __init__(self, title):
        self.titile = title

    def get_page(self):
        print("Title", self.titile)

class ProductPage(Page):

    classname = "ProductPage"
    def __init__(self, name, description, img, id):
        self.name = name
        self.description = description
        self.img = img
        self.id = id

    def get_page(self):
        print(f" id: {self.id} \n  name: {self.name}\n description: {self.description}\n")