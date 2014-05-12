#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is a script to wrap files in text:{} for Chambua
# internews KE HIV@30 project
import sys
import traceback
import argparse
import glob
import urllib2
import os


def save_file(content, filename, dir):
    filename = os.path.join(dir, os.path.basename(filename))
    target = open(filename, 'w')
    target.write(content)
    target.close()


def main():
    parser = argparse.ArgumentParser(description='Wrap file content in json')
    parser.add_argument('-p', '--pattern', default='./*.txt', help='foo')
    parser.add_argument('-o', '--output', default='./output', help='foo')
    args = parser.parse_args()

    url = 'http://chambua.ushahidi.com/v1/tags'
    for file in glob.glob(args.pattern):
        with open(file, "r+") as f:
            data = f.read()
            req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
            rq = urllib2.urlopen(req)
            response = rq.read()
            rq.close()
            save_file(response, file, args.output)
        

if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt, e:
        raise e
    except SystemExit, e:
        raise e
    except Exception, e:
        print str(e)
        traceback.print_exc()
        sys.exit(1)
