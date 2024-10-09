import os
import pandas as pd

def get_database():
    # Get the current branch name
    current_branch = os.popen('git rev-parse --abbrev-ref HEAD').read().strip()

    
    
    # Return the appropriate data based on the branch
    if current_branch == 'develop':
        # Return only the first 3 lines for the test environment
        return pd.read_csv ("products.csv", nrows=3)
    else:
        return pd.read_csv ("products.csv")
        # Return the full dataset for production

# Usage
# from config import get_database()
# get_database = get_database()
# print(get_database)
