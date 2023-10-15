#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    r1 = Rectangle(1, 1, 2, 8, 1)
    r2 = Rectangle(2, 1, 5, 6, 2)
    r1.update(width=0)
    r2.update(height=1)
    print(str(r1), str(r2), sep='\n')
