#!/usr/bin/env python3

import csv
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--path", help="Path of the Manulex CSV file")
args = parser.parse_args()

lines = []
with open(args.path, newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    lines.append(row[0:4])

def line_to_json(line):
  word, phonetic, blending, relations = line

  return (
    {
      'word': word,
      'phonetic': phonetic,
      'blending': blending.split('-'),
      'relations': relations.split('.')
    }
  )

words = map(line_to_json, lines[1:-1])

print(
  json.dumps(list(words))
)
