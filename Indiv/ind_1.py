#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = list(input('Напечатайте предложение: ').split())
    c = input('Какой символ проверить на вхождение: ')
    for i in range(len(s)):
        if c in s[i]:
            print(s[i])