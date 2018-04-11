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
            device_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in device_reader :
                #-----Écrire chaque ligne dans la base de données-----
                client.model('iut.it.device').create({'name': row[3], 'date_allocation': row[1], 'serial_number': row[0], 'date_purchase': row[2]})


# Insérer un enregistrement avec ERPPEEK :
# model('iut.it.device').create({'name': 'GalaxyS9', 'date_allocation': '1900-01-01 00:00:00',
# 'serial_number' : 'AAXX123400ZZ', 'date_purchase': '1900-01-01 00:00:00', 'date_warranty_end': '1900-01-01 00:00:00'})
