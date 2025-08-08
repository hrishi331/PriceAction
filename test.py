import nsepy as nse
import pandas as pd
from datetime import date

df = nse.get_history(symbol="RELIANCE", start=date(2020,1,1), 
                     end=date(2025,8,8),
                     index=False,
                     series='EQ')
print(df)