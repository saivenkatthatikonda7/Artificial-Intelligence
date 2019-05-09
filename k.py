# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:24:50 2018

@author: saive
"""

import kivy

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()