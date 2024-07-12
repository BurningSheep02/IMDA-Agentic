from FileReader import FileReader
from FilterAgent import FilterAgent
from Summariser import Summariser

summariser = Summariser()
TARGET_PERSON = "Mao Zedong"

res = []

summary = summariser.summarise(res,TARGET_PERSON)
print("""\n\nResult:\n\n""")
print(summary)
