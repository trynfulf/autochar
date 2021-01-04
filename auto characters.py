import random
from random import choice


stat_block = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
skill_list = ["Athletics","Acrobatics","Sleight of Hand","Stealth","Arcana","History","Investigation",
          "Nature","Religion","Animal Handling","Insight","Medicine","Perception","Survival",
          "Deception","Intimidadtion","Performance","Persuasion"]

def file_to_list(filename):
    thefile = open(filename,"r")
    rows = [line for line in thefile]
    thefile.close()
    for i,r in enumerate(rows):
        rows[i] = r.replace("\n","")
    return rows

n = file_to_list("Name.txt")
r = file_to_list("Races.txt")
c = file_to_list("Classes.txt")
pr = file_to_list("Person.txt")
ide = file_to_list("Ideals.txt")
b = file_to_list("Bonds.txt")
f = file_to_list("Flaws.txt")
l = file_to_list("Languages.txt")
a = file_to_list("Alignment.txt")
ar = file_to_list("Armor.txt")
w = file_to_list("Weapons.txt")
rw = file_to_list("Rweapons.txt")
p = file_to_list("Packs.txt")

def stats():
    x =[0,0,0,0,0,0]
    while mean(x) != 14.5:
        x =[0,0,0,0,0,0]
        for i in range(6):
            a = random.randint(9,17)
            x[i] = a
    return x

def mean(x):
    y = sum(x)/6
    return y

def modifiers(stats):
    z = 0
    y = []
    for i in range(6):
        if stats[i]==9:
            z = -1
            y.append(z)
        elif stats[i]==10 or stats[i]==11:
            z = +0
            y.append(z)
        elif stats[i]==12 or stats[i]==13:
            z = +1
            y.append(z)
        elif stats[i]==14 or stats[i]==15:
            z = +2
            y.append(z)
        elif stats[i]==16 or stats[i]==17:
            z = +3
            y.append(z)
    return y

def hp(classes,modifiers):
    if classes=="Barbarian":
        hp = random.randint(1,12)
        hp = hp + modifiers[2]
    elif classes=="Bard" or classes=="Cleric" or classes=="Druid" or classes=="Monk" or classes=="Rogue" or classes=="Warlock":
        hp = random.randint(1,8)
        hp = hp + modifiers[2]
    elif classes=="Fighter" or classes=="Paladin" or classes=="Ranger":
        hp = random.randint(1,10)
        hp = hp + modifiers[2]             
    elif classes=="Sorcerer" or classes=="Wizard":
        hp = random.randint(1,6)
        hp = hp + modifiers[2] 

    return hp

def ac(arm,modifiers):
    if arm=="Padded" or arm=="Leather":
        armor = 11 + modifiers[1]
    elif arm=="Studded" or arm=="Hide":
        armor = 12 + modifiers[1]
    elif arm=="Chainshirt":
        armor = 13 + modifiers[1]
    elif arm=="Scale" or arm=="Breastplate":
        armor = 14 + modifiers[1]
    elif arm=="Ringmail":
        armor = 14
    elif arm=="Chainmail":
        armor = 16
    elif arm=="Splint":
        armor = 17
    elif arm=="Plate":
        armor = 18

    return armor

def skills(modifiers):
    print("Your skills are: ")
    print(skill_list[0],": ",modifiers[0])
    print(skill_list[1:4],": ",modifiers[1])
    print(skill_list[4:9],": ",modifiers[3])
    print(skill_list[9:14],": ",modifiers[4])
    print(skill_list[14:18],": ",modifiers[5])


def lines():
    for i in range(120):
        print("-",end="",sep="")
    print()

def presentation():
    s = stats()
    m = modifiers(s)
    name = choice(n)
    race = choice(r)
    classes = choice(c)
    person = choice(pr)
    idea = choice(ide)
    bond = choice(b)
    flaw = choice(f)
    st1 = choice(stat_block)
    st2 = choice(stat_block)
    lan = choice(l)
    lan2 = choice(l)
    al = choice(a)
    health = hp(classes,m)
    arm = choice(ar)
    armo = ac(arm,m)
    pack = choice(p)
    we = choice(w)
    rwe = choice(rw)
    print(name)
    print(race)
    print(classes)
    print("Health:",health,"/",health,sep="")
    print("ac:",armo,sep="")
    print("Speed:30ft")
    print("Intiative bonus: +2")
    print("Proficiency bonus: +2")
    lines()
    for i in range(6):
        print(stat_block[i],":",s[i]," ",end="",sep="")
    print()
    print(m)
    print()
    print("Your saving throws are:","    ",st1,"    ",st2)
    lines()
    skills(m)
    lines()
    print(choice(list(open("Background.txt"))),end="",sep="")
    print("Personality Traits:",person,sep="")
    print("Ideals:",idea,sep="")
    print("Bonds:",bond,sep="")
    print("Flaws:",flaw,sep="")
    print()
    print("Your languages are:","    ","Common","    ",lan,"    ",lan2)
    print("Your Alignment is:","     ",al)
    lines()
    print("| List of Equipment |")
    print("|",pack," " * (16-len(pack)),"|")
    print("|",arm," " * (16-len(arm)),"|")
    print("|",we," " * (16-len(we)),"|")
    print("|",rwe," " * (16-len(rwe)),"|")
    print("Money: 10gp")

presentation()
    






    



