                ##KÜTÜPHANALER##
#######################################################
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import pyautogui
from pycaw.pycaw import AudioUtilities, IAudioSessionManager2, IAudioSessionControl2, IAudioMeterInformation
#######################################################
import cv2
import numpy as np
from PIL import ImageGrab
import subprocess
import pygetwindow as gw
import math
import keyboard
import requests
from requests import get
import os
import wmi
import contextlib
import hashlib
import socket
import pyuac
from ultralytics import YOLO
import torch
from pynput.mouse import Controller, Button
import cvzone
from multiprocessing import Process, Value, Array, Lock
from torchvision import transforms
from sort import *
import threading
global px, py, px2, py2, px3, py3
px, py, px2, py2, px3, py3 = 0, 0, 0, 0, 0, 0 
#######################################################
                    ##DEĞİŞKENLER##
#######################################################
serial_key = ""
THRESHOLD = 1.1
FRAME_COUNT = 5
farekanks = False
previous_frames = []
sattiama = False
threshold = 0.5
processed_screen = 0
mouse = Controller()
classNames = ["emoji-detect", "fare", "harita", "hasan", "kafa", "bosbisey", "bosbisey1", "bosbisey2"]
model = YOLO("deneme.pt")
device = torch.device("cpu")
model.to(device)
tracker = Sort()
antibot = False
oltayatakilmadi = "olta.png"
dolduenvanter = "doldu.png"
tasa = "tas.png"
plastik_sise = "plastik_sise.png"
cam_sise = "cam.png"
telsiz = "telsiz.png"
metal_konserve = "metal.png"
plastik_torba = "torba.png"
yipranmis_kiyafet = "yipranmis.png"
yipranmis_ayakkabi = "yipranmisa.png"
balikyem= "balikyemi.png"
balikyem1="balikyemi1.png"
yosun = "yosun.png"
yosun1 = "yosun1.png"
tas1 = "tas1.png"
psise1 = "psise1.png"
csise1 = "csise1.png"
metal1 = "metal1.png"
torba1 = "torba1.png"
ykiyafet1 = "ykiyafet1.png"
yayakkabi1 = "yipranmisa1.png"
at = "yereat.png"
bagaj = "bagaj.png"
balik = "balik.png"
envanterdoldu = False
region = (449, 187, 598, 346)
interval = 30
timer = None
zamanlayici = None
metal = 0
torba = 0
psise = 0
csise = 0
tas = 0
ykiyafet = 0
yayakkabi = 0
yosunu = 0
#######################################################
                ##GEREKLİ FONKSİYONLAR##
#######################################################

class HushPrints:
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self._stdout

    def write(self, x):
        # İstemediğiniz çıktıları buraya ekleyin
        if not any(keyword in x for keyword in ["preprocess", "inference", "postprocess"]):
            self._stdout.write(x)

    def flush(self):
        pass


def set_console_title(title):
    if os.name == "nt":
        os.system(f"title {title}")

def clear_console():
    os.system("cls")

def fetch_serial_keys():
    url = "https://raw.githubusercontent.com/widearth/serialkeys/refs/heads/main/serialkey"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip().split("\n")
    else:
        print("Serial key listesi çekilemedi.")
        return []

# def fetch_hwid_id():
#     url = "https://raw.githubusercontent.com/widearth/serialkeys/refs/heads/main/hwid"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text.strip().split("\n")
#     else:
#         print("hwid id listesi çekilemedi.")
#         return []

def check_serial_key(serial_key, valid_serial_keys):
    return serial_key in valid_serial_keys
  
# def check_hwid_id(hwid, hwidler):
#     return hwid in hwidler

def oltayatakilmiyor():
    try:
        screenshot_location = pyautogui.locateOnScreen(oltayatakilmadi, confidence=0.7)
        if screenshot_location is not None:
            return True
        else:
            return False
    except Exception as e:

        return False

def balikvar():
    try:
        screenshot_location = pyautogui.locateOnScreen(balik, confidence=0.75, region=region)
        if screenshot_location is not None:
            return True
        else:
            return False
    except Exception as e:
        print("Hata:", str(e))
        return False


def dolduenvanterama():
    try:
        screenshot_location = pyautogui.locateOnScreen(dolduenvanter, confidence=0.7)
        if screenshot_location is not None:
            return True
        else:
            return False
    except Exception as e:

        return False
        
