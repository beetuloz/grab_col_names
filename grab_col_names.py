# Libraries
import pandas as pd
import seaborn as sns

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Return categorical, numerical and cardinal variables in a dataframe

    Parameters:
        dataframe: dataframe
        cat_th: int, float
            Number of class threshold for categorical variables that looks like numerical
        car_th: int, float
            Number of class threshold for cardinal variables that looks like categorical

    Returns:
        cat_cols: list
            categorical variables list
        num_cols: list
            numerical variables list
        cat_but_car: list
            cardinal variables list (that looks like categorical)

    Notes:
        cat_cols + num_cols + cat_but_car = total number of variables
        num_but_cat is in cat_cols
    """
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in dataframe.columns if dataframe[col].dtypes in ["int", "float"] and dataframe[col].nunique() < cat_th]

    cat_but_car = [col for col in dataframe.columns if
                   str(dataframe[col].dtypes) in ["category", "object"] and dataframe[col].nunique() > car_th]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car


# Test
df = sns.load_dataset("titanic")
grab_col_names(df)


cat_cols, num_cols, cat_but_car = grab_col_names(df)