#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"c", "e", "h", "n"}
    b = {"e", "f", "k", "n", "x"}
    c = {"b", "c", "h", "p", "r", "s"}
    d = {"b", "e", "g"}
    x = (a.difference(b)).intersection(c.union(d))
    print(f"x = {x}")
    bn = u.difference(b)
    y = (a.intersection(bn)).union(c.difference(d))
    print(f"y = {y}")
    