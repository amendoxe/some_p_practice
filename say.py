"""We are going to do some library testing"""
import cowsay
import sys

if len(sys.argv) > 1:
    message = ""
    for arg in sys.argv[1:]:
        message += arg
        message += " "
    cowsay.stegosaurus(message)
    cowsay.octopus(message)
    cowsay.pig(message)
    cowsay.tux(message)
