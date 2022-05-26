import os
from tika import parser


def talk(text, voice="Milena"):
    print(text)
    os.system(f"say -v {voice} {text}")


raw = parser.from_file('sample.pdf')
talk(raw)
