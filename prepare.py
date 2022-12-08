from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



def split_data(df,col):
    

    train_validate, test = train_test_split(df, test_size=.2,stratify=df[col])
    
    train, validate = train_test_split(train_validate,test_size=.3,stratify=train_validate[col])



                                       
    return train, validate, test