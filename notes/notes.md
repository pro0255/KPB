# 460404602 - Kryptografie a počítačová bezpečnost

### Podmínky pro ukončení předmětu

Zápočet

- Část za úkoly - 3 dílčí
- Část za docházku

Zkouška

- Písemná zkouška

### Materiály

web: http://www.cs.vsb.cz/ochodkova/
reference: http://www.cs.vsb.cz/ochodkova/courses/kpb/mzka.pdf

### 7.2.2022

- Přednášky jsou "povinné", nebude se opakovat učivo na cvičení.
- Ze cvičení se omlouvat dopředu.
- Konzultace jsou možné se domluvit. (Třeba v neděli večer wtf? :D)

#### Notes

m nacpeme do šifrovacího algoritmu s klíčem a dostaneme šifrový text (mezivýsledek).
Pokud tenhle šifrový text dáme do dešifrovacího algoritmu pak dostaneme m´, kde platí že m´=m.

Dobrá představa je, že jsme schopni naším algoritmem napadnout data, server, kde všechno zašifrujeme. Můžeme potom vydírat!

Alice (odesílatel) a Bob (příjemce) jsou legitimní účastníci komunikace Riest (1978).

Symetrický vztah - oba používají to stejné.

Asymetrický - veřejný znají, soukromý ne. Takže nepoužívají to stejné.

Proudové zpracování - bit po bitu, nebo byte po bytu.. 

Blokové zpracování - zpracování omezené velikosti bitů/bytů.. nelze napsat algoritmus, který by uměl 
zašifrovat neomezenou délku vstupu

Útok hrubou silou - snažíme se zkrátka zajistit aby přepokladaný čas touto technikou byl vyšší než je "normální", a tak se nevyplatil praktikovat. Nutné zmínit, že to není kryptoanalytický útok.

Caesar - substituční 100-44 př.n.l ... 
    - klíč je 3..
    - šifrovací - posun o 3 znaky dopředu v abecedě 
    - dešifrovací - posun o 3 znaky zpět v abecedě 



## 


K(E): 41532 ... vem 4 znak z bloku a zapis na 1 pozici, udelej potom 

Symetrické klíče bývají většinou dlouhodobé..

Pokud se jedná o stejnou distribuci jako v přirozeném jazyce, pak se povětšinou jedná o transpoziční šifru. Jelikož ta nemá vlanost záměny distrubce monogramů (znaků).