def tasbuldu():
    try:
        tasdur = pyautogui.locateOnScreen(tas1, confidence=0.998, region=region)
        screenshot_location = pyautogui.locateOnScreen(tasa, confidence=0.6, region=region)
        if screenshot_location is not None and tasdur is not None:
            return True
        else:
            return False
    except Exception as e:
        print("Hata tas:", str(e))
        return False

def camsisebuldu():
    try:
        csisedur = pyautogui.locateOnScreen(csise1, region=region, confidence=0.998)
        screenshot_location = pyautogui.locateOnScreen(cam_sise, confidence=0.7, region=region)
        if screenshot_location is not None and csisedur is None:
            return True
        else:
            return False
    except Exception as e:
        print("Hata camsise:", str(e))
        return False

def plastiksisebuldu():
    try:
        psisedur = pyautogui.locateOnScreen(psise1, region=region, confidence=0.998)
        screenshot_location = pyautogui.locateOnScreen(plastik_sise, confidence=0.7, region=region)
        if screenshot_location is not None and psisedur is None:
            return True
        else:
            return False
    except Exception as e:
        print("Hata plastiksise:", str(e))
        return False

def torbabuldu():
    try:
        torbadur = pyautogui.locateOnScreen(torba1, region=region, confidence=0.998)
        screenshot_location = pyautogui.locateOnScreen(plastik_torba, confidence=0.7, region=region)
        if screenshot_location is not None and torbadur is None:
            return True
        else:
            return False
    except Exception as e:
        print("Hata torba:", str(e))
        return False


def telsizbuldu():
    try:
        screenshot_location = pyautogui.locateOnScreen(telsiz, confidence=0.7, region=region)
        if screenshot_location is not None:
            return True
        else:
            return False
    except Exception as e:

        return False       

def metalbuldu():
    try:
        metaldur = pyautogui.locateOnScreen(metal1, region=region, confidence=0.998)
        screenshot_location = pyautogui.locateOnScreen(metal_konserve, confidence=0.7, region=region)
        if screenshot_location is not None and metaldur is None:
            return True
        else:
            return False
    except Exception as e:
        print("Hata metal:", str(e))
        return False

def yipranmisbuldu():
    try:
        ykiyafetdur = pyautogui.locateOnScreen(ykiyafet1, region=region, confidence=0.998)
        screenshot_location = pyautogui.locateOnScreen(yipranmis_kiyafet, confidence=0.7, region=region)
        if screenshot_location is not None and ykiyafetdur is None:
            return True
        else:
            return False
    except Exception as e:
        print("Hata yipranmis:", str(e))
        return False
    
def yipranmisayakkabibuldu():
    try:
        yayakkabidur = pyautogui.locateOnScreen(yayakkabi1, region=region, confidence=0.998)
        screenshot_location = pyautogui.locateOnScreen(yipranmis_ayakkabi, confidence=0.7, region=region)
        if screenshot_location is not None and yayakkabidur is None: 
            return True
        else:
            return False
    except Exception as e:
        print("Hata yipranmisa:", str(e))
        return False
    
def yosunbuldu():
    try:
        yosundur = pyautogui.locateOnScreen(yosun1, region=region, confidence=0.998)
        screenshot_location = pyautogui.locateOnScreen(yosun, confidence=0.7, region=region)
        if screenshot_location is not None and yosundur is None:
            return True
        else:
            return False
    except Exception as e:
        print("Hata yosun:", str(e))
        return False
    region

# def balikyemi():
#     try:
#         balikyemidir = None
#         screenshot_location = None

#         # Önce balikyem1'i arıyoruz (seçili yem mi kontrolü)
#         try:
#             balikyemidir = pyautogui.locateOnScreen(balikyem1, region=region, confidence=0.3)
#         except pyautogui.ImageNotFoundException:
#             print("[HATA] 'balikyem1' görseli ekran görüntüsünde bulunamadı.")

#         # Sonra balikyem'i arıyoruz (ekranda yemi görüyor muyuz)
#         try:
#             screenshot_location = pyautogui.locateOnScreen(balikyem, region=region, confidence=0.3)
#         except pyautogui.ImageNotFoundException:
#             print("[HATA] 'balikyem' görseli ekran görüntüsünde bulunamadı.")

#         if screenshot_location is not None and balikyemidir is None:
#             print("[LOG] Balık yemi mevcut ama seçili değil.")
#             return True
#         else:
#             print("[LOG] Balık yemi ya seçili ya da görünmüyor.")
#             return False

