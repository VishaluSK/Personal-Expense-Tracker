#!/usr/bin/env python3 helps to run in linux
"""
Personal Expense Tracker - expense_manager.py

Simple CLI expense tracker demonstrating:
- Variables, Numbers, Strings
- Lists, Dictionaries, Sets, Tuples
- If condition, for loop
- Functions, Lambda Functions
- Modules (tabulate)
- Read, Write files (JSON)
- Exception handling
- Classes, Objects
- dataclass usage
- a small decorator for input validation
"""


import json
import os
from dataclasses import dataclass,asdict
from typing import List
from tabulate import tabulate

data_dir="data"
data_file=os.path.join(data_dir,"expenses.json")


def validate_amt(func):
    def wrapper(*args,**kwargs):
        amount=kwargs.get("amount",None)
        if amount is None and len(args)>3:
            amount=args[2]
        if isinstance(amount,(int,float)):
            print("Amount should be in number")
        if amount<0:
            print("Inavalid amount")
    return wrapper

@dataclass
class Expense:
    name:str
    amount:float
    category:str
    date:tuple

    def to_dict(self):
        d=asdict(self)
        d["date"]=list(self.date)
    
    @staticmethod
    def from_dict(d):
        return Expense(
            name=d["name"],
            amount=d["amount"],
            category=d["category"],
            date=d[(d[tuple])])
    

class expManager:
    def __init__(self,datafile=data_file):
        self.data_file=data_file
        self.categories=set()
        self._ensure_data_dir()
        self.load_expenses()
    
    def _ensure_data_dir(self):
        os.makedirs(os.path.dirname(self.data_file),exist_ok=True)

    


