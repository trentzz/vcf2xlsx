# vcf2xlsx

[![PyPI Downloads](https://static.pepy.tech/badge/vcf2xlsx)](https://pepy.tech/projects/vcf2xlsx)

A lightweight cli wrapper for [vcf2pandas](https://github.com/trentzz/vcf2pandas) that converts a Variant Call Format (VCF) file to an excel spreadsheet.

For more information about the format of the excel spreadsheet, naming, or otherwise, see [vcf2pandas](https://github.com/trentzz/vcf2pandas).

## Install

```bash
pipx install vcf2xlsx
```

## Usage

```bash
vcf2xlsx <vcf-filename>.vcf
```

Outputs `<vcf-filename>.xlsx` by default.

```bash
  -o OUTPUT, --output OUTPUT
                        Path to the XLSX file.
  -r, --remove-empty-columns
                        Remove empty columns.
```

## Examples

```bash
vcf2xlsx examples/example.vcf -o examples/example.xlsx
```
