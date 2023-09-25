import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class TimeColumnMissingError(Exception):
    pass

def transform_time_to_seconds(df):
    if 'time' not in df.columns:
        raise TimeColumnMissingError("A coluna 'time' não existe no arquivo CSV.")
    
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'] - df['time'][0]
    df['time'] = df['time'].dt.total_seconds()
    return df

def fill_non_numeric_with_mean(df):
    df = df.apply(pd.to_numeric, errors='coerce')
    df.fillna(df.mean(), inplace=True)
    return df

def create_subplots(df, filename, output_folder):
    column_info = {
        'pleth_1': ('Vermelho', 'Distal', 'Pleth 1'),
        'pleth_2': ('Infravermelho', 'Distal', 'Pleth 2'),
        'pleth_3': ('Verde', 'Distal', 'Pleth 3'),
        'pleth_4': ('Vermelho', 'Proximal', 'Pleth 4'),
        'pleth_5': ('Infravermelho', 'Proximal', 'Pleth 5'),
        'pleth_6': ('Verde', 'Proximal', 'Pleth 6')
    }

    fig, axes = plt.subplots(len(column_info), 1, figsize=(10, 8), sharex=True)
    fig.suptitle(f'Leituras PPG para {filename}')

    for i, (col, (wavelength, location, pleth)) in enumerate(column_info.items()):
        if col in df.columns:
            color = 'red' if wavelength == 'Vermelho' else 'green' if wavelength == 'Verde' else 'purple'
            
            axes[i].plot(df['time'], df[col], color=color)
            axes[i].set_title(f'{pleth} - {wavelength} - {location}')
            axes[i].set_ylabel('Amplitude')
            axes[i].set_xlabel('Tempo (s)')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_filename = os.path.join(output_folder, os.path.splitext(os.path.basename(filename))[0] + '.png')
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig(output_filename, bbox_inches='tight', pad_inches=0)
    plt.close()

def process_csv_files(folder_path, output_folder):
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            print(f"Processando arquivo: {filename}")
            input_file = os.path.join(folder_path, filename)
            
            try:
                df = pd.read_csv(input_file)
                
                df = transform_time_to_seconds(df)
                
                df = fill_non_numeric_with_mean(df)
                
                create_subplots(df, filename, output_folder)
            
            except TimeColumnMissingError as e:
                print(f"Erro: {e}")
                continue
            except Exception as e:
                print(f"Erro ao processar arquivo {filename}: {e}")
                continue

if __name__ == "__main__":
    folder_path = '/home/palhares/Documents/PTT-PPG-PhysioNet/csv/'
    output_folder = '/home/palhares/Documents/PTT-PPG-PhysioNet/figures/'
    process_csv_files(folder_path, output_folder)
