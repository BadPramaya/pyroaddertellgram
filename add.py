o
    K��b
  �                   @   s  d dl mZmZ d dlmZmZmZmZmZm	Z	m
Z
 d dlmZmZ d dl mZ d dlmZ d dlmZmZ d dlZd dlZd dlZe�  ejZejZejZejZejZej Z!ej"Z#ej$Z%eeeee!gZ&dd	� Z'd
Z(dZ)e'�  e*e� de#� d��Z+zede+� �e(e)d�Z,W n e-y� Z. ze/de0e.�� �� W Y dZ.[.ndZ.[.ww ze,�1�  W n e2y�   e,�3�  e,�1�  Y nw e/e#� de%� e,�4� j5� d�� e*e� de#� d��Z6e/e� d�� e/e� d�� e/e� d�� e7e*e� de� d���Z8e8d k�re0e*e!� de� ���Z9ne0e*e!� de� ���Z9e/e%� d�d � e7e*e#� de� ���Z:d Z;d Z<d Z=e=d Z>z�de6v �ree6�?d�d  Z@ze,�Ae@� e/e%� d!e,�4� j5� d"e� d#�� W n( e-�yd Z. zW Y dZ.[.ndZ.[.ww e,�Ae6� e/e%� d!e,�4� j5� d"e� d#�� e8d k�r�e,�Ae9� e/e%� d!e,�4� j5� d"e� d$�� n-ze9�?d�d  ZBe,�AeB� e/d!e,�4� j5� d%�� W n e-�y� Z. zW Y dZ.[.ndZ.[.ww W n" e-�y� Z. ze/e� d&�� e/e� e.� �� W Y dZ.[.ndZ.[.ww g ZCe,�De6�ZCeEe0eC��Z<e<d k�s�J �e=e<k�re/e� d'�� e/e%� d(e=� �� d ZFeCD ]�ZGe=d 7 Z=eFd)k�r'e/e� d*��  n�z0e8d k�r6e,�He9eGjGjI� ne,�He9eGjGjI� e/e#� eGjGj5� de� d+�� e;d 7 Z;e�Je:� W �q e�y{ ZK ze/e#� eGjGj5� de� d,eK� �� W Y dZK[K�qdZK[Kw e�y� ZL ze/e#� eGjGj5� de� d,eL� �� eFd 7 ZFW Y dZL[L�qdZL[Lw e-�y� Z. ze/e#� eGjGj5� de� d,e.� �� W Y dZ.[.�qdZ.[.ww e;d k�r�e/d-� n	e/e� d.e� �� e,�3�  e*e� d/e� d0e� d1e� d2��ZMeMd3k�r�e�Nd4� dS eMd5k�re/d6� dS e/d7� dS )8�    )�Client�filters)�	FloodWait�ApiIdInvalid�PhoneCodeExpired�PhoneCodeInvalid�UserNotParticipant�PhoneNumberInvalid�SessionPasswordNeeded)�PeerIdInvalid�ChatAdminRequired)�errors)�	Forbidden)�init�ForeNc                  C   s<   dd l } g d�}|D ]}t| �t�� |� �� q
td� d S )Nr   )uu   ██████╗ ███████╗ █████╗ ███████╗████████╗u{   ██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝uh   ██████╔╝█████╗  ███████║███████╗   ██║uh   ██╔══██╗██╔══╝  ██╔══██║╚════██║   ██║uh   ██████╔╝███████╗██║  ██║███████║   ██║uf   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝z+=============Dev-@Godmrunal==============

)�random�print�choice�colors)r   �b�char� r   �#/storage/emulated/0/pyrogram/add.py�banner#   s
   
r   i<|z Z 9b70b20efd67e9b99edc395d78407cfazSend Phone Number To Use:�
zmemory/)�api_id�api_hashz	errror : z Logged In Via � z2Public group Username without @ to scrape members:z

zChoose an optionz[0] Add to public groupz[1] Add to private groupzEnter choice:z(Enter public group Username without @:

zEnter private group link:
�~�2   z*Enter delay time per request 0 for None]:
�<   z
/joinchat/�   zUser: �z-- Joined group to scrapez-- Joined group to Addz -- Joined group to addzFailed to join groupzNo members to add!zStart:�
   z.Too many Peer Flood Errors! Closing session...z--> DONEz--> error-->zAdding session endedzAdding donezpress zY z*if you want Use another Number Else Press z N�Yzpython add.py�NZDonezplease choose options)OZpyrogramr   r   Zpyrogram.errorsr   r   r   r   r   r	   r
   Z*pyrogram.errors.exceptions.bad_request_400r   r   r   r   Zcoloramar   r   �time�sys�osZRESET�nZLIGHTGREEN_EXZlgZLIGHTRED_EX�rZWHITE�wZCYAN�cyZLIGHTYELLOW_EXZyeZLIGHTMAGENTA_EXZmgZLIGHTBLUE_EXZlbr   r   r   r   �inputZphone_numberZsession�	Exception�er   �strZconnect�ConnectionErrorZ
disconnectZget_meZ
first_nameZscraped_grp�intr   �targetZ
sleep_timeZadding_statusZapprox_members_count�index�stop�splitZg_hashZ	join_chatZgrp_hash�membersZget_chat_members�lenZpeer_flood_status�userZadd_chat_members�id�sleepZfk�opZsed�systemr   r   r   r   �<module>   s�    $	���


$��
 

"
�����



 � � ��

 

