import argparse
from analyzer import load_data, generate_summary, vendor_summary
from utils import plot_vendor_chart, export_to_excel
import os


def main():
    parser = argparse.ArgumentParser(description="Import Export Analyzer")
    parser.add_argument("--file", required=True, help="Path to CSV file")

    args = parser.parse_args()

    os.makedirs("output", exist_ok=True)

    df = load_data(args.file)

    summary = generate_summary(df)
    vendor_df = vendor_summary(df)

    print("\n📊 Summary Report")
    for k, v in summary.items():
        print(f"{k}: {v}")

    plot_vendor_chart(vendor_df)
    export_to_excel(summary, vendor_df)

    print("\n✅ Report Generated in 'output/' folder")


if __name__ == "__main__":
    main()
