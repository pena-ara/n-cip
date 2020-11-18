#!/usr/bin/env python

import os
import json
import requests

api_token = "" # api key dari ipgeolocation
ipgeo = f"https://api.ipgeolocation.io/ipgeo/?apiKey={api_token}" # url api untuk cek ip
ipuser = f"https://api.ipgeolocation.io/user-agent/?apiKey={api_token}" # url api untuk cek user agent

# dapatkan hasil json dari api untuk cek ip
res_ipgeo = requests.get(ipgeo)
json_ipgeo = res_ipgeo.json()
ipgeo_timezone = json_ipgeo['time_zone']
ipgeo_currency = json_ipgeo['currency']

# dapatkan hasil json dari api untuk cek user agent
res_ipuser = requests.get(ipuser)
json_ipuser = res_ipuser.json()
ipuser_device = json_ipuser['device']
ipuser_engine = json_ipuser['engine']
ipuser_os = json_ipuser['operatingSystem']


print("=========== IP ANDA ===========")
print("IP      = ", json_ipgeo['ip'])
print("Kota    = ", json_ipgeo['city'])
print("Prov    = ", json_ipgeo['state_prov'])
print("Negara  = ", json_ipgeo['country_name'])
print("ISP     = ", json_ipgeo['isp'])
print("Device  = ", ipuser_device['name'])
print("Type    = ", ipuser_device['type'])
print("OS      = ", ipuser_os['name'])
print(f"Lokasi  = https://www.openstreetmap.org/#map=15/{json_ipgeo['latitude']}/{json_ipgeo['longitude']}" )
print("===============================")
def menu():
    while True:
        print('''\033[1;94m
███╗   ██╗       ██████╗██╗██████╗ 
████╗  ██║      ██╔════╝██║██╔══██╗
██╔██╗ ██║█████╗██║     ██║██████╔╝
██║╚██╗██║╚════╝██║     ██║██╔═══╝ 
██║ ╚████║      ╚██████╗██║██║     
╚═╝  ╚═══╝       ╚═════╝╚═╝╚═╝ By Nestero
N-CIP adalah tool sederhana untuk mengecek ip dengan bantuan api dari ipgeolocation.io
        ''')
        print("======= MENU =======")
        print(" [1] Cek IPv4")
        print(" [0] Keluar")
        m = input("Pilih Opsi : ")
       
        while m == "1":
            ip = input("masukan IP : ")
            ipgeo_ip = f"{ipgeo}&ip={ip}"
            res_ip = requests.get(ipgeo_ip)
            json_ip = res_ip.json()
            ip_timezone = json_ip['time_zone']
            ip_currency = json_ip['currency']
            res_ipuser = requests.get(ipuser)
            json_ipuser = res_ipuser.json()
            ipuser_device = json_ipuser['device']
            ipuser_engine = json_ipuser['engine']
            ipuser_os = json_ipuser['operatingSystem']
            
            print("Detail untuk IP", ip)
            print("IP     = ", json_ip['ip'])
            print("Kota   = ", json_ip['city'])
            print("Prov   = ", json_ip['state_prov'])
            print("Negara = ", json_ip['country_name'])
            print("ISP    = ", json_ip['isp'])
            print("Device = ", ipuser_device['name'])
            print("Type   = ", ipuser_device['type'])
            print("OS     = ", ipuser_os['name'])
            print(f"Lokasi = https://www.openstreetmap.org/#map=15/{json_ipgeo['latitude']}/{json_ipgeo['longitude']}" )
            print("\n[0] untuk kembali")
            cip = input("> ")
            if cip == "0":
                os.system("clear")
                menu()
            else:
                os.system("clear")
                print("Tak ada dalam menu !!!")
                menu()
        if m == "0":
            print("Bye..............")
            exit()
        else:
            os.system("clear")
            print("Tak ada dalam menu !!!")
            menu()

menu()

