from pathlib import Path
from bs4 import BeautifulSoup
import json
import re

class Res_Paper:
    
    def __init__(self, path):
        self.path = path
        self.json = json.load(open(path,encoding= "utf-8"))
        self.title = self.json['articleTitle']
        self.number = self.json['articleNumber']
        self.authors = self.json['authors']
        self.abstract = self.json['abstract']
        self.text = self.get_text()


    def __repr__(self):
        return f'{self.title}'

    def get_text(self):
        text = self.abstract + '\n' + "\n".join([p.text for p in BeautifulSoup(self.json['xml'], features = "xml").find_all('p')])
        return self.clean_text(text)

    def clean_text(self, text:str) ->str:
        regex = r"CCBY - IEEE.*|\[\d+\]|\$.*\$|View Source.*|\\begin.*|FIGURE \d+|Fig. \d+|[^A-Za-z0-9^ ]|SECTION [A-Z]+|\t\t|\n|Eq \d+|  "
        regex_empty = r" +"
        regex_eqns = r"Eq \d+|Lemma \d+|section \d+|section \d+ \d+|From \d+|Eqs[^a-z^A-Z]+"
        result = re.sub(regex, " ", text, 0, re.MULTILINE)
        result = re.sub(regex_empty, " ", result, 0, re.MULTILINE)
        result = re.sub(regex_eqns, "", result, 0, re.MULTILINE).strip()
        return result

def getData(path_to_data):
    papers = []
    for path in Path(path_to_data).rglob('*.json'):
        try:
            paper = Res_Paper(path)
            papers.append(paper)
        except Exception as e:
            print(f"Error processing file {path}: {e}")
    return papers