import matplotlib.pyplot as plt

def generate_manhattan_plot(input_file):
    chromosomes = {}
    colors = ['red', 'dodgerblue', 'green', 'mediumpurple', 'darkorange']
    color_index = 0

    with open(input_file, 'r') as file:
        next(file)  
        for line in file:
            line = line.strip()
            snp, chr_num, bp, p = line.split()

            if chr_num not in chromosomes:
                chromosomes[chr_num] = {'snps': [], 'color': colors[color_index]}
                color_index = (color_index + 1) % len(colors)

            chromosomes[chr_num]['snps'].append((int(bp), float(p)))

    fig, ax = plt.subplots()
    ax.set_xlabel('Chromosome')
    ax.set_ylabel('D-value')
    ax.set_title('Manhattan Plot')

    x_ticks = []
    x_tick_labels = []

    x_position = 0
    for chr_num, data in chromosomes.items():
        snps = data['snps']
        color = data['color']

        x_ticks.append(x_position + len(snps) // 2)
        x_tick_labels.append(chr_num)

        x_values = [x_position + i for i in range(len(snps))]
        y_values = [p for _, p in snps]

        ax.scatter(x_values, y_values, color=color, alpha=0.8)

        x_position += len(snps)

    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_tick_labels)

    ax.axhline(y=-1.0183, color='red', linestyle='-')

    plt.ylim(-2, 5)
    plt.legend()
    plt.show()

# Usage
input_file = '/home/yami/CLRMANHATTAN'
generate_manhattan_plot(input_file)

