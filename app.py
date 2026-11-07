
# Importam biblioteca random pentru a genera date false (valori aleatorii) de la senzori
import random
# Importam biblioteca time pentru a putea introduce mici pauze sau intarzieri daca este nevoie
import time
# Importam biblioteca principala Streamlit pentru a construi interfata grafica web a proiectului
import streamlit as st

# Configuram pagina aplicatiei: setam titlul din tab-ul de browser si latimea pe tot ecranul
st.set_page_config(page_title="Sistem Irigatie Precizie IoT", layout="wide")

# Afisam titlul principal al aplicatiei pe pagina web cu ajutorul unui emoji si text formatat
st.title("🌱 Proiect Internship: Sistem Automat de Irigatie de Precizie")
# Adaugam un subtitlu care explica componentele hardware simulate (ESP32 si senzorul NPK pe RS-485)
st.subheader("Simulare IoT bazata pe arhitectura ESP32-WROOM-32 si Senzor NPK prin RS-485")

# Verificam daca variabila care tine starea pompei exista deja in memoria aplicatiei (session_state)
if "stare_pompa" not in st.session_state:
    # Daca nu exista, o initializam ca fiind "OPRIT", adica pompa nu functioneaza la pornirea aplicatiei
    st.session_state.stare_pompa = "OPRIT"

# Cream o sectiune de configurare in bara principala din stanga (sidebar) pentru setari tehnice
st.sidebar.header("⚙️ Configurare Parametri Sistem")
# Cream un selector glisant (slider) pentru pragul minim de umiditate de la care porneste irigarea
prag_min = st.sidebar.slider("Prag minim umiditate (Pornire)", 20.0, 50.0, 35.0)
# Cream un selector glisant (slider) pentru pragul maxim de umiditate la care se opreste irigarea
prag_max = st.sidebar.slider("Prag maxim umiditate (Oprire)", 60.0, 90.0, 70.0)

