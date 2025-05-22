import os
import time
import random
import base64
import platform

# --- XỬ LÝ CHUỖI ---
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def reverse_string(s: str) -> str:
    return s[::-1]

# --- THỜI GIAN ---
def current_time() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")

def wait_seconds(seconds: int):
    print(f"Đợi {seconds} giây...")
    time.sleep(seconds)

# --- FILE ---
def read_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# --- HỆ THỐNG ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def system_info():
    return platform.platform()

# --- RANDOM ---
def random_password(length=8):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

def roll_dice():
    return random.randint(1, 6)

# --- MẠNG ---
def ping_google():
    return os.system("ping -c 1 google.com" if os.name != "nt" else "ping -n 1 google.com") == 0

# --- BASE64 ---
def encode_base64(text: str) -> str:
    return base64.b64encode(text.encode()).decode()

def decode_base64(encoded: str) -> str:
    return base64.b64decode(encoded.encode()).decode()

# --- TEST ĐƠN GIẢN ---
if __name__ == "__main__":
    print("🌟 Chạy test nhanh cho các hàm:")
    print("Palindrome của 'madam':", is_palindrome("madam"))
    print("Reverse 'hello':", reverse_string("hello"))
    print("Thời gian hiện tại:", current_time())
    print("Random password:", random_password())
    print("Ping Google:", "Thành công" if ping_google() else "Thất bại")
    print("Mã hóa 'hello' ->", encode_base64("hello"))
