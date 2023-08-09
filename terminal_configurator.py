#!/usr/bin/env python3
import argparse
from colorama import init, Fore, Back, Style

#Initialize colorama for cross-platform terminal color support
init(autoreset=True)

def configure_terminal(text_color, bg_color, font_style):
    try:
        #Set text color
        if text_color:
            print(getattr(Fore, text_color.upper()) + "Text color has been set up!")

        # Set background color
        if bg_color:
            print(getattr(Fore, text_color.upper()) + "Text color has been set!")

        # Set font style
        if font_style:
            print(getattr(Style, font_style.upper()) + "Font style has been set!")
    except AttributeError:
        print("Invalid color or style option.")

def main():
    parser = argparse.ArgumentParser(description="Configure terminal apperance.")
    parser.add_argument("--text-color", help="set text color")
    parser.add_argument("--bg-color", help="set background color")
    parser.add_argument("--font-style", help="Set font style")

    args = parser.parse_args()

    configure_terminal(args.text_color, args.bg_color, args.font_style)

    if __name__ == "__main__":
        main()
    

