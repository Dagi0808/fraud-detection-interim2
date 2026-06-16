def create_time_features(df):
    df["hour_of_day"] = df["purchase_time"].dt.hour
    df["day_of_week"] = df["purchase_time"].dt.dayofweek

    df["time_since_signup"] = (
        df["purchase_time"] - df["signup_time"]
    ).dt.total_seconds()

    return df