from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  
  fitLine = False
  norm = False
  curDis = None

  
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
    anvil.server.call("initDataList")
    hipImg = anvil.server.call("createGraph")
    kneeImg = anvil.server.call("createGraph", "Knee")
    ankleImg =  anvil.server.call("createGraph", "Ankle")
    self.curDis = "All"
    if hipImg:
      self.HipImage.visible = True
      self.HipImage.source = hipImg
    if kneeImg:
      self.KneeImage.visible = True
      self.KneeImage.source = kneeImg
    if ankleImg:
      self.AnkleImage.visible = True
      self.AnkleImage.source = ankleImg
    self.graphsAllButton.background = app.theme_colors['ButtonSelect']
    self.graphsKneeButton.background = app.theme_colors['White']
    self.graphsHipButton.background = app.theme_colors['White']
    self.graphsAnkleButton.background = app.theme_colors['White']

  



  
  def clickGraphAllButton(self, **event_args):
    self.curDis = "All"
    self.graphsAllButton.background = app.theme_colors['ButtonSelect']
    self.graphsKneeButton.background = app.theme_colors['White']
    self.graphsHipButton.background = app.theme_colors['White']
    self.graphsAnkleButton.background = app.theme_colors['White']

    hipImg = anvil.server.call("createGraph", "Hip", self.fitLine, self.norm, self.GraphCard.width)
    kneeImg = anvil.server.call("createGraph", "Knee", self.fitLine, self.norm)
    ankleImg =  anvil.server.call("createGraph", "Ankle", self.fitLine, self.norm)
    if hipImg:
      self.HipImage.visible = True
      self.HipImage.source = hipImg
    if kneeImg:
      self.KneeImage.visible = True
      self.KneeImage.source = kneeImg
    if ankleImg:
      self.AnkleImage.visible = True
      self.AnkleImage.source = ankleImg


  def clickGraphKneeButton(self, **event_args):
    self.curDis = "Knee"
    self.graphsAllButton.background = app.theme_colors['White']
    self.graphsKneeButton.background = app.theme_colors['ButtonSelect']
    self.graphsHipButton.background = app.theme_colors['White']
    self.graphsAnkleButton.background = app.theme_colors['White']
    
    kneeImg = anvil.server.call("createGraph", "Knee", self.fitLine, self.norm)
    self.HipImage.visible = False
    self.AnkleImage.visible = False
    if kneeImg:
      self.KneeImage.visible = True
      self.KneeImage.source = kneeImg
    

  def clickGraphHipButton(self, **event_args):
    self.curDis = "Hip"
    self.graphsAllButton.background = app.theme_colors['White']
    self.graphsKneeButton.background = app.theme_colors['White']
    self.graphsHipButton.background = app.theme_colors['ButtonSelect']
    self.graphsAnkleButton.background = app.theme_colors['White']

    hipImg = anvil.server.call("createGraph", "Hip", self.fitLine, self.norm)
    self.KneeImage.visible = False
    self.AnkleImage.visible = False
    if hipImg:
      self.HipImage.visible = True
      self.HipImage.source = hipImg

  def clickGraphAnkleButton(self, **event_args):
    self.curDis = "Ankle"
    self.graphsAllButton.background = app.theme_colors['White']
    self.graphsKneeButton.background = app.theme_colors['White']
    self.graphsHipButton.background = app.theme_colors['White']
    self.graphsAnkleButton.background = app.theme_colors['ButtonSelect']
    ankleImg = anvil.server.call("createGraph", "Ankle", self.fitLine, self.norm)
    self.KneeImage.visible = False
    self.HipImage.visible = False
    if ankleImg:
      self.AnkleImage.visible = True
      self.AnkleImage.source = ankleImg

  def updateImg(self):
    if self.curDis == "Hip":
      self.clickGraphHipButton()
    if self.curDis == "Ankle":
      self.clickGraphAnkleButton()
    if self.curDis == "Knee":
      self.clickGraphKneeButton()
    if self.curDis == "All":
      self.clickGraphAllButton()

  def clickBestFitButton(self, **event_args):
    self.fitLine = not self.fitLine

    if self.fitLine:
      self.bestFitLine.background = app.theme_colors['ButtonSelect']
    else:
      self.bestFitLine.background = app.theme_colors['White']
    self.updateImg()

  def clickNormRef(self, **event_args):
    self.norm = not self.norm

    if self.norm:
      self.normRef.background = app.theme_colors['ButtonSelect']
    else:
      self.normRef.background = app.theme_colors['White']
    self.updateImg()

  
    

