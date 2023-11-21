import json
import sys

def write(save_file):

    with open(save_file) as file_data:
        print(f'Opening {save_file}...')
        save_data = json.dumps(json.loads(file_data.read()),separators=(',', ':'))
        print(f'Opened {save_file}.')

    new_hex_data = bytearray()

    print(f'Reading complete. Beginning conversion...')

    for c in save_data:
        new_hex_data.append(ord(c))
        new_hex_data.append(0)

    with open(save_file.replace('.json', ''), 'wb') as file_data:
        file_data.write(new_hex_data)
        print(f'Finished conversion.')

def main():

    if len(sys.argv) != 1:
        try:
            write(sys.argv[1])
            input('Your save file has been converted to SMRPG format. Press enter to quit.')
        except:
            input('Your edited json save file is either corrupted or incompatible. Press enter to quit.')

    else:
        input('Drag your edited json save file on the python script. Press enter to quit.')

if __name__ == '__main__':
    main()