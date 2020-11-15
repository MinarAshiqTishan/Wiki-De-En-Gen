# -*- coding: utf-8 -*-

from wikideengen.wikideengen import WikiScraper as ws

if __name__ == "__main__":
    ws.generate_csv("Unternehmen", "Unternehmen.csv", ";", translations=1)


