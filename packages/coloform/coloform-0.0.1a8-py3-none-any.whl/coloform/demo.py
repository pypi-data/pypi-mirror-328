from coloform.ansi import Back, Fore, Style

msg = (
    f"Look ma: {Style.UNDERLINED}more{Style.RESET_UNDERLINED} {Style.ITALICS}styles{Style.RESET_ITALICS}, "
    f"than we {Style.BOLD}ever{Style.RESET_ALL} "
    f"{Style.STRIKE_OUT}wanted{Style.RESET_STRIKE_OUT} "
    f"{Style.BLINK}needed{Style.RESET_BLINK}!\n"
    f"Also, {Fore.HEX_1234FF}HEX{Fore.RESET} and {Fore.RGB_0_255_255}RGB{Fore.RESET} "
    f"colors for {Style.DOUBLE_UNDERLINED}fore- and {Back.RGB_255_0_255}background{Style.RESET_ALL}.\n"
    f"Common {Fore.RED}aliases {Back.GREEN}just{Fore.RESET} work!{Style.RESET_ALL}"
)

if __name__ == "__main__":
    print(msg)
