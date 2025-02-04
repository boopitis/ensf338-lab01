import json
import timeit
import numpy as np
import matplotlib.pyplot as plt

# Change size field in num records to 42
def change_size(num):
    for i in range(num):
        json_object[i]['payload']['size'] = 42

if __name__ == '__main__':
    avg_times = []
    list_lengths = [1000, 2000, 5000, 10000]

    # Load json data
    with open('large-file.json', mode='r', encoding='utf-8') as in_file:
        file_contents = in_file.read()
    json_object = json.loads(file_contents)

    # For each list_length in list_lengths, calculate average time spent to change list_length amount of records
    for list_length in list_lengths:
        tm = timeit.timeit(lambda: change_size(list_length), number=100)
        avg = tm / 100
        avg_times.append(avg)
        print(f"Average time to modify {list_length} records:", avg)


    # Reverse json and write to output file
    #reversed_json_object = list(reversed(json_object))
    #with open('output.2.3.json', 'w', encoding='utf-8') as out_file:
    #    json.dump(reversed_json_object, out_file, ensure_ascii=False, indent=2)

    # Create linear regression plot 
    slope, intercept = np.polyfit(list_lengths, avg_times, 1)
    plt.scatter(list_lengths, avg_times)
    line_values = [slope * x + intercept for x in list_lengths]
    plt.plot(list_lengths, line_values, 'r')
    plt.xlabel("number of Records")
    plt.ylabel("average processing time")
    print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))
    plt.show()

    # Close opened files
    in_file.close()
    #out_file.close()