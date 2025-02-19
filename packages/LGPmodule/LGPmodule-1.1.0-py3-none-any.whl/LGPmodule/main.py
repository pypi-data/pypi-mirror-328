from sys import exit
from builtins import print as dprint

lgp_default_icons = {
  "i": "",
  "d": "",
  "w": "",
  "e": "",
  "c": "",
  "t": ""
}

COLORS = {
  "i": "\033[36m",
  "d": "\033[32m",
  "w": "\033[33m",
  "e": "\033[31m",
  "c": "\033[35m",
  "t": "\033[0m"
}

def bold(text:str, start:str="<b>", end:str="</b>") -> str:
  return text.replace(start, "\033[1m").replace(end, "\033[22m")

def print(text="", mode:str="t", icon=None):
  global lgp_default_icons, COLORS
  color = COLORS.get(mode[0], "")
  icon = icon if icon else lgp_default_icons.get(mode[0], lgp_default_icons.get(mode))

  if isinstance(text, str):
    text = bold(text)

  dprint(color+icon+text+COLORS["t"])

def info(message:str, icon=None):
  print(message, "i", icon)

def debug(message:str, icon=None):
  print(message, "d", icon)

def warn(message:str, icon=None):
  print(message, "w", icon)

def error(message:str, icon=None):
  print(message, "e", icon)

def critical(message:str, icon=None, exit_code:int=1):
  print(message, "c", icon)
  if exit_code:
    exit(exit_code)