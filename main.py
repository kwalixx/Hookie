#/usr/bin/env python
# -*- encoding: utf-8 -*-

from colorama import Fore, init
from banner import banner
from hookie import Hookie
import argparse

init(autoreset=True)



def main():
    banner()  # Header

    parser = argparse.ArgumentParser(description='Powerful WebHook tool', prog='Hookie')
    parser.add_argument('--hook', metavar='url', type=str, help='URL of target WebHook', required=True)
    parser.add_argument('--spam', metavar='nb_req', type=int, help='Set number of requests you want to send')

    args = parser.parse_args()

    hook = Hookie(args.hook)
    if args.spam:
        hook.spam(args.spam)


if __name__ == '__main__':
    main()
