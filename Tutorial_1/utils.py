import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def print_n_projects(df, df_name="the dataset"):
    print(f"There are {df.shape[0]} projects in {df_name}.")
    
    
def describe_array(array: np.array, name=None, min_len=15):
    name = f"\"{name}\"".ljust(min_len) if name is not None else ''
    print(f"{name}Number of projects: {len(array)}" + "\t" 
          + f"Min: {array.min():.2f}" + "\t"
          + f"Max: {array.max():.2e}" + "\t"
          + f"Avg: {array.mean():.2f}" + "\t"
          + f"Median: {np.percentile(array, 50):.2e}")
    
    
def get_projects_by(df, row_name, func):
    """Returns a list of projects, sorted by `func` result by `Subcategory`"""
    # noinspection PyUnresolvedReferences
    func = getattr(pd.core.groupby.generic.DataFrameGroupBy, func)
    grouped_df = (func(df.groupby("Subcategory"))
                  .sort_values(by=row_name, ascending=False)
                  .reset_index())
    ans = []
    for index, row in grouped_df.iterrows():
        ans.append(
            f"{index+1}. {row.Subcategory.ljust(20-(index+1)//10)} "
            f"{row[[row_name]].values[0]:.2e}")
    return ans


def print_projects_by(df, row_name, func):
    """Prints a list of projects, sorted by `func` result by `Subcategory`"""
    projects = get_projects_by(df, row_name, func)
    print("\n".join(projects))
    
    
def label_plot_for_subcats(ax):
    plt.title("Goal amounts per Technology Subcategory", y=1.06)
    ax.set_ylabel("Goal ($)")
    ax.set_xlabel("Technology Project Subcategory", labelpad=20)
    
    
def label_plot_for_states(ax):
    plt.title("Goal amounts per project State", y=1.06)
    ax.set_ylabel("Goal ($)")
    ax.set_xlabel("Project State", labelpad=20)
    
    
def get_log_ax(orient="v"):
    if orient == "v":
        figsize = (12, 6)
        set_scale = "set_yscale"
    else:
        figsize = (10, 8)
        set_scale = "set_xscale"
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    fig.patch.set_alpha(1)
    getattr(ax, set_scale)("log")
    return ax


def add_legend(ax):
    ax.legend(loc=(1.05, 0.5))
