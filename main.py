import checkers
from Type import Type

type_list = []
type_list.append(Type("Normal"))
type_list.append(Type("Fighting"))
type_list.append(Type("Flying"))
type_list.append(Type("Poison"))
type_list.append(Type("Ground"))
type_list.append(Type("Rock"))
type_list.append(Type("Bug"))
type_list.append(Type("Ghost"))
type_list.append(Type("Steel"))
type_list.append(Type("Fire"))
type_list.append(Type("Water"))
type_list.append(Type("Grass"))
type_list.append(Type("Electric"))
type_list.append(Type("Psychic"))
type_list.append(Type("Ice"))
type_list.append(Type("Dragon"))
type_list.append(Type("Dark"))
type_list.append(Type("Fairy"))

type_list[0].set_strong_off([])
type_list[1].set_strong_off(["Normal", "Rock", "Steel", "Ice", "Dark"])
type_list[2].set_strong_off(["Fighting", "Bug", "Grass"])
type_list[3].set_strong_off(["Grass", "Fairy"])
type_list[4].set_strong_off(["Poison", "Rock", "Steel", "Fire", "Electric"])
type_list[5].set_strong_off(["Flying", "Bug", "Rock", "Ice"])
type_list[6].set_strong_off(["Grass", "Psychic", "Dark"])
type_list[7].set_strong_off(["Ghost", "Psychic"])
type_list[8].set_strong_off(["Rock", "Ice", "Fairy"])
type_list[9].set_strong_off(["Bug", "Steel", "Grass", "Ice"])
type_list[10].set_strong_off(["Ground", "Rock", "Fire"])
type_list[11].set_strong_off(["Ground", "Rock", "Water"])
type_list[12].set_strong_off(["Flying", "Water"])
type_list[13].set_strong_off(["Fighting", "Poison"])
type_list[14].set_strong_off(["Flying", "Ground", "Grass", "Dragon"])
type_list[15].set_strong_off(["Dragon"])
type_list[16].set_strong_off(["Ghost", "Psychic"])
type_list[17].set_strong_off(["Fighting", "Dragon", "Dark"])

results_strong_off = checkers.strong_off_checker(type_list)

file = open("Results.txt", "a")

for combo in results_strong_off:
    string = ""
    for t in combo:
        string += t + " "
    string = string[:-1] + "\n"
    file.write(string)

file.close()