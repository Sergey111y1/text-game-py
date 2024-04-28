import time  
import sys   
import keyboard
import os   
 
import textwrap   
 
from colorama import *

 

init()   
class textp:
    def text(self,text,crl,spe):

   
 
        def get_terminal_width():   
        
            return os.get_terminal_size().columns   
        

        self.text2 = text   
        
        temp = ""   
        

        # Плавная анимация с более мелкими задержками   
        
        #speed = 0.020
        self.speed = spe
        
        
        
        # Добавляем кириллицу в список возможных символов   
        
        all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*()-=_+[]{}|;:,.<>?/`~" + "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"   
        
        
        
        # Получаем ширину окна терминала   
        
        terminal_width = get_terminal_width()   
        
        
        
        # Перенос текста согласно ширине терминала   
        
        wrapped_text = textwrap.fill(self.text2, width=terminal_width)   
        
        
        
        # Проходим по каждой строке перенесённого текста   
        
        for line in wrapped_text.split('\n'):   
        
            for ch in line:   
        
                found = False   
        
                for i in all_characters:   
        
                    if not found:   
        
                        sys.stdout.write(crl + '\r' + temp + i)   
        
                        sys.stdout.flush()   
        
                        time.sleep(self.speed)   
        
                    if i == ch:   
        
                        temp += ch   
        
                        found = True   
        
            # Переносим каретку на следующую строку   
        
            sys.stdout.write(crl +'\n')   
        
            temp = ""   
        
        
        
        # Очищаем строку от лишних символов   
        
        sys.stdout.write('\r' + ' ' * terminal_width + '\r')   
        
        sys.stdout.flush()
# теперь мы можем воспользоватся движком.
textp.text(self=textp,text="Бесмысленный текст",crl=Fore.GREEN,spe=0.0001)
