# FluCleave

Deep learning prediction of influenza virus pathogenicity from HA cleavage sites.

## Features

-   Analyzes hemagglutinin (HA) cleavage site sequences
-   Predicts high/low pathogenicity using deep learning
-   Handles both DNA and protein sequences
-   Command-line interface for easy use
-   Trained on curated dataset of known pathogenic sequences

## Installation

```bash
pip install flucleave
```

## Usage

Predict pathogenicity from FASTA file:

```bash
flucleave predict --fasta sequences.fasta --output-dir results/
```

Train new model (optional):

```bash
flucleave train --training-csv data.csv
```

## Data Format

Input FASTA should contain HA protein sequences. Example:

```
>A/chicken/Hong_Kong/220/97
MVNQILIILAAIASAAPGDQICIGYHANNSTEQVDTIMEKNVTVTHAQDI...
```

Or DNA sequences. Example:

```
>A/chicken/Hong_Kong/220/97
ATGGAAGGCAATACTAGTAGTCTTCTTCTTCTTCTTCTTCTTCTTCTTCT...
```

## License

FluCleave is licensed under the [MIT License](LICENSE).
