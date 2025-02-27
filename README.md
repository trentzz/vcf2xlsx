# vcf2xlsx

A lightweight cli wrapper for [vcf2pandas](https://github.com/trentzz/vcf2pandas) that converts a Variant Call Format (VCF) file to an excel spreadsheet.

For more information about the format of the excel spreadsheet, naming, or otherwise, see [vcf2pandas](https://github.com/trentzz/vcf2pandas) for more details.

## Install

```bash
pipx install vcf2xlsx
```

## Usage

```bash
vcf2xlsx <vcf-file> --output <xlsx-file>
```

## Examples

```bash
cd vcf2xlsx
poetry run vcf2xlsx examples/example.vcf -o examples/example.xlsx
```
