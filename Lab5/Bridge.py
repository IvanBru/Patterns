from abc import ABC, abstractmethod

class Render(object):

    def render_page(self):
        pass

class RenderHTML(Render):

    def render_page(self, page):
        print("HTML render")
        print(f"Class page: {page.classname}")

class RenderJSON(Render):

    def render_page(self, page):
        print("Json render")
        print(f"Class page: {page.classname}")

class RenderXML(Render):

    def render_page(self, page):
        print("XML render")
        print(f"Class page: {page.classname}")


class Renderer:

    def __init__(self, obj):
        self._obj = obj()

    def action(self, page):
        self._obj.render_page(page)