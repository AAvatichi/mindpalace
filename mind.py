"""
This file create a cli for user to add the the mind palace 
"""
import argparse
import config
import json


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('type', choices=config.CHOICE)
    parser.add_argument('text', nargs='?')

    args = parser.parse_args()
    return args 


def main():
    #args = parse_args()
    #print "TAGS in {}".format(args.type)
    
    palace_object = json.load(config.FILE)
    print "DSFds"
    print palace_object["idea"]["tags"]


if __name__ == '__main__':
    main()
