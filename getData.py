from pathlib import Path
from bs4 import BeautifulSoup
import json
import re

class Paper:

    def __init__(self, path:str) -> None:
        
        self.path = path
        self.json = json.load(open(path, encoding='utf-8'))
        self.title = self.json['articleTitle']
        self.number = self.json['articleNumber']
        self.authors = self.json['authors']
        self.abstract = self.json['abstract']
        self.text = self._get_text()

    def __str__(self) -> str:
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'

    def _get_text(self) -> str:
        text = self.abstract + "\n" + "\n".join([p.text for p in BeautifulSoup(self.json['xml'], 'lxml').find_all('p')])
        return self._clean_text(text)

    def _clean_text(self, text:str) ->str:
        """
        arg(s) : The input text is the xml component of the json object with the key `xml`
        return(s) : Return the cleaned text without the xml tags
        """
        regex = r"CCBY - IEEE.*|\[\d+\]|\$.*\$|View Source.*|\\begin.*|FIGURE \d+|Fig. \d+|[^A-Za-z0-9^ ]|SECTION [A-Z]+|\t\t|\n|Eq \d+|  "
        regex_empty = r" +"
        regex_eqns = r"Eq \d+|Lemma \d+|section \d+|section \d+ \d+|From \d+|Eqs[^a-z^A-Z]+"
        result = re.sub(regex, " ", text, 0, re.MULTILINE)
        result = re.sub(regex_empty, " ", result, 0, re.MULTILINE)
        result = re.sub(regex_eqns, "", result, 0, re.MULTILINE).strip()
        return result

def getData(path_to_data:str)-> list[list]:
    papers = [Paper(path) for path in Path(path_to_data).rglob('*.json')]
    return papers

