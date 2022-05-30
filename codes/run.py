import json
import os

def read_data(path='./'):
    dialogs = json.load(open(os.path.join(path, 'Dialogs.json'), 'r'))
    search_behaviors = json.load(open(os.path.join(path, 'SearchBehaviors.json'), 'r'))
    return dialogs, search_behaviors

if __name__ == '__main__':
    dialogs, search_behaviors = read_data(path='../dataset') # modify para *path* to your dataset stored path

    for dialog in dialogs:
        print(f'for the dialog (id = {dialog["id"]}):')
        for key in dialog:
            if key != 'turns':
                print(f'{key}: {dialog[key]}')
            else:
                print('turns:')
                for turn in dialog['turns']:
                    print(f'\tturn (id = {turn["id"]}): ')
                    for key in turn:
                        print(f'\t\t{key}: {turn[key]}')

        break



    print('\n\n')

    for query_request in search_behaviors:
        print(f'for the query_request (id = {query_request["id"]}):')
        for key in query_request:
            print(f'{key}: {query_request[key]}')
        break