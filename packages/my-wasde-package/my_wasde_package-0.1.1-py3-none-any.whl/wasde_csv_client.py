import pandas as pd
import requests
from io import StringIO
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class WasdeCSVClient:

    Wasde=pd.read_csv("Wasde.csv")

# Convert ReportDate column to datetime and find the max date
    dummy =   pd.to_datetime(Wasde["ReportDate"], format="%B %Y")

    start_date = dummy.max()

# Get the current date
    end_date = datetime.today().replace(day=1)  # Set to first of the current month

# Generate list of months between start and end date
    month_list = pd.date_range(start=start_date, end=end_date, freq='MS')[1:].strftime("%Y-%m").tolist()

# Formatting the list as required
    formatted_month_list = [f'{month}' for month in month_list]

# Print the result
    print(formatted_month_list)


# Optionally adjust this User-Agent string to mimic a standard browser.
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0"}

    all_dfs=[]
    for x in formatted_month_list:
        link =  f"https://www.usda.gov/sites/default/files/documents/oce-wasde-report-data-{x}.csv"
        try:
        # Add a custom User-Agent header and set a timeout
            response = requests.get(link, headers=headers, timeout=10)
        # Raise an HTTPError if the response code was unsuccessful
            response.raise_for_status()

        # Convert the response text into a pandas DataFrame
            csv_text = response.text
            df = pd.read_csv(StringIO(csv_text), skiprows=0)
            all_dfs.append(df)
            print(f"Successfully downloaded {link}")

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error for {link}: {http_err}")
        except requests.exceptions.RequestException as req_err:
        # This catches all other requests-related errors (ConnectionError, Timeout, etc.)
            print(f"Request error for {link}: {req_err}")
        except Exception as e:
            print(f"Unknown error for {link}: {e}")
    
    if all_dfs:
        combined_df = pd.concat(all_dfs,ignore_index=True)
        combined_df = pd.concat([Wasde,combined_df],ignore_index=True)
        combined_df.to_csv("Wasde.csv", index=False)
        print("Combined CSV saved as Wasde.csv")
    else:
        print("No DataFrames to combine; downloads may have failed or Data is Up to date ",f'Last Wasde Report Updated: {Wasde["ReportDate"].iloc[-1]} ')

    def __init__(self, csv_file='Wasde.csv'):
        """
        Initializes the client by reading data from a local CSV
        and building lists of valid commodities and regions.
        """
        self.wasde_data = pd.read_csv(csv_file)
        
        # Create lists of valid commodities and regions
        self.commodity_list = self.wasde_data['Commodity'].unique().tolist()
        self.region_list = self.wasde_data['Region'].unique().tolist()

    def query(self, commodity, region, world_summary=False, cleaned=True):
        """
        Query for a specific commodity and one or more regions.
        If 'region' is a list, it handles multiple regions at once.
        Otherwise, treat it as a single region.
        """
        # 1) Validate commodity
        if commodity not in self.commodity_list:
            raise ValueError(f"Commodity '{commodity}' not found in the data.")

        # 2) Normalize 'region' to a list if it's a string
        if isinstance(region, str):
            region = [region]

        # 3) Validate each region in the list
        for r in region:
            if r not in self.region_list:
                raise ValueError(f"Region '{r}' not found in the data.")

        # 4) Filter by commodity + region(s)
        query_df = self.wasde_data.loc[
            (self.wasde_data['Commodity'] == commodity) &
            (self.wasde_data['Region'].isin(region))
        ].copy()

        # If you need “world_summary” logic, you could add it here

        # 5) Format and return
        return self.format(query_df, fancy=cleaned)

    def format(self, df, fancy=True):
        """
        Splits data into (current_year, last_year, two_years_ago),
        then optionally pivots and cleans the result. Returns a tuple
        of three DataFrames.

        We interpret 'ProjEstFlag' to classify rows:
          - current_year   if 'Proj' in the flag
          - last_year      if 'Est'  in the flag
          - two_years_ago  otherwise

        Then we pivot so that each (Region, Attribute) is a column, and
        each ReleaseDate is a row, resulting in a multi-level column index.
        Finally, we compute "Use" = "Domestic Use" + "Exports" and
        "STU" = "Ending Stocks" / "Use" for each region.
        """
        # Classify rows by 'ProjEstFlag'
        wasde_frame_configs = {
            'current_year':   df['ProjEstFlag'].str.contains('Proj', na=False),
            'last_year':      df['ProjEstFlag'].str.contains('Est', na=False),
            'two_years_ago': ~df['ProjEstFlag'].str.contains('Proj|Est', na=False)
        }
        df['estimate_type'] = None
        for label, condition in wasde_frame_configs.items():
            df.loc[condition, 'estimate_type'] = label

        # Build three subsets
        df_current = df[df['estimate_type'] == 'current_year'].copy()
        df_last    = df[df['estimate_type'] == 'last_year'].copy()
        df_two_ago = df[df['estimate_type'] == 'two_years_ago'].copy()

        # Return them raw if not fancy
        if not fancy:
            return (df_current, df_last, df_two_ago)

        def pivot_subset(subset_df):
            """
            1) Parse 'ReleaseDate' to a proper datetime (if not already).
            2) Pivot so each row is one distinct ReleaseDate,
               columns are (Region, Attribute),
               and values are 'Value'.
            3) Sort by ReleaseDate ascending.
            4) Compute "Use" and "STU" for each region.
            """
            if subset_df.empty:
                return subset_df

            # Ensure ReleaseDate is datetime
            subset_df["ReleaseDate"] = pd.to_datetime(subset_df["ReleaseDate"])

            # Sort by the parsed date
            subset_df.sort_values('ReleaseDate', ascending=True, inplace=True)

            # We'll drop non-essential columns for the pivot
            drop_cols = [
                'WasdeNumber', 'Commodity', 'ProjEstFlag', 'MarketYear',
                'estimate_type', 'ReleaseTime', 'ForecastYear',
                'ForecastMonth', 'ReliabilityProjection', 'ReportTitle', 'ReportDate'
            ]
            subset_df = subset_df.drop(columns=[c for c in drop_cols if c in subset_df], errors='ignore')

            # Pivot: index = ReleaseDate, columns = (Region, Attribute), values = Value
            pivoted_df = subset_df.pivot_table(
                index='ReleaseDate',
                columns=['Region','Attribute'],
                values='Value'
            )

            # Add "Use" = "Domestic Use" + "Exports", and "STU" = "Ending Stocks"/Use
            for r in pivoted_df.columns.levels[0]:
                domestic_use = pivoted_df.get((r, 'Domestic Use'), pd.Series([0]*len(pivoted_df), index=pivoted_df.index))
                exports      = pivoted_df.get((r, 'Exports'), pd.Series([0]*len(pivoted_df), index=pivoted_df.index))
                pivoted_df[(r, 'Use')] = domestic_use + exports

                end_stocks   = pivoted_df.get((r, 'Ending Stocks'), pd.Series([0]*len(pivoted_df), index=pivoted_df.index))
                use_series   = pivoted_df[(r, 'Use')].replace({0: pd.NA})
                pivoted_df[(r, 'STU')] = end_stocks / use_series

            # Sort columns by region and then by attribute
            pivoted_df = pivoted_df.sort_index(axis=1, level=[0,1])

            return pivoted_df

        # Pivot each subset
        cleaned_current = pivot_subset(df_current)
        cleaned_last    = pivot_subset(df_last)
        cleaned_two_ago = pivot_subset(df_two_ago)
        cleaned_current = cleaned_current[["ReleaseDate","Region","Beginning Stocks","Production","Imports","Domestic Use","Exports","Ending Stocks","Use","STU"]]
        cleaned_last    = cleaned_last[["ReleaseDate","Region","Beginning Stocks","Production","Imports","Domestic Use","Exports","Ending Stocks","Use","STU"]]
        cleaned_two_ago = cleaned_two_ago[["ReleaseDate","Region","Beginning Stocks","Production","Imports","Domestic Use","Exports","Ending Stocks","Use","STU"]]


        return (cleaned_current, cleaned_last, cleaned_two_ago)
