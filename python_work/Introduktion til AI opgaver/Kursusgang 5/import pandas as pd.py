import pandas as pd
import tarfile
import io

# Åbn tarfilen direkte
with tarfile.open('housing.tgz') as tar:
    # Find CSV-filen inde i tar-filen
    housing_csv = tar.extractfile('housing.csv')
    
    # Læs den ind i pandas direkte fra streamen
    housing_data = pd.read_csv(io.TextIOWrapper(housing_csv))

# Bekræft at data er læst korrekt
housing_data.head()
