import matplotlib.pyplot as plt

def task_2():
    data = {
        'ahmedabad': [120, 200, 10],
        'surat': [150, 175, 7],
        'rajkot': [75, 150, 15]
    }

    categories = ['Category 1', 'Category 2', 'Category 3']
    colors = ['b', 'g', 'r']
    bar_width = 0.2

    plt.figure(figsize=(10, 6))
    for i, (city, values) in enumerate(data.items()):
        x_positions = [j + bar_width * i for j in range(len(categories))]
        plt.bar(x_positions, values, width=bar_width, color=colors[i], label=city)

    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Multiple Bar Graph')
    plt.xticks([r + bar_width for r in range(len(categories))], categories)
    plt.legend()
    plt.tight_layout()
    plt.show()

task_2()
