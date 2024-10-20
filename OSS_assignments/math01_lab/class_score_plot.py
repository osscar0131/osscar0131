import matplotlib.pyplot as plt
import os

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    #print(os.getcwd()) print your current file workspace directory
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    #print(midterm_kr)
    #print('/////')
    #print(final_kr)
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]

    # TODO) Plot midterm/final scores as points

    score_scatter = plt.figure(1)

    plt.scatter(x=midterm_kr, y=final_kr,
                c="red", label='Korean')
    plt.scatter(x=midterm_en, y=final_en,
                c="blue", marker="+", label='English')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.xlim([0, 125])
    plt.ylim([0, 100])
    plt.grid()
    plt.legend()
    # TODO) Plot total scores as a histogram
    
    score_hist = plt.figure(2)
    
    plt.hist(x=total_kr, bins=range(0, 105, 5),
             color='red', label='Korean')
    plt.hist(x=total_en, bins=range(0, 105, 5),
             color=(0.5, 0.5, 1, 0.8), label='English')
    plt.xlabel('Total scores')
    plt.ylabel('The number of students')
    plt.xlim([0, 100])
    plt.legend()

    plt.show()