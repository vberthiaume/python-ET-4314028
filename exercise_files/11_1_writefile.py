from argparse import ArgumentParser 

parser = ArgumentParser()

# create the arguments. Convention is for full words to have -- in front. These are added as DYNAMIC ATTRIBUTES OMG
parser.add_argument('--output', '-o', required=True, help='The destination file for the output of this program')
parser.add_argument('--text', '-t', required=True, help='The text to write to the file')

# parse the arguments
args = parser.parse_args()

# the arguments you added above are magically available as attributes here
with open(args.output, 'w') as f:
    f.write(args.text+'\n')

print(f'Wrote "{args.text}" to file "{args.output}"')