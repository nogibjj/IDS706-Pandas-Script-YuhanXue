import pandas as pd
import matplotlib.pyplot as plt

def get_mean(df: pd.DataFrame, col: str):
    return df[col].mean()

def get_median(df: pd.DataFrame, col: str):
    return df[col].median()

def get_stddev(df: pd.DataFrame, col: str):
    return df[col].std()

def get_scatter_plot(df: pd.DataFrame, xcol: str, ycol: str, title: str, xlabel: str, ylabel: str):
    plt.scatter(df[xcol], df[ycol])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(xlabel + "_vs_" + ylabel + '.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('diabetes.csv')
    print(data.head())
    print('=====================================')
    print('Data Report')
    for col in data.columns:
        print('============ ' + col + ' ============')
        print('Mean:', get_mean(data, col))
        print('Median:', get_median(data, col))
        print('Std Dev:', get_stddev(data, col))
    print('=====================================')
    get_scatter_plot(data, 'Age', 'BMI', 'Age vs. BMI', 'Age', 'BMI')
    