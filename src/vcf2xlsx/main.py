import argparse

from vcf2pandas import vcf2pandas


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("vcf", help="Path to the VCF file")
    parser.add_argument("-o", "--output", help="Path to the XLSX file")
    args = parser.parse_args()

    df = vcf2pandas(args.vcf)
    df.to_excel(args.output, index=False)
