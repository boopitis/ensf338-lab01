import json

if __name__ == '__main__':
    # load json data
    with open('large-file.json', mode='r', encoding='utf-8') as in_file:
        file_contents = in_file.read()
    json_object = json.loads(file_contents)
    
    # change size field to 42
    for data in json_object:
        data['payload']['size'] = 42

    # reverse json and write to output file
    reversed_json_object = list(reversed(json_object))
    with open('output.2.3.json', 'w', encoding='utf-8') as out_file:
        json.dump(reversed_json_object, out_file, ensure_ascii=False, indent=2)

    # Close opened files
    in_file.close()
    out_file.close()