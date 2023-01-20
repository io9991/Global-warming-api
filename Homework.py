'''
DOCUMENTAZIONE PRESA DA : https://global-warming.org/

progetto Traccia 1 : monitoraggio dati riscaldamento globale in particolare CO2, N2O e CH4

'''


#importo librerie
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#import plotly.express as px

#api delle varie sezioni

#cambiamento_temperatura = requests.get('https://global-warming.org/api/temperature-api').text
livelli_co2 = requests.get('https://global-warming.org/api/co2-api').text
emissioni_metano = requests.get('https://global-warming.org/api/methane-api').text
ossido_diazoto_aria = requests.get('https://global-warming.org/api/nitrous-oxide-api').text
#temperatura_oceani = requests.get('https://global-warming.org/api/temperature-api').text


#prendo in input le richieste
#interfaccia del terminale
def main():
#dati = ''
    print('')
    print('DATI RELATIVI AL RISCALDAMENTO GLOBALE:')
    print('')
    spazio = input('Premi invio per visualizzare le varie opzioni')
    print('')
    print("1-Livello CO2 nell'aria")
    print("2-Ossido di diazoto")
    print("3-Emissioni di metano")
    #print("4-Temperatura oceani")
    #print("5-Temperatura globale")
    print('')

    numero_richiesta = int(input('Digita il numero dei dati che vuoi visualizzare '))


#creo le funzioni

