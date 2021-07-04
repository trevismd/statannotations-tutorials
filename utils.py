import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def print_n_projects(df, df_name="the dataset"):
    print(f"There are {df.shape[0]} projects in {df_name}.")
    
    
def describe_array(array: np.array, name=None):
    name = f"\"{name}\"".ljust(20) if name is not None else ''
    print(f"{name}Number of projects: {len(array)}" + "\t" 
          + f"Min: {array.min():.2f}" + "\t"
          + f"Max: {array.max():.2f}" +"\t"
          + f"Avg: {array.mean():.2f}" + "\t"
          + f"Median: {np.percentile(array, 50):.2e}")
    
    
def get_projects_by(df, row_name, func):
    """Returns a list of projects, sorted by `func` result by `Subcategory`"""
    func = getattr(pd.core.groupby.generic.DataFrameGroupBy, func)
    grouped_df = (func(df.groupby("Subcategory"))
                  .sort_values(by="ID", ascending=False)
                  .reset_index())
    ans = []
    for index, row in grouped_df.iterrows():
        ans.append((f"{row.Subcategory.ljust(20)} {row[[row_name]].values[0]:.2e}"))
    return ans


def print_projects_by(df, row_name, func):
    """Prints a list of projects, sorted by `func` result by `Subcategory`"""
    projects = get_projects_by(df, row_name, func)
    print("\n".join(projects))
    
    
def label_plot_for_subcat(ax):
    plt.title("Goal amounts per Tech Subcategory")
    ax.set_ylabel("Goal ($)")
    ax.set_xlabel("Tech Project Subcategory")
    
    
def label_plot_for_state(ax):
    plt.title("Goal amounts per project State")

    ax.set_ylabel("Goal ($)")
    ax.set_xlabel("Project State")
    
    
def get_log_ax():
    fig, ax = plt.subplots(1,1, figsize=(12,6))
    ax.set_yscale("log")
    return ax

def add_legend(ax):
    ax.legend(loc=(1.05, 0.5))
