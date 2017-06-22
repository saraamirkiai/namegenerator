from random import *

word_list = ["Holiday", "Venus", "Morticia", "Demise", "Juno", "Rosa", "Lydia", "Desi", "Daria", "March", "Mondate"]

middle_name = ["Alex","Riot","Luther","Craig","Theo"]

x = randint(0, len(word_list)-1)

y = randint(0, len(middle_name)-1)

print(word_list[x]+" " +middle_name[y])
