# -*- coding: utf-8 -*-

from dictcc import Dict
import pandas as pd
import wikipediaapi

"""
    Generate  German word list from Wiki with meaning as a CSV
    ----------------------------------------------------------
    * download wiki page with wikipedia-api as text    
    * read the text , generate the unique german words list
    * translate the words with dictcc API
    * generate csv with pandas
        ** delimiter:  ';' 

"""


class FullText:
    def __init__(self, title, text):
        self.url = title
        self.text = text

    def _list_unique_words(self):
        # create unique_list from text
        word_list = list()
        raw_word_list = list()

        text_updated = " ".join(self.text.split("\n"))
        raw_word_list = text_updated.split(" ")

        for word in raw_word_list:
            if len(word) > 1:
                word_list.append(word)

        unique_list = list(set(word_list))
        return unique_list

    @property
    def unique_words(self):
        return self._list_unique_words()


class TranslatedWords():
    def __init__(self, llist):
        self.words = llist

    def append(self, item):
        self.words += item

    def delete(self, item):
        # do stuff
        pass

    @property
    def converted2df(self):
        # do stuff
        if self.words:
            return pd.DataFrame(self.words)
        else:
            return pd.DataFrame()


class WikiScraper:
    @classmethod
    def download_page(cls, title="Wikipedia", lang='de'):
        # get all text from page
        wiki_object = wikipediaapi.Wikipedia(language=lang, extract_format=wikipediaapi.ExtractFormat.WIKI)
        page = wiki_object.page(title)

        if not page.exists():
            raise ValueError

        text = page.text
        return FullText(title, text)

    @classmethod
    def translate_list(cls, word_list):
        # translate
        translator = Dict()
        translation_list = list()

        word_count = len(word_list)
        print("number of words: ", str(word_count))

        for word in word_list:
            result = translator.translate(word, from_language='de', to_language='en')
            for tup in result.translation_tuples[:2]:
                translation_list.append(list(tup))

            word_count -= 1
            print("\r" + str(word_count), end="")

        return TranslatedWords(translation_list)

    @classmethod
    def scrape(cls, title):
        words = cls.download_page(title)
        u_words = words.unique_words
        t_words = cls.translate_list(u_words)
        return t_words

    @classmethod
    def generate_csv(cls, title, file_name):
        s_words = cls.scrape(title)
        df_words = s_words.converted2df
        df_words.to_csv(file_name, sep=';', encoding='utf-8', index=False, header=False)
