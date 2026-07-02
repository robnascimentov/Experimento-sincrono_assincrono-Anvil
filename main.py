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

  # 2. Experimento Síncrono (Bloqueia a tela desativando os botões)
  @handle("btn_sincrono", "click")
  def btn_sincrono_click(self, **event_args):
    self.label_status.text = "Processando Áudio (Síncrono)..."
    self.btn_sincrono.enabled = False
    self.btn_assincrono.enabled = False
    self.btn_interativo.enabled = False
    time.sleep(5)
    self.btn_sincrono.enabled = True
    self.btn_assincrono.enabled = True
    self.btn_interativo.enabled = True
    self.label_status.text = "Áudio síncrono processado!"
