import os 
import env
import pandas as pd

def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data(get_connection):
    filename = "titanic.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else :
    # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename,index = False)

    # Return the dataframe to the calling code
        return df  

def get_iris_data(get_connection):
    filename = "iris_and_name.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
    # read the SQL query into a dataframe
        df = pd.read_sql('''SELECT * FROM measurements 
                            left join species
                            using (species_id)

                        ''', get_connection('iris_db'))

    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

    # Return the dataframe to the calling code
        return df  
    
def get_telco_data(get_connection):
    filename = "telco.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        
    # read the SQL query into a dataframe
        df = pd.read_sql(
    
        '''
        select * from customers
        join contract_types
        using (contract_type_id)
        join internet_service_types
        using (internet_service_type_id)
        join payment_types
        using (payment_type_id)
        ''', get_connection('telco_churn'))

    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

    # Return the dataframe to the calling code
        return df 
    
def get_tidy_attendance(get_connection):
    filename = "tidy_attendance.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else :
    # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM attendance',get_connection("tidy_data"),
                      index_col = None  )

    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename,index = False)

    # Return the dataframe to the calling code
        return df 
    
def get_tidy_cake(get_connection):
    filename = "tidy_cake.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else :
    # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM cake_recipes',get_connection("tidy_data"),
                      index_col = None  )

    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename,index = False)

    # Return the dataframe to the calling code
        return df 


