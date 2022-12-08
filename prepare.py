from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


def split_data(df):
    

    train_validate, test = train_test_split(df, test_size=.2)
    train, validate = train_test_split(train_validate,
                                       test_size=.3

                                       )
    return train, validate, test