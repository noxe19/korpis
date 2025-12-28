import matplotlib.pyplot as plt

def visualize(success_count, error_count):
    labels = ["Успешно", "Ошибки"]
    values = [success_count, error_count]

    plt.bar(labels, values)
    plt.title("Результаты ETL загрузки")
    plt.ylabel("Количество записей")
    plt.show()
