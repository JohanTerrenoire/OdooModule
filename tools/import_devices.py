#!/usr/bin/python
# -*- coding: utf-8 -*-


import csv
import ConfigParser
import erppeek

#Chargement du fichier de configuration ERPPEEK
fichier_config = ConfigParser.ConfigParser()
fichier_config.read('/home/johan/erppeek.ini')
scheme = fichier_config.get('test','scheme')
port = fichier_config.get('test','port')
host = fichier_config.get('test','host')
username = fichier_config.get('test','username')
password = fichier_config.get('test','password')
database = fichier_config.get('test','database')

#Création de la connexion ERPPEEK
with erppeek.Client.from_config('test') as client:
    #-----Si la base de données n'éxiste pas sur le serveur-----
    if not database in client.db.list():
        print("The database doesn't exist !")
    #-----Si la base de données éxiste sur le serveur-----
    else:
        #-----Lire le fichier CSV-----
        with open('device.csv', 'rb') as csvfile:
            fichier_csv = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in fichier_csv:
                pMarque = client.search('iut.it.brand', [('name', '=', row[4])])

                pTypeModel = client.search('iut.it.model.type', [('name', '=', row[3])])

                pModele = client.search('iut.it.model', [('name', '=', row[5])])
                print ("Existe déjà")

                pPartenaire = client.search('res.partner', [('name', '=', row[6])])

                pNumeroSerie = client.search('iut.it.device', [('serial_number','=', row[0]), ('date_allocation','=', row[1]), ('date_purchase','=', row[2])])

                print('')

                #insertion des données dans la bdd si elles n'existent pas

                #ajout des valeurs de la marque
                if len(pMarque) == 0:
                     vBrand = client.create('iut.it.brand', {'name':row[4], 'warranty_delay_month':12})
                else:
                    vBrand = pMarque[0]
                    print('Erreur')

                #ajout des valeurs du type de modèle
                if len(pTypeModel) == 0:
                     vModelType = client.create('iut.it.model.type', {'name': row[5]})
                else:
                    vModelType = pTypeModel[0]
                    print('Erreur')

                #ajout des valeurs du modèle
                if len(pModele) == 0:
                     vModel = client.create('iut.it.model', {'name': row[3], 'brand_id': vBrand})
                else:
                    vModel = pModele[0]
                    print('Erreur')

                #ajout des valeurs de l'employé
                if len(pPartenaire) == 0:
                     vPartner = client.create('res.partner', {'name': row[6]})
                else:
                    vPartner = pPartenaire[0]
                    print('Erreur')

                #ajout des valeurs du dispositif
                if len(pNumeroSerie) == 0:
                     vDevice = client.create('iut.it.device', {'name': 'xxx',
                                                                'serial_number': row[0],
                                                                'date_allocation': row[1],
                                                                'date_purchase': row[2],
                                                                'partner_id': vPartner,
                                                                'model_id': vModel})
                else:
                    vDevice = pNumeroSerie[0]
                    print('Erreur')


# Insérer un enregistrement avec ERPPEEK :
# model('iut.it.device').create({'name': 'GalaxyS9', 'date_allocation': '1900-01-01 00:00:00',
# 'serial_number' : 'AAXX123400ZZ', 'date_purchase': '1900-01-01 00:00:00', 'date_warranty_end': '1900-01-01 00:00:00'})
