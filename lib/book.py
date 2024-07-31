#!/usr/bin/env python3

class Book:
    
    def __init__(self, title="And Then There Were None", page_count=272):
        self.page_count =page_count
        self.title = title
      
    @property
    def page_count(self):
        print("in getter")
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
        
    def turn_page(self):
            print("Flipping the page...wow, you read fast!")
        
   # page_count = property(get_page_count, set_page_count)
    
    
    