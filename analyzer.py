import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def generate_summary(df):
    total_invoices = len(df)
    total_revenue = df['amount'].sum()
    pending_shipments = df[df['status'] == 'pending'].shape[0]
    top_vendor = df.groupby('vendor')['amount'].sum().idxmax()

    return {
        "total_invoices": total_invoices,
        "total_revenue": total_revenue,
        "pending_shipments": pending_shipments,
        "top_vendor": top_vendor
    }


def vendor_summary(df):
    return df.groupby('vendor')['amount'].sum().reset_index()
