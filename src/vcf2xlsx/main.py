import argparse

from vcf2pandas import vcf2pandas


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.description = "Convert a VCF file to an XLSX file."
    parser.add_argument("vcf", help="Path to the VCF file.")
    parser.add_argument("-o", "--output", help="Path to the XLSX file.")
    parser.add_argument(
        "-r", "--remove-empty-columns", action="store_true", help="Remove empty columns."
    )
    args = parser.parse_args()

    df = vcf2pandas(args.vcf, remove_empty_columns=args.remove_empty_columns)
    if args.output is None:
        args.output = args.vcf.replace(".vcf", ".xlsx")

    df.to_excel(args.output, index=False)