# Cream un buton mare pe ecran care va declansa citirea datelor simulate prin click
if st.button("🔄 Simuleaza Citire Senzori Live (MAX485/ESP32)"):
    # Generam o valoare aleatorie pentru umiditatea solului intre 25% si 80%, cu 2 zecimale
    umiditate = round(random.uniform(25.0, 80.0), 2)
    # Generam o valoare aleatorie pentru temperatura solului intre 18 si 38 grade Celsius, cu o zecimala
    temperatura = round(random.uniform(18.0, 38.0), 1)
    # Generam o valoare aleatorie pentru pH-ul solului (aciditate/alcalinitate) intre 6.0 si 7.2
    ph = round(random.uniform(6.0, 7.2), 2)
    # Generam o valoare pentru conductivitatea electrica (salinitate) intre 300 si 1100 uS/cm
    conductivitate = round(random.uniform(300, 1100), 0)
    # Generam o valoare pentru nivelul de Azot (N) din sol ca numar intreg intre 25 si 75 mg/kg
    n = round(random.uniform(25, 75), 0)
    # Generam o valoare pentru nivelul de Fosfor (P) din sol ca numar intreg intre 15 si 45 mg/kg
    p = round(random.uniform(15, 45), 0)
    # Generam o valoare pentru nivelul de Potasiu (K) din sol ca numar intreg intre 50 si 110 mg/kg
    k = round(random.uniform(50, 110), 0)

    # Initializam o variabila de text vida in care vom stoca mesajul de explicatie pentru algoritm
    status_mesaj = ""
    
    # Incepe logica algoritmului de decizie: daca umiditatea masurata e mai mica decat pragul minim setat
    if umiditate < prag_min:
        # Schimbam starea pompei in mod activ, simuland declansarea releului fizic
        st.session_state.stare_pompa = "PORNIT (Activ)"
        # Salvam mesajul care explica de ce s-a pornit pompa (releul a primit semnalul de control de 5V)
        status_mesaj = f"🚨 Umiditatea ({umiditate}%) e sub pragul critic de {prag_min}%. Releul a primit semnal de 5V. Pompa a pornit!"
    # Daca umiditatea masurata este mai mare decat pragul maxim setat de utilizator
    elif umiditate > prag_max:
        # Schimbam starea pompei in oprit, deoarece solul are destula apa
        st.session_state.stare_pompa = "OPRIT (Saturat)"
        # Salvam mesajul care confirma oprirea alimentarii releului si implicit a pompei
        status_mesaj = f"✅ Solul a atins nivelul optim de umiditate ({umiditate}%). Releul a oprit alimentarea pompei."
    # Daca umiditatea este intre cele doua praguri, sistemul isi mentine starea fara sa schimbe nimic
    else:
        # Salvam un mesaj informativ care spune ca solul este in parametrii normali de siguranta
        status_mesaj = f"ℹ️ Umiditatea este in zona de siguranta ({umiditate}%). Nu sunt necesare modificari."

    # Impartim ecranul in 4 coloane egale pentru a afisa parametrii principali de mediu sub forma de casete
    col1, col2, col3, col4 = st.columns(4)
    # In prima coloana afisam caseta cu valoarea procentuala pentru umiditatea solului
    col1.metric(label="💧 Umiditate Sol", value=f"{umiditate} %")
    # In a doua coloana afisam caseta cu valoarea temperaturii exprimate in grade Celsius
    col2.metric(label="🌡️ Temperatura Sol", value=f"{temperatura} °C")
    # In a treia coloana afisam caseta cu valoarea pH-ului din sol
    col3.metric(label="🧪 pH Sol", value=ph)
    # In a patra coloana afisam caseta cu valoarea conductivitatii electrice masurate
    col4.metric(label="⚡ Conductivitate", value=f"{conductivitate} uS/cm")

    # Adaugam un subtitlu pe pagina pentru sectiunea rezervata macronutrientilor esentiali ai plantelor
    st.markdown("### 📊 Stare Nutrienti Sol (Macroelemente NPK)")
    # Impartim ecranul in 3 coloane noi pentru a afisa cele trei elemente chimice din sol (N, P, K)
    col_n, col_p, col_k = st.columns(3)
    # In prima coloana de nutrienti afisam valoarea pentru Azot (N) in miligrame pe kilogram
    col_n.metric(label="🟤 Azot (N)", value=f"{n} mg/kg")
    # In a doua coloana de nutrienti afisam valoarea pentru Fosfor (P) in miligrame pe kilogram
    col_p.metric(label="⚪ Fosfor (P)", value=f"{p} mg/kg")
    # In a treia coloana de nutrienti afisam valoarea pentru Potasiu (K) in miligrame pe kilogram
    col_k.metric(label="🟠 Potasiu (K)", value=f"{k} mg/kg")

    # Trasam o linie orizontala de demarcatie vizuala pentru a separa datele de starea hardware-ului
    st.markdown("---")
    # Adaugam un titlu pentru sectiunea care monitorizeaza comportamentul releului electric de control
    st.subheader("📢 Monitorizare Releu Hardware")
    # Verificam daca starea actuala salvata a pompei contine cuvantul "PORNIT"
    if "PORNIT" in st.session_state.stare_pompa:
        # Daca pompa este pornita, afisam o caseta verde (de succes) cu starea curenta a pompei
        st.success(f"Stare Pompa: **{st.session_state.stare_pompa}**")
        # Sub caseta verde afisam mesajul explicativ salvat anterior in variabila status_mesaj
        st.info(status_mesaj)
    # In caz contrar (daca starea pompei este "OPRIT")
    else:
        # Afisam o caseta rosie (de avertizare/oprire) care indica faptul ca pompa nu functioneaza
        st.error(f"Stare Pompa: **{st.session_state.stare_pompa}**")
        # Sub caseta rosie afisam textul informativ stocat in variabila status_mesaj
        st.info(status_mesaj)
# Daca utilizatorul nu a apasat inca butonul de simulare (la prima incarcare a paginii)
else:
    # Afisam o caseta informativa albastra care indruma utilizatorul sa apese pe buton pentru a porni sistemul
    st.info("Faceti click pe butonul de mai sus pentru a simula receptia datelor de la placa ESP32.")
