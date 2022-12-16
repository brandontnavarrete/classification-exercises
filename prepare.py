from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import pandas as pd


def split_data(df,col):
    

    train_validate, test = train_test_split(df, test_size=.2,stratify=df[col])
    
    train, validate = train_test_split(train_validate,test_size=.3,stratify=train_validate[col])



    return train, validate, test

def prep_tidy(df):
    '''
        take in presupposed version of tidy bases on acquire.py and make appropriate 
        changes.
    
    positional arg : uncleaned tidy
    return: cleaned tidy
    '''
   
   
    df = df.rename(columns={'Unnamed: 0':'name'})
    
    
    return df


def prep_titanic(df):
    
    df = df.drop_duplicates()
    
    cols_to_drop = ['deck', 'embarked', 'class', 'age','passenger_id']
    df = df.drop(columns=cols_to_drop)
    
    df['embark_town'] = df.embark_town.fillna(value='Southampton')
    
    dummy_df = pd.get_dummies(df[['sex','embark_town']], dummy_na=False, drop_first =     True)
    
    df = pd.concat([df, dummy_df], axis=1)  
    
    return df

def prep_telco(df):
    
    df = df.drop(columns=['Unnamed: 0'])
    
    
    df = df.drop_duplicates()
    
    cols_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id']
    df = df.drop(columns=cols_to_drop)
    
  
    dummy_df = pd.get_dummies(df[[
     'gender',
     
     'partner',
     'dependents',
     'phone_service',
     'multiple_lines',
     'online_security',
     'online_backup',
     'device_protection',
     'tech_support',
     'streaming_tv',
     'streaming_movies',
     'paperless_billing',
     'churn',
     'contract_type',
     'internet_service_type',
     'payment_type']], dummy_na=False,drop_first = True )
    
    df = pd.concat([df, dummy_df], axis=1)  
    
    return df
    