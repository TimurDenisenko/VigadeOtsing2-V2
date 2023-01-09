print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => ")))) #Lisatud paar sulgu, mis puudusid
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a
    paaris=0
    paaritu=0
    #eemaldas topelt võrdse ja jättis tavapärase võrdusseisu
    while b > 0: #kooloni asemel semikoolon
            if b % 2 == 0: #asendas võrrandi kontrolliga, kas osad on võrdsed
                    paaris += 1
            else:
                    paaritu += 1
                    #ümber korraldatud pluss
            b = b // 10 #b on lisaruumi
  
    print("Paarisarvud:",paaris)
    print("paarituid numbreid:",paaritu)
    #teksti järel ei olnud koma, nii et trükis oli muutuja
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Tagurda* sisestatud number")
    print()
    b=0
    while a > 0: #puudu semikoolon
        number = a % 10
        a = a // 10
        b = b * 10
        b +=number #b-l on lisaruum ja pluss on ümber paigutatud
    print("*Ümberpööratud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine") #lisasulgud
    print()
    if c % 2 == 0: #selle asemel, et kontrollida, kas mõlemad osad on võrdsed, oli võrrand
        print("c on paarisarv. Jagame 2-ga.")
    else:
        print("c on paaritu arv. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2 == 0: #selle asemel, et kontrollida, kas mõlemad osad on võrdsed, oli võrrand
                    c = c / 2 #eemaldati võrdsuse kontroll ja määrati võrdsus
            else:
                    c = (3*c + 1) / 2 #eemaldati võrdsuse kontroll ja määrati võrdsus
            print(round(c), end=" ") #teine ​​tsitaat jäeti välja
    print()
    print("Hüpotees on õige") #erinevad tsitaadid

