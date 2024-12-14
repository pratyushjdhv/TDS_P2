# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",
#   "seaborn",
#   "matplotlib",
#   "httpx",
#   "chardet",
#   "python-dotenv",
#   "ipykernel",
#   "numpy",
#   "chardet"
# ]
# ///

import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import httpx
import chardet
from pathlib import Path
import logging
import numpy as np
from dotenv import load_dotenv
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

# Ensure token is retrieved from environment variable
def get_token():
    try:
        token = os.environ["AIPROXY_TOKEN"]
        # Validate token with a test API call
        response = httpx.post(
            API_URL,
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "Test token."}]},
            timeout=10.0
        )
        response.raise_for_status()
        logging.info("Token validated successfully.")
        return token
    except KeyError:
        logging.error("AIPROXY_TOKEN environment variable not set.")
        sys.exit(1)
    except httpx.RequestError:
        logging.error("Failed to validate the token. Check your network or token validity.")
        sys.exit(1)

def load_data(file_path):
    """Load CSV data with encoding detection."""
    if not os.path.isfile(file_path):
        logging.error(f"File '{file_path}' not found.")
        sys.exit(1)
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result.get('encoding', 'utf-8')
    logging.info(f"Detected file encoding: {encoding}")
    try:
        return pd.read_csv(file_path, encoding=encoding)
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        sys.exit(1)

def analyze_data(df, token):
    """Use LLM to suggest and perform data analysis."""
    if df.empty:
        logging.error("Dataset is empty.")
        sys.exit(1)

    prompt = (
        f"You are a data analyst. Given the following dataset information, provide an analysis plan:\n\n"
        f"Columns: {list(df.columns)}\n"
        f"Data Types: {df.dtypes.to_dict()}\n"
        f"First 5 rows of data:\n{df.head()}\n\n"
        "Suggest useful data analysis techniques, such as correlation analysis, regression, anomaly detection, clustering, or others."
    )

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = httpx.post(API_URL, headers=headers, json=data, timeout=30.0)
        response.raise_for_status()
        suggestions = response.json().get('choices', [{}])[0].get('message', {}).get('content', 'No suggestions.')
        logging.info("LLM Suggestions retrieved successfully.")
    except Exception as e:
        logging.error(f"Failed to retrieve LLM suggestions: {e}")
        suggestions = "No suggestions from LLM."

    numeric_df = df.select_dtypes(include=['number'])
    analysis = {
        'summary': df.describe(include='all').to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'correlation': numeric_df.corr().to_dict() if not numeric_df.empty else {}
    }
    logging.info("Data analysis complete.")

    return analysis, suggestions

def visualize_data(df, output_dir, analysis):
    """Generate and save enhanced visualizations."""
    sns.set(style="whitegrid", palette="muted")
    numeric_columns = df.select_dtypes(include=['number']).columns

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    if not numeric_columns.empty:
        # 1. Distribution Plots
        for column in numeric_columns:
            plt.figure(figsize=(6, 6))
            sns.histplot(df[column].dropna(), kde=True, color='steelblue', bins=30)
            plt.title(f'Distribution of {column}', fontsize=14)
            plt.xlabel(column, fontsize=12)
            plt.ylabel('Frequency', fontsize=12)
            plt.tight_layout()
            file_name = output_dir / f'{column}_distribution.png'
            plt.savefig(file_name, dpi=100)
            logging.info(f"Saved distribution plot: {file_name}")
            plt.close()

        # 2. Correlation Heatmap
        plt.figure(figsize=(8, 8))
        corr = df[numeric_columns].corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        sns.heatmap(
            corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', cbar=True, square=True,
            linewidths=0.5, annot_kws={"size": 10}
        )
        plt.title('Correlation Heatmap', fontsize=16)
        file_name = output_dir / 'correlation_heatmap.png'
        plt.tight_layout()
        plt.savefig(file_name, dpi=100)
        logging.info(f"Saved correlation heatmap: {file_name}")
        plt.close()

        # 3. Pairplot (if manageable size)
        if len(numeric_columns) <= 5:  # To avoid overwhelming plots
            pairplot = sns.pairplot(df[numeric_columns], diag_kind="kde", corner=True)
            pairplot.fig.suptitle("Pairwise Relationships", y=1.02, fontsize=16)
            file_name = output_dir / 'pairplot.png'
            pairplot.savefig(file_name, dpi=100)
            logging.info(f"Saved pairplot: {file_name}")
            plt.close()

    else:
        logging.warning("No numeric columns found for visualization.")

    # 4. Bar Plot for Categorical Columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    for column in categorical_columns:
        if df[column].nunique() <= 10:  # Limit to small categories for readability
            plt.figure(figsize=(8, 6))
            sns.countplot(data=df, x=column, palette="muted", order=df[column].value_counts().index)
            plt.title(f'Count of Each Category in {column}', fontsize=14)
            plt.xlabel(column, fontsize=12)
            plt.ylabel('Count', fontsize=12)
            plt.xticks(rotation=45, ha="right", fontsize=10)
            plt.tight_layout()
            file_name = output_dir / f'{column}_countplot.png'
            plt.savefig(file_name, dpi=100)
            logging.info(f"Saved bar plot: {file_name}")
            plt.close()

    logging.info("All visualizations generated successfully.")

def generate_narrative(analysis, token, file_path):
    """Generate narrative using LLM."""
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    prompt = (
        f"You are a data analyst. Provide a detailed narrative based on the following data analysis results for the file '{file_path.name}':\n\n"
        f"Column Names & Types: {list(analysis['summary'].keys())}\n\n"
        f"Summary Statistics: {analysis['summary']}\n\n"
        f"Missing Values: {analysis['missing_values']}\n\n"
        f"Correlation Matrix: {analysis['correlation']}\n\n"
        "Based on this information, provide insights into trends, outliers, anomalies, or patterns you detect."
    )

    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = httpx.post(API_URL, headers=headers, json=data, timeout=30.0)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        logging.error(f"Failed to generate narrative: {e}")
        return "Narrative generation failed."

def save_narrative_with_images(narrative, output_dir):
    """Save narrative to README.md and embed image links."""
    readme_path = output_dir / 'README.md'
    image_links = "\n".join(
        [f"![{img.name}]({img.name})" for img in output_dir.glob('*.png')]
    )
    with open(readme_path, 'w') as f:
        f.write(f"# Data Analysis Report\n\n{narrative}\n\n## Visualizations\n\n{image_links}")
    logging.info(f"Narrative successfully written to {readme_path}")

def main(file_path):
    logging.info("Starting autolysis process...")

    # Ensure input file exists
    file_path = Path(file_path)
    if not file_path.is_file():
        logging.error(f"File '{file_path}' does not exist.")
        sys.exit(1)

    # Load token
    token = get_token()

    # Load dataset
    df = load_data(file_path)
    logging.info("Dataset loaded successfully.")

    # Analyze data
    analysis, suggestions = analyze_data(df, token)
    logging.info(f"LLM Analysis Suggestions: {suggestions}")

    # Create output directory
    output_dir = Path(file_path.stem)

    # Generate visualizations
    visualize_data(df, output_dir, analysis)

    # Generate narrative
    narrative = generate_narrative(analysis, token, file_path)

    if narrative != "Narrative generation failed.":
        save_narrative_with_images(narrative, output_dir)
    else:
        logging.warning("Narrative generation failed. Skipping README creation.")

    logging.info("Autolysis process completed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error("Usage: python autolysis.py <file_path>")
        sys.exit(1)
    main(sys.argv[1])


    