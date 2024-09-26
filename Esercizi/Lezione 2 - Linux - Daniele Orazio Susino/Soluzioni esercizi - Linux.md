# SOLUZIONI ESERCIZI CON TERMINALE LINUX

Tutti questi esercizi devono essere **svolti** **dopo** aver letto le **slide della seconda lezione**.
Ognuno di questi **esercizi** deve essere **svolto dal terminale** di Ubuntu o della vostra distro linux di scelta.

**ATTENZIONE**: Il comando **touch** è già **preinstallato** su **ubuntu**, se **non dovesse essere così** nella vostra distro, installatelo con **sudo apt install nano**.

## CREAZIONE DI UN FILE DI TESTO

- Muovetevi nella cartella /home/vostroNomeUtente

```shell
    cd ~
    # oppure
    cd /home/vostroNomeUtente # letteralmente il vostro nome utente, non dovete scrivere quindi vostroNomeUtente
```

- Create un file denominato prova.txt

```shell
    touch prova.txt
    # oppure
    nano prova.txt # nano in questo caso creerà anche il file oltre a fare da editor
```

- **Scrivete** dentro il file

```shell
    nano prova.txt # Modifica il file prova.txt DA NON FARE SE GIA' FATTO PRIMA
    # Dopo bisogna scrivere ciò che si vuole
    # salvare con ctrl + s
    # uscire con ctrl + x
```

- **Visaulizzate** il contenuto del file

```shell
    cat prova.txt # Manda in output il contenuto del file in terminale
```

## CREAZIONE DI UNA CARTELLA

- Muovetevi nella cartella /home/vostroNomeUtente

```shell
    cd ~
    # oppure
    cd /home/vostroNomeUtente # letteralmente il vostro nome utente, non dovete scrivere quindi vostroNomeUtente
```

- Create una cartella chiamata Test

```shell
    mkdir Test # Crea una cartella di nome Test
```

- Entrate nella cartella Test

```shell
    cd Test
```

- Create un file al suo interno, scriveteci qualcosa e visualizzatene il contenuto

```shell
    nano Prova.txt  # Crea il file, scrivete, salvate ed uscite
    cat Prova.txt   # Manda in output il contenuto del file
```

- **Eliminate** il file e poi la cartella **in questo esatto ordine**

```shell
    rm Prova.txt # Cancelliamo il file
    cd ..        # Torniamo indietro
    rm Test      # Cancelliamo la cartella
```

## CANCELLAZIONE DI UNA CARTELLA CONTENENTE DEI FILE

- Muovetevi nella cartella /home/vostroNomeUtente

```shell
    cd ~
    # oppure
    cd /home/vostroNomeUtente # letteralmente il vostro nome utente, non dovete scrivere quindi vostroNomeUtente
```

- Create una cartella chiamata Test

```shell
    mkdir Test # Crea una cartella di nome Test
```

- Entrate nella cartella Test

```shell
    cd Test
```

- Create un file al suo interno, scriveteci qualcosa e visualizzatene il contenuto

```shell
    nano Prova.txt  # Crea il file, scrivete, salvate ed uscite
    cat Prova.txt   # Manda in output il contenuto del file
```

- **Uscite** dalla cartella **senza eliminare il file**

```shell
    cd ..       # Usciamo dalla cartella senza eliminare il file
```

- Eliminate la cartella

```shell
    rm -dr Test # Usiamo il comando rm con le opzioni d (directory) ed r (recursive)
    # Quste due opzioni permettono di cancellare directory contenenti file
```

## INSTALLAZIONE DEL PACCHETTO SL

- Provare ad **installare il pacchetto SL**
- **Scoprire** il suo **funzionamento**

```shell
    sudo apt update     # Aggiorniamo la cache del gestore di pacchetti
    sudo apt install sl # Installiamo il pacchetto sl
    sl                  # Vediamo che il programma fa stampare un trenino a schermo
    man sl              # Leggiamo la sua documentazione
                        # Notiamo che ci sono delle opzioni -a, -l, -F
                        # proviamo a utilizzarle tutte
    sl -alFe            # Il treno vola e sembra che stia per succedere un incidente!
```

## GUERRE STELLARI

- Cercare e capire come **riprodurre Star Wars sul terminale**

```shell
    sudo apt update                 # Aggiorniamo la cache del gestore di pacchetti
    sudo apt install telnet         # Installiamo il protocollo telnet
    telnet towel.blinkenlights.nl   # Usiamo il protocollo telnet per collegarci al server dove guardare Star Wars
```

- Capire come **terminare un programma dal terminale**

```shell
   # Per terminare un programma dal terminale, bisogna premere la combinazione di tasti Ctrl + C
```
