from concurrent.futures import ThreadPoolExecutor

from requests import get
from bs4 import BeautifulSoup as bs
from rich.console import Console
from random import choice

c = Console()

class Rev:

    def __init__(self) -> None:
        self.url = "https://domains.tntcode.com/ip/{}/"
        self.domains = []
        self.domen = []
        self.result = "result.txt"

    def reverse(self, ip: str) -> int:
        try:
            res = 0
            parse = bs(get(self.url.format(ip)).text, "html.parser")
            if parse.textarea:
                for x in parse.textarea.text.strip().splitlines():
                    self.domains.append(x)
                    self.domen.append(x)
                    open(self.result, "a+").write(x+"\n")
                res = self.domen.__len__()
            self.domen = []
            return res
        except Exception as e:
            print(e)
            return 0

    def animation(self, task: list, title: str, type: str="rev") -> None:
        with c.status("[cyan]%s" % title) as tod:
            with ThreadPoolExecutor(max_workers=self.thread) as thread:
                for tosk in task:
                    if type == "rev":
                        anu = thread.submit(self.reverse, tosk).result()
                        spin = choice(["aesthetic","bouncingBall","bouncingBar","arc"])
                        if anu == 0:
                            tod.update("[cyan]%s[white] Reversed - [red]%s [white]domain(s)" % (tosk, anu), spinner=spin)
                        else:
                            tod.update("[cyan]%s[white] Reversed - [green]%s [white]domains(s)" % (tosk, anu), spinner=spin)
                    elif type == "write":
                        open(self.result, "a+").write(tosk+"\n")

    @property
    def main(self):
        ip = open(input("IP list : "), "r").read().splitlines()
        self.result = input("Saved : ")
        self.thread = int(input("Thread : "))
        self.animation(list(dict.fromkeys(ip)), "Reverse IP", "rev")
        #self.animation(self.domains, "Writing domains on file [cyan]%s" % self.result, "write")
        c.print("[green]Successfully [white]File saved in [green]%s" % self.result)

if __name__ == "__main__":
    Rev().main
