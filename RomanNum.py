# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 10:42:51 2022

@author: tahni
"""

def conv(inputNumber):
    num = [1, 4, 5, 9, 10]
    symbols = ["I", "IV", "V", "IX", "X"]
    i = 4
    convertedNumeral = ""
    
    
    while inputNumber:
        div = inputNumber // num[i]
        inputNumber %= num[i]
  
        while div:
            convertedNumeral += symbols[i]
            # print(sym[i], end = "")
            div -= 1
        i -= 1
    return convertedNumeral

    
