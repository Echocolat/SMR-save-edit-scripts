import json
import sys

def parse(save_file):

    with open(save_file, 'rb') as file_data:
        print(f'Opening {save_file}...')
        save_data = file_data.read()
        print(f'Opened {save_file}.')

    new_hex_data = bytearray(save_data)
    print(f'Reading {save_file}...')
    
    for i in range(1, len(new_hex_data) // 2 + 1):
        del new_hex_data[i]

    print(f'Reading complete. Beginning conversion...')

    with open(f'{save_file}.json', 'w') as json_file:
        json_file.write(json.dumps(json.loads(new_hex_data), indent = 2))
        print(f'Finished conversion.')

def main():

    if len(sys.argv) != 1:
        try:
            parse(sys.argv[1])
            input('Your save file has been converted to json. Press enter to quit.')
        except:
            input('Your save file is either corrupted or incompatible. Press enter to quit.')

    else:
        input('Drag your save file on the python script. Press enter to quit.')

if __name__ == '__main__':
    main()