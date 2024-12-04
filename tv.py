import matplotlib.pyplot as plt
import math


# Функция для построения вариационного ряда
def calculate_variational_range(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]  # Меняем элементы местами
    return data


# Функция для нахождения экстремальных значений и размаха
def calculate_extreme_values_and_range(data):
    X_min = data[0]
    X_max = data[-1]
    range_data = X_max - X_min
    return X_min, X_max, range_data


# Функция для расчета математического ожидания
def calculate_mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)


# Дисперсия
def calculate_variance(data, mean):
    sum_ = 0
    for x in data:
        sum_ += data.count(x) * (x - mean) ** 2
    return sum_ / len(data)


# Нахождение медианы
def find_median(data):
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]


# Нахождение моды
def find_mode(data):
    freq = {}
    for num in data:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())  # Находим максимальную частоту
    modes = [num for num, count in freq.items() if count == max_freq]
    if len(modes) == 1:
        return modes[0]  # Возвращаем единственную моду
    else:
        return None  # Моды нет (несколько значений встречаются одинаково часто)


# Функция для построения гистограммы
def plot_histogram(data):
    plt.figure(figsize=(12, 6))
    plt.hist(data, bins=10, density=True, alpha=0.6, color='b', edgecolor='black')
    plt.title('Гистограмма')
    plt.xlabel('Значения')
    plt.ylabel('Плотность')
    plt.grid(True)
    plt.show()


# Функция для построения полигона частот
def plot_frequency_polygon(data):
    plt.figure(figsize=(12, 6))
    count, bins, ignored = plt.hist(data, bins=10, density=True, alpha=0.5, color='g', edgecolor='black')
    bin_centers = 0.5 * (bins[1:] + bins[:-1])
    plt.plot(bin_centers, count, marker='o', label='Полигон частот', color='r')
    plt.title('Полигон частот')
    plt.xlabel('Значения')
    plt.ylabel('Плотность')
    plt.legend()
    plt.grid(True)
    plt.show()


def foo(x, numbers):
    count = 0
    for value in numbers:
        if value < x:
            count += 1
    return count


# Функция для построения эмпирической функции распределения
def empirical_cdf(data):
    arr = []
    for i in range(len(data)):
        arr.append(foo(data[i], data) / len(data))
    return arr


def print_empricial_function(arr, data, max_value, min_value):
    print(f"\tx <= {min_value}: 0")
    for i in range(len(data) - 1):
        print(f"\t{data[i]} < x <= {data[i + 1]}: {arr[i]}")
    print(f"\tx > {data[-1]}: 1")


# Основная функция main
def main():
    data = [-0.76, -0.55, -0.62, 0.21, -1.31, 0.64, -0.21, -1.07, 0.21, 1.16,
            -1.14, 1.07, -0.14, -1.45, 1.45, 0.24, 1.46, 1.04, -0.31, -1.12]
    n = len(data)

    # Вариационный ряд
    data = calculate_variational_range(data)
    print("1. Вариационный ряд:", data)

    # Статистический ряд
    data2 = sorted(set(data))
    print("2. Статистический ряд:\n")
    print(f"\t{data2}")
    print(f"\t{[data.count(x) for x in data2]}")

    # Экстремальные значения и размах
    X_min, X_max, range_data = calculate_extreme_values_and_range(data)
    print("3. Минимальное значение:", X_min)
    print("4. Максимальное значение:", X_max)
    print("5. Размах:", range_data)

    # Математическое ожидание
    mean = calculate_mean(data)
    print("6. Выборочное среднее: ", mean)

    # Дисперсия
    variance = calculate_variance(data, mean)
    corrected_variance = (n / (n - 1)) * variance
    print(f"7. Выборочная дисперсия: {variance}")
    print(f"8. Исправленная выборочная дисперсия: {corrected_variance}")

    # Среднеквадратическое отклонение
    std_deviation = variance ** 0.5
    print("9. Выборочное среднеквадратическое отклонение:", std_deviation)
    print("10. Исправленное СКО:", corrected_variance ** 0.5)

    # Мода и медиана
    mode = find_mode(data)
    print("11. Медиана: ", find_median(data))
    print("12. Мода: ", mode if mode is not None else 'Мода отсутствует')

    # Эмпирическая функция распределения
    print(f"13. Эмпирическая функция распределения: ")
    arr = empirical_cdf(data)
    print_empricial_function(arr, data, data[0], data[-1])

    # 6. Построение гистограммы, полигона частот и доп. анализ
    minValue = X_min
    maxValue = X_max
    dataLength = n

    numberOfBins = math.ceil(1 + 3.322 * math.log10(n))
    binWidth = (maxValue - minValue) / (1 + 3.322 * math.log10(n))  # h
    binEdges = [minValue + i * binWidth - binWidth / 2 for i in range(numberOfBins + 1)]
    binCounts = [0] * numberOfBins

    # Подсчет частот для гистограммы
    for value in data:
        for i in range(numberOfBins):
            if binEdges[i] <= value < binEdges[i + 1]:
                binCounts[i] += 1
                break
        if value == binEdges[-1]:  # Учитываем крайний случай
            binCounts[-1] += 1

    # Вычисление относительных частот
    relativeFrequencies = [count / dataLength for count in binCounts]
    binCenters = [(binEdges[i] + binEdges[i + 1]) / 2 for i in range(numberOfBins)]
    print(f"Количество интервалов: {numberOfBins}")
    print(f"Длина интервала h: {binWidth}")
    print("Интервальный статистический ряд:")
    for i in range(numberOfBins):
        print(f"\t[{binEdges[i]}, {binEdges[i + 1]}): частота: {binCounts[i]}, частотность {binCounts[i] / 20}")
    print("\n")

    # Визуализация эмпирической функции распределения
    ecdfX = data
    ecdfY = arr
    plt.figure(figsize=(10, 5))
    plt.step(ecdfX, ecdfY, where="post", label="Эмпирическая функция распределения", color='black', linewidth=1,
             linestyle='--')

    for i in range(0, len(ecdfX) - 1):
        plt.hlines(y=ecdfY[i], xmin=ecdfX[i], xmax=ecdfX[i + 1], color='black', linestyle='-', linewidth=2)

    plt.xlabel("x", fontsize=12)
    plt.ylabel("F(x)", fontsize=12)
    plt.title("Эмпирическая функция распределения", fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Визуализация гистограммы
    plt.figure(figsize=(10, 5))
    plt.bar(
        [binEdges[i] for i in range(numberOfBins)],
        binCounts,
        width=binWidth,
        align="edge",
        alpha=0.6,
        color="teal",
        edgecolor="darkblue",
        label="Гистограмма"
    )
    plt.xlabel("Интервалы", fontsize=12)
    plt.ylabel("Частота", fontsize=12)
    plt.title("Гистограмма", fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Визуализация полигона частот
    plt.figure(figsize=(10, 5))
    plt.plot(binCenters, relativeFrequencies, marker='o', linestyle='-', color='purple',
             label="Полигон приведенных частот")
    plt.xlabel("Интервалы", fontsize=12)
    plt.ylabel("Относительная частота", fontsize=12)
    plt.title("Полигон приведенных частот", fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Запуск программы
if __name__ == "__main__":
    main()
