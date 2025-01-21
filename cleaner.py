import re
import sys

#####
# Place this script somewhere and import re and sys if needed
# copy any text containing SHA-256 SHA-1 or MD5 hashes and save it in a text file
# cd to the script location and provide the input and output files as positional args (or use full file paths)
# Usage: python cleaner.py <input_file> <output_file>
#####

def clean_hashes(value):
    algos = [r'\b[a-fA-F0-9]{32}\b', r'\b[a-fA-F0-9]{40}\b', r'\b[a-fA-F0-9]{64}\b']
    hashes = []
    words = re.split(r'[^a-fA-F0-9]', str(value))
    for word in words:
        for algo in algos:
            if (re.match(algo, word)) and (word not in hashes):
                hashes.append(word)
    return hashes

def main():
    try:
        if len(sys.argv) == 3:
            with open(sys.argv[1], 'r') as f:
                data = f.read()
            cleaned = clean_hashes(data)
            with open(sys.argv[2], 'w') as f:
                f.write('\n'.join(cleaned))
        else:
            print('Usage: python cleaner.py <input_file> <output_file>')
    except FileNotFoundError:
        print('File not found. Please provide a valid full file path.')

if __name__ == '__main__':
    main()