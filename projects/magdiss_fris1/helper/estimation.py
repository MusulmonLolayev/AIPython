import tkinter.filedialog
import matplotlib.pyplot as plt

def Estimation(a, ln):
    a = a[a[:, 0].argsort()]
    """
        Ushbu funksiya, sinflararo o'xshashlik va sinflararo farq kriteriyasini hisoblash uchun xizmat qiladi:
        values - miqdoriy alomatning qiymatlari, list;
        classes - miqdoriy alomatning sinfi, list;
        ln - sinflardagi obyektlar soni, list;
        Qaytuvchi natija:
        max_value - kriteriyaning qiymati;
        min_index - miqdoriy alomatning minimum qiymati indeksi;
        opt_index - miqdoriy alomatning kriteriya bo'yicha optimal chegarasining indexi;
        max_index - miqdoriy alomatning maximum qiymati indeksi;
    """
    # u[x, y] is count of x index of interval and y class. x is index of interval's and y is index of class. Where are x = {0, 1}.
    u = [[0, 0], [0, 0]]
    # Result values
    # Default of max value of Kriteriya is 0
    max_value = 0
    opt_index = 0
    
    # maxraj
    m1 = ln[0] * (ln[0] - 1) + ln[1] * (ln[1] - 1)
    m2 = 2 * ln[0] * ln[1]
    
    # for begin from 0 to len(vaules) - 1, beacuse each interval need min one object
    for x in range(a.shape[0] - 1):
        # Count object's in fisrt interval by class
        sinf = int(a[x][1]) - 1
        u[0][sinf] += 1

        # Calculate len of object's by class in second interval
        u[1][0] = ln[0] - u[0][0]
        u[1][1] = ln[1] - u[0][1]

        # if current object and next object aren't eqvivalent
        if a[x][0] != a[x + 1][1]:
            sum1 = 0.0
            sum2 = 0.0
            # Furmulation
            for y in range(0, 2):
                for z in range(0, 2):
                    sum1 += u[y][z] * (u[y][z] - 1)
                    sum2 += u[y][z] * (ln[1 - z] - u[y][1 - z])
            
            current_max = (sum1 / m1) * (sum2 / m2)
            # Check current max than more max value
            if current_max > max_value:
                max_value = current_max
                opt_index = x
    return max_value, opt_index

def Normalizing_Min_Max(a, res, types = None):
    for j in range(len(a[0])):
        if types == None or types[j] != 0:
            _min = a[0][j]
            _max = a[0][j]
            for i in range(len(a)):
                if _min > a[i][j]:
                    _min = a[i][j]
                if _max < a[i][j]:
                    _max = a[i][j]
            diff = _max - _min
            for i in range(len(a)):
                a[i][j] = (a[i][j] - _min) / diff

def drawobjects(a, classes = None, className = None, objectLabel = None, isVisibleLabel = False):
    
    # for just lie the package matplotlib for include the tkinter
    #tkinter.filedialog.ask
    
    g1_x = []
    g1_y = []

    g2_x = []
    g2_y = []

    x = []
    y = []

    for item in range(len(a)):
        if classes[item] == 0:
            g1_x.append(a[item][0])
            g1_y.append(a[item][1])
        else:
            g2_x.append(a[item][0])
            g2_y.append(a[item][1])
        x.append(a[item][0])
        y.append(a[item][1])

    g1 = (g1_x, g1_y)
    g2 = (g2_x, g2_y)

    data = (g1, g2)
    colors = ("red", "green")
    groups = ("Birinchi sinf", "Ikkinchi sinf")

    # Create plot
    fig = plt.figure()
    fig.suptitle("Obyektlarning ikki o'lchovli fazoda joylashish o'rni")
    ax = fig.add_subplot(1, 1, 1)

    for data, color, group in zip(data, colors, groups):
        x1, y1 = data
        ax.scatter(x1, y1, alpha=0.8, c=color, edgecolors='none', s=10, label=group)

    for i in range(len(x)):
        ax.annotate(str(i + 1), (x[i], y[i]))
    
    plt.title('Obyektlar oynasi')
    plt.legend(loc=2)
    plt.show()