import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('resnet_lstm_dftimit_lq_predictions_on_celebdf.csv')

# Plot a histogram of the "Prediction" column
plt.hist(df['Prediction'], bins=30, alpha=0.5, label='Prediction', edgecolor='black')

# Plot a histogram of the "Label" column
plt.hist(df['Label'], bins=30, alpha=0.5, label='Label', edgecolor='black')

plt.title('Distribution of Predictions and Labels')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Add a legend to distinguish the two histograms
plt.legend(loc='upper right')

plt.show()