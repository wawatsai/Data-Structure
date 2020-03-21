#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:17:57 2020

@author: allen
"""

a = [123,234, 22, 777,876, 111,234,700,455,666,333,876,544,779, 4555, 1, 33, 556, 888, 2, 34, 69, 456]
for _ in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
print(a)
print(sorted(a))