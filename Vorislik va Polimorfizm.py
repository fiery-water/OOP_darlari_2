# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 23:00:09 2023

@author: Mavlonbek
"""

class Talaba:
    def __init__(self,ism,familya,tyil,pasport,fanlar_ruyxati=[]):
        self.ism=ism
        self.familya=familya
        self.tyil=tyil
        self.pasport=pasport
        self.fanlar_ruyxati=fanlar_ruyxati
    
    def get_name(self):
        """ Talabaning ismini qaytaruvchi funksiya """
        return self.ism
    
    def get_familya(self):
        """  Talabaning familyasini qaytaruvchi funksiya """
        return self.familya
    
    def get_age(self,hozirgi_yil):
        """ Talabaning yoshini qaytaruvchi funksiya """
        return self.hozirgi_yil-self.tyil
    
    def get_pasport(self):
        """ Talabaning pasport raqamini qaytaruvchi funcsiya """
        return self.pasport
    
    def __add__(self,fan):
        if isinstance(fan, Fan):
            self.fanga_yozil(fan)
    
    def fanga_yozil(self,*fan):
        for f in fan:
            if isinstance(f,Fan):
                self.fanlar_ruyxati.append(f)
            else:
                print("Fan obyektini kiriting")
                
    def get_fanlar_ruyxati(self):
        """ Talabaning fanlari ruyxatini qaytaruvchi funksiya """
        for fan in self.fanlar_ruyxati:
            return fan
    

class Fan:
    def __init__(self,*fan_nomi):
        self.fan_nomi=fan_nomi
        
        
talaba=Talaba("Mavlonbek","Toshtemirov",2004,"AD0845794")
fanlar=Fan("fizika","matematika","geografiya","ona-tili")