import csv

def candidate_elimination(filename):
    with open(filename, 'r') as f:
        data = list(csv.reader(f))

    # Remove header
    data = data[1:]

    # Initialize S and G
    num_attributes = len(data[0]) - 1
    S = ['0'] * num_attributes
    G = [['?' for _ in range(num_attributes)]]

    for instance in data:
        attributes = instance[:-1]
        label = instance[-1]

        if label == 'Yes':  # Positive example
            for i in range(num_attributes):
                if S[i] == '0':
                    S[i] = attributes[i]
                elif S[i] != attributes[i]:
                    S[i] = '?'

            # Remove hypotheses from G inconsistent with S
            G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(num_attributes))]

        else:  # Negative example
            new_G = []
            for g in G:
                for i in range(num_attributes):
                    if g[i] == '?' and S[i] != attributes[i]:
                        temp = g.copy()
                        temp[i] = S[i]
                        new_G.append(temp)
            G = new_G

    return S, G


# Run the algorithm
S_final, G_final = candidate_elimination('data.csv')

print("Final Specific Hypothesis (S):", S_final)
print("Final General Hypotheses (G):", G_final)
