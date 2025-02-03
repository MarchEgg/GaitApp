from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    result = anvil.server.call("predict", self.file_loader_1.file)
    if result:
      self.label_2.visible = True
      
      self.label_2.text = result

  

  def generateButtonClick(self, **event_args):
    """This method is called when the button is clicked"""
    img = False #anvil.server.call("generateAngleGraphs")
    if img:
      self.KneeImage.visible = True
      self.KneeImage.source = img
    self.graphsAllButton.background = app.theme_colors['Gray 30']
