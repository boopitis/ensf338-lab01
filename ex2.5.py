import json
import timeit

def change_size(num):
    for data in json_object:
        data['payload']['size'] = num

if __name__ == '__main__':
    # load json data
    with open('large-file.json', mode='r', encoding='utf-8') as in_file:
        file_contents = in_file.read()
    json_object = json.loads(file_contents)
    
    # change size field to 42
    elapsed_time = timeit.timeit(lambda: change_size(42), number=10)

    # reverse json and write to output file
    reversed_json_object = list(reversed(json_object))
    with open('output.2.3.json', 'w', encoding='utf-8') as out_file:
        json.dump(reversed_json_object, out_file, ensure_ascii=False, indent=2)

    avg_time = elapsed_time / 10
    print("Average time to modify size in each record:", avg_time)