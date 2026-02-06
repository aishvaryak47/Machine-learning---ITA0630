import csv


def find_s(training_data):
    hypothesis = ['0'] * (len(training_data[0]) - 1)
    for instance in training_data:
            if instance[-1] == 'Yes':
                for i in range(len(hypothesis)):
                    if hypothesis[i] == '0':
                        hypothesis[i] = instance[i]
                    elif hypothesis[i] != instance[i]:
                            hypothesis[i] = '?'
                            return hypothesis
with open('data.csv') as f:
    data = list(csv.reader(f))


print("Final Hypothesis:", find_s(data[1:]))
