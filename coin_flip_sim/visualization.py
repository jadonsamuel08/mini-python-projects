import matplotlib.pyplot as plt

def plot_results(results):
    values = results.values()
    labels = results.keys()

    plt.bar(labels, values)
    plt.title("Coin Flip Results")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.show()