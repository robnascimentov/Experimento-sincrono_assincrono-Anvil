from ._anvil_designer import Form1Template
from anvil import *
import time

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  # 1. Testar Interatividade
  @handle("btn_interativo", "click")
  def btn_interativo_click(self, **event_args):
    if self.label_interativo.text == "Botão de teste clicado!":
      self.label_interativo.text = "Botão de teste clicado novamente!"
      self.label_interativo.foreground = "blue"
    else:
      self.label_interativo.text = "Botão de teste clicado!"
      self.label_interativo.foreground = "green"
