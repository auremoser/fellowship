#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is a script to make chambua data work with a d3 node-edge map
# It takes two parameters:
# -p which is the pattern to match agains the files you want to parse
# -o which is the filename of the output json file.
# run in Terminal : python python make_cfl_struct.py -p './1980/*.txt' -o 'tree_structure.json'
# internews KE HIV@30 project
import sys
import traceback
import argparse
import glob
import json


def places(content):
    out = {}
    out['name'] = 'places'
    childs = []
    for p in content.get('places', []):
        place = {}
        place['name'] = p.get('name')
        place['place_type'] = p.get('place_type')
        childs.append(place)

    out['children'] = childs
    return out


def people(content):
    out = {}
    out['name'] = 'people'
    childs = []
    for person in content.get('people', []):
        childs.append(person)

    out['children'] = childs
    return out


def organizations(content):
    out = {}
    out['name'] = 'organizations'
    childs = []
    for org in content.get('organizations', []):
        childs.append(org)

    out['children'] = childs
    return out


def main():
    parser = argparse.ArgumentParser(description='Wrap file content in json')
    parser.add_argument('-p', '--pattern', default='./*.txt', help='Glob pattern files to match')
    parser.add_argument('-o', '--output', default='./hiv.json', help='Output path')
    args = parser.parse_args()

    result = {"name":"Aids", "children":[]}
    years = {"name":"Years","children":[]}

    for file in glob.glob(args.pattern):
        print "Reading file {0}".format(file)
        with open(file, "r+") as f:
            out = {}
            out['name'] = file
            childs = []

            content = json.loads(f.read())

            #people
            childs.append(people(content))
            #places
            childs.append(places(content))
            #organizations
            childs.append(organizations(content))

            out['children'] = childs

            years['children'].append(out)

    result['children'].append(years)

    print json.dumps(result)
    try:
        with open(args.output, "w") as f:
            f.write(json.dumps(result))
    except Exception, e:
        print e

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

