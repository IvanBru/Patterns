from Bridge import *
from page import *

page1 = SimplePage("Education")
page2 = ProductPage("Pen", "Simple writing", "img.jpg", 1)

rendererHTML = Renderer(RenderHTML)
rendererXML = Renderer(RenderXML)
rendererJson = Renderer(RenderJSON)

rendererHTML.action(page1)
rendererXML.action(page1)
rendererHTML.action(page1)

rendererHTML.action(page2)
rendererXML.action(page2)
rendererHTML.action(page2)

