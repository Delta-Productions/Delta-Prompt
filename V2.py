#!/usr/bin/env python3
import argparse
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform terminal color support
init(autoreset=True)

# Define ASCII art graphics
GRAPHICS = {
    "star": r"""
        *
    *       *
        *
    """,
    "heart": r"""
    *       *  
*    * *    *
 *       * 
  *     *   
   *   *
    * *
     *
    """,
    "smiley": r"""
   ******  
 *      *
*  0  0  *
*    v   *
 * ------ 
   ****** 
    """
}

def configure_terminal(text_color, bg_color, font_style, graphic):
    try:
        # Set text color
        if text_color:
            print(getattr(Fore, text_color.upper()) + "Text color has been set!")

        # Set background color
        if bg_color:
            print(getattr(Back, bg_color.upper()) + "Background color has been set!")

        # Set font style
        if font_style:
            print(getattr(Style, font_style.upper()) + "Font style has been set!")

        # Display graphic
        if graphic:
            if graphic in GRAPHICS:
                print(getattr(Fore, "WHITE") + GRAPHICS[graphic])
            else:
                print("Invalid graphic option.")
    except AttributeError:
        print("Invalid color or style option.")

def main():
    parser = argparse.ArgumentParser(description="Configure terminal appearance.")
    parser.add_argument("--text-color", help="Set text color")
    parser.add_argument("--bg-color", help="Set background color")
    parser.add_argument("--font-style", help="Set font style")
    parser.add_argument("--graphic", choices=GRAPHICS.keys(), help="Display ASCII art graphic")

    args = parser.parse_args()

    configure_terminal(args.text_color, args.bg_color, args.font_style, args.graphic)

if __name__ == "__main__":
    main()
