import random
import time
mylist = ["Roche", "Papier", "Ciseaux"]
y = (random.choice(mylist))
x = input("Roche, Papier ou Ciseaux? ")
if x == "Roche" and y == "Papier":
    print("J'ai " + y)
    time.sleep(0.5)
    print("J'ai Ganger")
if x == "Roche" and y == "Roche":
    print("J'ai " + y)
    time.sleep(0.5)
    print("Égalité")
if x == "Roche" and y == "Ciseaux":
    print("J'ai " + y)
    time.sleep(0.5)
    print("J'ai Perdu")
if x == "Papier" and y == "Papier":
    print("J'ai " + y)
    time.sleep(0.5)
    print("Égalité")
if x == "Papier" and y == "Roche":
    print("J'ai " + y)
    time.sleep(0.5)
    print("J'ai Gagné")
if x == "Papier" and y == "Ciseaux":
    print("J'ai " + y)
    time.sleep(0.5)
    print("J'ai Perdu")
if x == "Ciseaux" and y == "Papier":
    print("J'ai " + y)
    time.sleep(0.5)
    print("J'ai Gagné")
if x == "Ciseaux" and y == "Roche":
    print("J'ai " + y)
    time.sleep(0.5)
    print("J'ai Perdu")
if x == "Ciseaux" and y == "Ciseaux":
    print("J'ai " + y)
    time.sleep(0.5)
    print("Égalité")
