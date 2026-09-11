import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf

from src.config import DEFAULT_UNIT


def plot_daily_profile(df, value_col, title, xlabel, ylabel, unit = DEFAULT_UNIT):

    hourly_data = df.groupby(df.index.hour)[value_col].agg(['mean', 'median', 'std'])

    paint_seasonal_profile(hourly_data, title, xlabel, ylabel, unit)


def plot_daily_seasonal_profile(df, value_col, season, title, xlabel, ylabel, unit=DEFAULT_UNIT):    

    season_filtered_data = df[df['season'] == season]

    hourly_data = season_filtered_data.groupby([season_filtered_data.index.hour])[value_col].agg(['mean', 'median', 'std'])
    paint_seasonal_profile(hourly_data, title, xlabel, ylabel, unit)




def plot_predictions_vs_actual(timestamps, y_true, y_pred):
    """
    Plot predictions against actual values ​​over time.
    """
    raise NotImplementedError



def set_seasonal_profile(df):
    seasonal_data = df.copy()
    seasonal_data['season'] = seasonal_data.index.month % 12 // 3 + 1
    seasonal_data['season'] = seasonal_data['season'].map({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'})
    return seasonal_data

def paint_seasonal_profile(df, title, xlabel, ylabel, unit = DEFAULT_UNIT):
    _, ax = plt.subplots(figsize=(10, 5))
    
    color_mean = "#6ecfff"
    color_median = "#fa655a"
    
    ax.plot(df.index, df['mean'], label='Mean', color=color_mean, lw=2)
    ax.plot(df.index, df['median'], label='Median', color=color_median, lw=2)
    clean_inf_limit = np.clip(df['mean'] - df['std'], a_min=0, a_max=None)

    ax.fill_between(
        df.index, 
        clean_inf_limit,
        df['mean'] + df['std'], 
        alpha=0.2, color=color_mean, label='Standard Deviation (from Mean)'
    )
    
    idx_max_mean = df['mean'].idxmax()
    val_max_mean = df['mean'].max()
    
    idx_max_med = df['median'].idxmax()
    val_max_med = df['median'].max()
    
    ax.scatter(idx_max_mean, val_max_mean, color="#3aa0d1", s=40, zorder=5)
    ax.scatter(idx_max_med, val_max_med, color="#cc4137", s=40, zorder=5)
    
    statistics_text = (
        f"Peak Values:\n"
        f"Max Mean: {val_max_mean:.1f} {unit} (at {idx_max_mean}:00h)\n"
        f"Max Median: {val_max_med:.1f} {unit} (at {idx_max_med}:00h)"
    )
    
    ax.text(
        0.02, 0.95, statistics_text,
        transform=ax.transAxes,
        fontsize=9.5,
        verticalalignment='top',
        bbox={'boxstyle': 'round,pad=0.5', 'facecolor': 'white', 'edgecolor': '#e0e0e0', 'alpha': 0.9}
    )

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(range(24))
    ax.grid(True, linestyle='--')
    
    ax.spines[['right', 'top']].set_visible(False)    
    ax.legend(loc='upper right')
    
    plt.show()


def scatter_tcc_gbi_by_season(df, x_col, x_label, y_col, y_label, season):
    _, ax = plt.subplots(figsize=(10, 5))

    df = df[(df['H_sun'] > 0) & (df['season'] == season)]
    
    scatter = ax.scatter(df[x_col], df[y_col], alpha=0.5, c=df['H_sun'], cmap='plasma', s=10, vmin=0, vmax=80)
    
    ax.set_title(f'Scatter Plot of {x_label} vs {y_label} ({season})')
    ax.set_xlabel(f'{x_label} ({x_col})')
    ax.set_ylabel(f'{y_label} ({y_col})')
    ax.grid(True, linestyle='--')
    
    ax.spines[['right', 'top']].set_visible(False)    
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('H_sun')
    
    plt.show()


def plot_autocorrelation(df, value_col, lags=48):

    autocorr = df[value_col].autocorr(lag=24)
    print(f"Yesterday's autocorrelation: {autocorr:.3f}")

    _, ax = plt.subplots(figsize=(10, 5))
    plot_acf(df[value_col], lags=lags, alpha=0.05, ax=ax)
    ax.set_title(f'Autocorrelation of {value_col}')
    ax.set_xlabel('Lags')
    ax.set_ylabel('Autocorrelation')
    ax.spines[['right', 'top']].set_visible(False)    
    ax.grid(True, linestyle='--')
    plt.show()