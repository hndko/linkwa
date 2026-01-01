#!/usr/bin/env python3
"""
LinkWa - Powerful WhatsApp Link Generator
Created by Kyuoko | Updated for Modern Usage
"""
import os
import sys
import time
import urllib.parse
import argparse
import webbrowser

# ANSI Colors
C_RED = "\033[91m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_BLUE = "\033[94m"
C_CYAN = "\033[96m"
C_RESET = "\033[0m"
C_BOLD = "\033[1m"

# Icons
I_WA = "🟢"
I_LINK = "🔗"
I_ERROR = "❌"
I_SUCCESS = "✅"
I_INFO = "ℹ️"
I_INPUT = "⌨️"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{C_GREEN}{C_BOLD}")
    print(r"  _     _       _  __        __    ")
    print(r" | |   (_)_ __ | |_\ \      / /_ _ ")
    print(r" | |   | | '_ \| __|\ \ /\ / / _` |")
    print(r" | |___| | | | | |_  \ V  V / (_| |")
    print(r" |_____|_|_| |_|\__|  \_/\_/ \__,_|")
    print(f"{C_RESET}")
    print(f"  {C_CYAN}{I_WA}  Powerful WhatsApp Link Generator {I_WA}{C_RESET}")
    print(f"  {C_YELLOW}Creating Connections, Simplified.{C_RESET}\n")
    print(f"  {C_BLUE}[-] Created By : Kyuoko{C_RESET}")
    print(f"  {C_BLUE}[-] Updated By : Antigravity{C_RESET}\n")

def format_number(phone):
    """Formats phone number to international format (default ID 62)."""
    # Remove non-numeric characters
    phone = ''.join(filter(str.isdigit, phone))

    if not phone:
        return None

    if phone.startswith("08"):
        return "62" + phone[1:]
    elif phone.startswith("62"):
        return phone
    else:
        # Assume international format or user knows what they are doing
        return phone

def generate_link(phone, text):
    """Generates the WhatsApp API link."""
    base_url = "https://api.whatsapp.com/send"
    params = {"phone": phone}
    if text:
        params["text"] = text
    return f"{base_url}?{urllib.parse.urlencode(params)}"

def interactive_mode():
    """Runs the interactive CLI menu."""
    while True:
        banner()
        print(f"{C_YELLOW}  [1] {C_RESET}Generate WhatsApp Link")
        print(f"{C_YELLOW}  [2] {C_RESET}About")
        print(f"{C_YELLOW}  [3] {C_RESET}Exit")

        try:
            choice = input(f"\n{C_CYAN}  {I_INPUT}  Choose an option: {C_RESET}")
        except KeyboardInterrupt:
            print(f"\n\n{C_GREEN}Exiting...{C_RESET}")
            sys.exit(0)

        if choice == '1':
            print(f"\n{C_BLUE}  --- Generator Mode ---{C_RESET}")
            phone = input(f"  {I_INPUT}  Enter WhatsApp Number (e.g., 08123...): ")
            formatted_phone = format_number(phone)

            if not formatted_phone:
                print(f"  {C_RED}{I_ERROR} Invalid phone number!{C_RESET}")
                time.sleep(2)
                continue

            text = input(f"  {I_INPUT}  Enter Message (Optional): ")

            print(f"\n  {C_CYAN}{I_INFO} Processing...{C_RESET}")
            time.sleep(0.5)

            link = generate_link(formatted_phone, text)

            print(f"\n  {C_GREEN}{I_SUCCESS} Link Generated Successfully!{C_RESET}")
            print(f"  {C_BOLD}{link}{C_RESET}\n")

            try:
                open_choice = input(f"  {I_LINK} Open in browser? (y/n): ").lower()
                if open_choice == 'y':
                    webbrowser.open(link)
            except KeyboardInterrupt:
                pass

            input(f"\n  Press Enter to return to menu...")

        elif choice == '2':
            print(f"\n{C_CYAN}  --- About ---{C_RESET}")
            print(f"  This tool helps you create direct WhatsApp links quickly.")
            print(f"  It automatically formats '08' numbers to international '62' format.")
            print(f"  Supports URL encoding for messages.")
            input(f"\n  Press Enter to return to menu...")

        elif choice == '3':
            print(f"\n  {C_GREEN}Goodbye! {I_WA}{C_RESET}")
            break
        else:
            print(f"  {C_RED}Invalid Option!{C_RESET}")
            time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description="Generate WhatsApp Direct Links")
    parser.add_argument("-n", "--number", help="Target WhatsApp Number")
    parser.add_argument("-t", "--text", help="Message to send")
    parser.add_argument("--no-output", action="store_true", help="Suppress output (print only link)")

    args = parser.parse_args()

    if args.number:
        formatted_phone = format_number(args.number)
        if not formatted_phone:
            sys.stderr.write("Invalid phone number supplied.\n")
            sys.exit(1)

        link = generate_link(formatted_phone, args.text)

        if args.no_output:
            print(link)
        else:
            # Check if we are being piped or redirected
            if not sys.stdout.isatty():
                print(link)
            else:
                print(f"{C_GREEN}{I_SUCCESS} Link: {C_RESET}{link}")

    else:
        try:
            interactive_mode()
        except KeyboardInterrupt:
            print(f"\n\n{C_GREEN}Exiting...{C_RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()