#CO2
    def co2():
        giorni = []
        mesi = []

        for i in range(0,31):
            giorni.append(i)
        for j in range(0,12):
            mesi.append(j)
    

        dati_json = json.loads(livelli_co2)
        
        print('1-andamento per anno,mese,giorno')
        print('2-grafico andamento annuale')
        
        opz = int(input('cosa vuoi visualizzare?:'))
        
        if opz == 1:
            print("AVVERTENZA: i dati annuali partono dall'anno 2013, mese 1 e giorno 20, scrivere il mese in cifre.")
            anno = int(input('inserisci anno: '))
            mese = int(input('inserisci mese: '))
            giorno = int(input('inserisci giorno: '))
            
            if mese not in mesi or giorno not in giorni:
                print('AVVISO: Non hai inserito il giusto input, riprova')
                print("")
                co2()
            
            else:
                for chiave in dati_json:
                    lista = dati_json["co2"]
                    for i in range(len(lista)):
                        diz = lista[i]
                        for k in diz:
                            if diz["year"] == str(anno) and diz["month"] == str(mese) and diz["day"] == str(giorno):
                                
                                print("")
                                
                                print("Moli a secco di CO2 nell'aria espressa in parti per milioni: ",diz["trend"])

                                print("")
                                
                                print("Se vuoi visualizzare ulteriori dati relativi alla CO2, digita 1")
                                print("Se vuoi tornare alla pagina iniziale, digita 2")
                                print("")
                                
                                ritorna = int(input("Digita: "))
                                
                                if ritorna == 1:
                                    co2()
                                
                                elif ritorna == 2:
                                    main()
                            
                            break   
                        
                        
        elif opz == 2:
            grafico_co2(dati_json)
        
        
        else:
            print("")
            print("AVVISO: input errato")
            print("INSERISCI NUOVAMENTE I DATI")
            print("")
            co2()




    def grafico_co2(dati_json):
        anno = []
        quantita = []

        for chiave in dati_json:
                lista = dati_json["co2"]
                for i in range(len(lista)):
                    diz = lista[i]
                    for k in diz:
                        anno.append(diz["year"])
                        quantita.append(float(diz["trend"]))


        #grafico
        #ax = plt.axes()
        plt.style.use("seaborn-v0_8-darkgrid")
        plt.title("Andamento della quantità di CO2 nell'aria")

        asse_x = anno
        asse_y = quantita
        x = np.arange(float(asse_x[0]), float(asse_x[len(asse_x) - 1]), (float(asse_x[len(asse_x) - 1]) - float(asse_x[0]))/len(asse_x))

        plt.plot(x, asse_y, color = 'red')

        plt.xlabel('Anni')
        plt.ylabel('CO2(ppm)')



        plt.show()

        print("")
        print("Se vuoi visualizzare ulteriori dati relativi alla CO2, digita 1")
        print("Se vuoi tornare alla pagina iniziale, digita 2")
        print("")
        
        ritorna = int(input("Digita: "))
        
        if ritorna == 1:
            co2()
        
        elif ritorna == 2:
            main()

        else:
            print("")
            print("input errato")
            main()





    #Monossido di diazoto
    def ossido_diazoto():
        dati_json = json.loads(ossido_diazoto_aria)
        print('1-andamento per anno')
        print('2-grafico')
        opz = int(input("cosa vuoi visualizzare?: "))    
        #!N.B parte dal 2001 fino al settembre 2022
        #!in questi dati l'anno e il mese sono insieme
        if opz == 1:
            print("AVVERTENZA: l'anno è espresso come anno.mese; ESEMPIO: 2018.11")
            anno_mese = float(input("Inserisci l'anno e il mese: "))
            for chiave in dati_json:
                lista = dati_json["nitrous"]
                for i in range(len(lista)):
                    diz = lista[i]
                    for k in diz:
                        if diz["date"] == str(anno_mese):

                            print("")

                            print("Moli a secco di N2O nell'aria espressa in parti per milioni: ",diz["trend"])

                            print("")
                                
                            print("Se vuoi visualizzare ulteriori dati relativi alla N2O, digita 1")
                            print("Se vuoi tornare alla pagina iniziale, digita 2")
                            print("")
                            
                            ritorna = int(input("Digita: "))
                            
                            if ritorna == 1:
                                ossido_diazoto()
                            
                            elif ritorna == 2:
                                main()

                        break


        elif opz == 2:
            grafico_n2o(dati_json)


        else:
            print("AVVISO: input errato")
            print("INSERISCI NUOVAMENTE I DATI")
            print("")
            ossido_diazoto()







    def grafico_n2o(dati_json):
        # declare the two axis
        asse_x = [] 
        asse_y = []
        dati = dati_json["nitrous"] 

        for i in range(1, len(dati)):
            asse_x.append((float(dati[i]["date"]))) 
            asse_y.append((float(dati[i]["trend"]))) 


        plt.style.use("seaborn-v0_8-darkgrid")

        plt.title("Andamento della quantità di N2O nell'aria")
        plt.plot(sorted(asse_x), asse_y, color = "red")

        plt.xlabel('Anni')
        plt.ylabel('N2O(ppm)')

        plt.show()

        print("")
        print("Se vuoi visualizzare ulteriori dati relativi alla N20, digita 1")
        print("Se vuoi tornare alla pagina iniziale, digita 2")
        print("")
        
        ritorna = int(input("Digita: "))
        
        if ritorna == 1:
            ossido_diazoto()
        
        elif ritorna == 2:
            main()
        
        else:
            print("")
            print("input errato")
            main()






    def metano():
        dati_json = json.loads(emissioni_metano)
        print('1-andamento per anno')
        print('2-grafico CH4')
        opz = int(input("cosa vuoi visualizzare?: ")) 

        if opz == 1:
            print("AVVERTENZA: l'anno è espresso come anno.mese; ESEMPIO: 2019.8")
            anno_mese = float(input("inserisci l'anno e il mese: "))
            for chiave in dati_json:
                lista = dati_json["methane"]
                for i in range(len(lista)):
                    diz = lista[i]
                    for k in diz:
                        if diz["date"] == str(anno_mese):

                            print("")

                            print("quantità di metano nell'aria: ",diz["trend"])

                            print("")
                                
                            print("Se vuoi visualizzare ulteriori dati relativi al metano, digita 1")
                            print("Se vuoi tornare alla pagina iniziale, digita 2")
                            print("")
                            
                            ritorna = int(input("Digita: "))
                            
                            if ritorna == 1:
                                metano()
                            
                            elif ritorna == 2:
                                main()

                        break

                    
        elif opz == 2:
            grafico_ch4(dati_json)

        else:
            print("")
            print("AVVISO: input errato")
            print("INSERISCI NUOVAMENTE I DATI")
            print("")
            metano()



    def grafico_ch4(dati_json):
        asse_x = [] 
        asse_y = []
        dati = dati_json["methane"] 

        for i in range(1, len(dati)):
            asse_x.append((float(dati[i]["date"]))) 
            asse_y.append((float(dati[i]["trend"]))) 


        plt.style.use("seaborn-v0_8-darkgrid")

        plt.title("Andamento della quantità di CH4 nell'aria")
        plt.plot(sorted(asse_x), asse_y, color = "green")


        plt.xlabel('Anni')
        plt.ylabel('CH4(ppm)')

        plt.show()

        print("")
        print("Se vuoi visualizzare ulteriori dati relativi al metano, digita 1")
        print("Se vuoi tornare alla pagina iniziale, digita 2")
        print("")
        
        ritorna = int(input("Digita: "))
        
        if ritorna == 1:
            metano()
        
        elif ritorna == 2:
            main()

        else:
            print("")
            print("input errato")
            main()





    #def grafico_tutto():
        #!fare grafico che unisce tutti e tre i gas nell'aria
        #!sia cartesiano
        #!sia istogramma




    if numero_richiesta == 1:
        co2()

    elif numero_richiesta == 2:
        ossido_diazoto()
    
    elif numero_richiesta == 3:
        metano()
    
    else:
        print("")
        print("AVVISO: input errato")
        print("INSERISCI NUOVAMENTE I DATI")
        print("")
        print("")
        main()

main()
