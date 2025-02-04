import json
import timeit
import numpy as np
import matplotlib.pyplot as plt

def change_size(num):
    for i in range(num):
        json_object[i]['payload']['size'] = 42

if __name__ == '__main__':
    
    # load json data
    with open('large-file.json', mode='r', encoding='utf-8') as in_file:
        file_contents = in_file.read()
    json_object = json.loads(file_contents)
    
    # change size field to 42 of the first 1000 records 1000 times
    tm = timeit.repeat(lambda: change_size(1000), repeat=1000, number=1)  
    

    # reverse json and write to output file
    reversed_json_object = list(reversed(json_object))
    with open('output.2.3.json', 'w', encoding='utf-8') as out_file:
        json.dump(reversed_json_object, out_file, ensure_ascii=False, indent=2)

    # close opened files
    in_file.close()
    out_file.close()

    # remove outliers for better histogram
    tm = np.array(tm)
    q1 = np.percentile(tm, 25)
    q3 = np.percentile(tm, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    filtered_data = tm[(tm >= lower_bound) & (tm <= upper_bound)]

    # plot histogram
    plt.hist(filtered_data, bins="auto", edgecolor="black")
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.title("Time to process the first 1000 records")
    plt.show()
