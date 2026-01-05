#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 11:03:21 2026

@author: Rohith Reddy Mandala

Project name: QR code generator
"""

import qrcode


def createQRcode():
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        user_input = input("Please enter your website address: ").strip()

        if user_input:
            break

        attempts += 1
        print(f"Website is required. Attempts left: {max_attempts - attempts}")

    if not user_input:
        raise ValueError("Website not provided after 3 attempts")

    user_input_fileName = input("Please enter file name: ").strip()


    if not user_input_fileName:
        filename = user_input + ".png"
    elif not user_input_fileName.lower().endswith(".png"):
        filename = user_input_fileName + ".png"
    else:
        filename = user_input_fileName

    img = qrcode.make(user_input)
    img.save(filename)

    print(f"Your file has been saved as {filename}")

try:
    createQRcode()
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Unexpected error:", e)