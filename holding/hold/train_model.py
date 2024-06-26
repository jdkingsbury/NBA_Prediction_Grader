import os
import yaml
import pandas as pd
from ludwig.api import LudwigModel

def train_model(config_path, dataset_path, output_directory):
    # Load config
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Load dataset
    dataset = pd.read_csv(dataset_path)

    # Initialize model
    model = LudwigModel(config)

    # Train model
    train_stats = model.train(dataset=dataset, output_directory=output_directory)

    # Output training stats
    print(train_stats)

    # Save model
    model_path = os.path.join(output_directory, 'model')
    model.save(model_path)

    return model_path, train_stats

if __name__ == '__main__':
    # Define paths
    config_path = './config/nba_training.yaml'
    dataset_path = './data/get_player_game_log_2544_2023-24.csv'
    output_directory = './results'

    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Train model
    model_path, train_stats = train_model(config_path, dataset_path, output_directory)

    # Output model path
    print(f'Model saved to: {model_path}')
    print('Training complete!')
