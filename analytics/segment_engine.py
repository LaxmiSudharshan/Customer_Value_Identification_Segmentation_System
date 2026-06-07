from sklearn.cluster import KMeans


def segment_customers(df):

    features = df[["cvi"]]

    model = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )

    df["segment"] = model.fit_predict(
        features
    )

    return df