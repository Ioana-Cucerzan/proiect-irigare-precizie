
# Simulator pentru Sistemul de Irigatie de Precizie (Proiect Internship)

Salut! Aici am pus codul pentru proiectul meu de practica. Practic, am facut o macheta digitala (un simulator) pentru un sistem inteligent de irigat solul, ca sa nu mai stam sa legam fire si placi fizice in faza de testare. Aplicatia are o interfata web facuta in Python unde poti sa vezi cum un algoritm simplu ia decizii singur si porneste sau opreste apa in functie de ce zic senzorii.

## De ce am facut doar partea de cod si nu am legat firele?
M-am ocupat strict de partea de software, algoritm si interfata grafica. In proiectele reale, inainte sa cumperi componente hardware sau sa trimiti oameni in teren sa intinda cabluri de sute de metri, trebuie sa validezi logica programului intr-un mediu de simulare. 

De aceea am facut acest simulator in Python: el imita perfect comportamentul senzorilor si al releului, demonstrand ca algoritmul functioneaza corect. Pasul urmator ar fi ca datele simulate de mine sa fie inlocuite cu datele reale citite de placa ESP32 prin protocol serial, codul ramanand in mare parte acelasi.

## De unde a pornit ideea?
Nu am inventat eu datele astea, ci m-am luat direct dupa un document de cercetare pe care l-am citit in internship: 'Studiul 1. CONTRIBUTII PRIVIND REALIZAREA UNUI SISTEM AUTOMAT DE IRIGATIE SI MONITORIZAREA ACESTUIA DE LA DISTANTA'. Ideea de baza din studiu e ca in agricultura moderna nu mai uzi pamantul la ochi, ci masori exact cand si cat are nevoie planta, ca sa economisesti apa si sa nu speli nutrientii din sol.

## Ce piese din teren simuleaza codul asta?
In spate, aplicatia gandeste exact ca un sistem IoT (Internet of Things - adica obiecte si senzori conectati la internet care schimba date intre ele) real din camp:
1. Placa ESP32-WROOM-32: Asta e creierul care sta in camp si trimite datele prin Wi-Fi.
2. Senzorul de sol: Cel care masoara umiditatea, temperatura, pH-ul, conductivitatea si nutrientii (Azot, Fosfor, Potasiu - adica NPK).
3. Modulul MAX485 (RS-485): Cablul industrial folosit pentru ca in camp sunt distante mari (sute de metri) si firele normale ar prinde paraziti sau ar pierde semnalul.
4. Releul si Pompa: Placa ESP32 scoate un curent foarte mic (3.3V-5V) si n-ar putea porni niciodata o pompa mare de retea. Releul e practic un intrerupator sigur: primeste semnalul mic de la placa si da drumul la curentul mare pentru pompa.

## Cum am construit proiectul si cum se ruleaza?
Mai intai am facut un folder pe Desktop si am izolat toutul intr-un mediu virtual Python (venv) ca sa nu amestec bibliotecile cu ce mai am prin PC. Am folosit si Git pe un branch separat numit 'feature/interfata-prezentare' ca sa lucrez curat, fara sa stric codul principal.

Pentru interfata grafica am ales Streamlit pentru ca e super rapid si iti face o pagina web direct din cod Python, fara sa ma chinui cu HTML, CSS sau prostii de genul asta.

Cum functioneaza cand ii dai drumul:
- Din stanga (glisoarele din pagina) alegi tu pragurile (ex: sa ude daca scade sub 35% umiditate si sa se opreasca la 70%).
- Cand apesi pe buton, codul genereaza niste numere random dar realiste pentru senzori (ca si cum ar veni date proaspete de pe ESP32).
- Algoritmul (niste functii if-else simple) compara datele. Daca e prea uscat, ecranul se face verde si zice ca a pornit pompa. Daca e destul de ud, se face rosu si zice ca pompa s-a oprit ca sa nu faca risipa de apa.

## Cum se porneste in PowerShell:
1. Intri in folderul de pe Desktop: cd ~\Desktop\proiect-irigare-precizie
2. Activezi venv-ul: .\\venv\\Scripts\\Activate.ps1
3. Rulezi aplicatia: streamlit run app.py