#     except Exception as e:
#         print("[HATA] balikyemi fonksiyonu genel hata:", str(e))
#         return False

# def get_hwid():
#     w = wmi.WMI()  
#     computer_name = w.Win32_ComputerSystem()[0].Name
#     processor_info = w.Win32_Processor()[0].ProcessorId.strip()
#     combined_info = f"{computer_name}-{processor_info}"  
#     hwid = hashlib.sha256(combined_info.encode('utf-8')).hexdigest()  
#     return hwid
    
def my_function():
    global farekanks
    farekanks = False
    pyautogui.press('x')
    print("[LOG] Olta geri atıldı.")
    global zamanlayici
    zamanlayici = None
    global timer
    timer = None

def my_function1():
    pyautogui.press('x')
    print("[LOG] Olta geri atıldı.")
    global timer
    timer = None


def process_image(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return rgb   

def detect_object():
    while True:
        screen = np.array(ImageGrab.grab(bbox=(0, 30, 1024, 768)))
        processed_screen = process_image(screen)
        processed_screen = cv2.resize(processed_screen, (1024, 768), interpolation=cv2.INTER_LINEAR)
        input_tensor = transforms.ToTensor()(processed_screen).unsqueeze(0).to(device)
        results = model(input_tensor,verbose=False)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                if not telsizbuldu() or envanterdoldu == False:        
                    if cls == 4:
                        if conf >= 0.80:
                            cx, cy = x1 + w // 2, y1 + h // 2
                            click_to_position(cx, cy, 0)
                    if cls == 5:
                        if conf >= 0.80:
                            global farekanks
                            farekanks = True
                    if cls == 9:
                        if conf >= 0.60:
                            global px, py
                            px, py = x1 + w // 2, y1 + h // 2
                            puzzlebot()
                    if cls == 10:
                        if conf >= 0.60:
                            global px2, py2
                            px2, py2 = x1 + w // 2, y1 + h // 2
                    if cls == 11:
                        if conf >= 0.60:
                            global px3, py3
                            px3, py3 = x1 + w // 2, y1 + h // 2
                    
def click_to_position(x, y, duration=0.5):
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()  
    global farekanks
    farekanks = True
    global zamanlayici 
    global timer  
    if zamanlayici is not None:
        zamanlayici.cancel()
    zamanlayici = threading.Timer(7, my_function) 
    zamanlayici.start()
    if timer is not None:
        timer.cancel()
    
def puzzlebot():
    pyautogui.moveTo(px3, py3)
    time.sleep(0.5)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.moveTo(px+3, py3, duration=1)
    time.sleep(1)
    pyautogui.mouseUp()
    print('[LOG] Puzzle botu geçildi.')
    time.sleep(3)
    global farekanks
    farekanks = True
    global zamanlayici
    global timer
    if zamanlayici is not None:
        zamanlayici.cancel()
    zamanlayici = threading.Timer(7, my_function) 
    zamanlayici.start()
    if timer is not None:
        timer.cancel()


def switch_to_window(window_title):
    try:
        target_window = gw.getWindowsWithTitle(window_title)
        if len(target_window) == 0:
            print(f"{window_title} adında bir pencere bulunamadı.")
            return

        target_window = target_window[0]

        target_window.activate()

        print(f"{window_title} adlı pencereye geçiş yapıldı.")
    except Exception as e:
        print(f"Hata: {e}")  

def sestakip():
    bulundu = False
    global timer
    global envanterdoldu
    if timer is not None:
        timer.cancel()
    timer = threading.Timer(25, my_function1) 
    timer.start()
    while not bulundu:     
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name().lower() == "ragemp_game_ui.exe".lower():
                bulundu = True
                audio_meter = session._ctl.QueryInterface(IAudioMeterInformation)
                print(f"[LOG] Bu işlemin sesini dinlemede. : 'ragemp_game_ui.exe'")
                try:
                    while True:
                        if dolduenvanterama():
                            if timer is not None:
                                timer.cancel()
                            envanterdoldu = True
                            print("[LOG] Envanter doldu, tekneye depolanıyor.")
                            pyautogui.press('f7')
                            time.sleep(3)
                            pyautogui.press('t')
                            time.sleep(0.5)
                            pyautogui.typewrite('/cc')
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            pyautogui.press('t')
                            time.sleep(0.5)
                            pyautogui.typewrite('/bagaj')
                            time.sleep(0.5)
                            pyautogui.press('enter')
                            time.sleep(0.5)
                            while balikvar():
                                if timer is not None:
                                    timer.cancel()
                                screenshot_location = pyautogui.locateOnScreen(balik, confidence=0.75, region=region)
                                if screenshot_location is not None:
                                    x, y = pyautogui.center(screenshot_location)
                                    pyautogui.moveTo(x-10, y)
                                    pyautogui.click()
                                    time.sleep(0.2)
                                    bagajaat = pyautogui.locateOnScreen(bagaj, confidence=0.6)
                                    if bagajaat is not None:
                                        xx, yy = pyautogui.center(bagajaat)
                                        pyautogui.moveTo(xx, yy)
                                        pyautogui.click()
                                        time.sleep(0.2)          
                                        print(f"[LOG] Bagaja balık atıldı.")
                                    else:
                                        pass
                            print("[LOG] Envater boşaltıldı.")
                            pyautogui.press('tab')
                            time.sleep(1)
                            pyautogui.press('f7')
                            time.sleep(1)
                            pyautogui.press('f7')
                            time.sleep(1)
                            pyautogui.press('x')
                            print("[LOG] Olta geri atıldı.")                       
                        else:    
                            if oltayatakilmiyor():
                                if timer is not None:
                                    timer.cancel()
                                timer = threading.Timer(25, my_function1) 
                                timer.start()
                                print("[LOG] Olta yetişemedi, tekrar olta atılıyor.")
                                time.sleep(3)
                                pyautogui.press('x')
                                global farekanks
                                farekanks = False
                            else:
                                if farekanks == False:
                                    peak = audio_meter.GetPeakValue()
                                    if peak > 0.04:
                                        if timer is not None:
                                            timer.cancel()
                                        timer = threading.Timer(25, my_function1) 
                                        timer.start()
                                        print("[LOG] Oltaya birşeyler geldi, çekiliyor.")
                                        pyautogui.press('x')
                                        time.sleep(1.7)
                                        print("[LOG] Balık tutuldu.")
                                        time.sleep(1.7)
                                        envanterdoldu = False 
                                        if dolduenvanterama() is False:
                                            pyautogui.press('x')
                                            print("[LOG] Olta geri atıldı.")
                except KeyboardInterrupt:
                    print("[LOG] Durduruldu.")
                    break
        if not bulundu:
            time.sleep(1)

# def send_discord_message(webhook_url, message):
#     data = {
#         "content": message
#     }
#     response = requests.post(webhook_url, json=data)

# def get_cpu_id():
#     result = subprocess.run(['wmic', 'cpu', 'get', 'ProcessorId'], stdout=subprocess.PIPE)
#     return result.stdout.decode('utf-8').split('\n')[1].strip()

# def get_motherboard_serial():
#     result = subprocess.run(['wmic', 'baseboard', 'get', 'SerialNumber'], stdout=subprocess.PIPE)
#     return result.stdout.decode('utf-8').split('\n')[1].strip()

# def get_user_name():
#     result = subprocess.run(['wmic', 'computersystem', 'get', 'name'], stdout=subprocess.PIPE)
#     return result.stdout.decode('utf-8').split('\n')[1].strip()

# def get_location_info(ip_address):
#     response = requests.get(f'http://ipinfo.io/{ip_address}/json')
#     data = response.json()
    
#     city = data.get('city')
#     bolge = data.get('region')
#     country = data.get('country')
    
#     return city, bolge, country

def on_home_key_press(event): 
    if event.name == 'home': 
        print("[LOG] Home tuşuna basıldı, program kapanıyor.")
        tespit_thread.terminate()
        okeylet_thread.terminate() 
        os._exit(0)

keyboard.on_press(on_home_key_press)

if __name__ == "__main__":
    windowlar = gw.getWindowsWithTitle("RAGE Multiplayer")
    if windowlar:
        window = windowlar[0]
        window.activate()
        window.maximize()
        time.sleep(0.5)

    print("[LOG] İlk olta atıldı.")
    keyboard.press_and_release('x')

    tespit_thread = Process(target=sestakip)
    okeylet_thread = Process(target=detect_object)
    try:
        okeylet_thread.start()
        tespit_thread.start()

        okeylet_thread.join()
        tespit_thread.join()
    except KeyboardInterrupt:
        print("Processes interrupted. Cleaning up...")
        tespit_thread.terminate()
        okeylet_thread.terminate()

    keyboard.wait('home')
