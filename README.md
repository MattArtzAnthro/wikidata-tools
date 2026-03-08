# Wikidata Tools

A collection of notebooks for building, enriching, and maintaining scholarly records in [Wikidata](https://www.wikidata.org/). Originally developed for anthropology journals, but applicable to any discipline.

## What's Here

| Notebook | Description |
|----------|-------------|
| [Wikidata Anthropologist List](Wikidata_Anthropologist_List.ipynb) | Query all anthropologists in Wikidata with metadata (birth/death, gender, citizenship, ORCID). |

*More notebooks coming soon — article importing, author reconciliation, citation enrichment, identifier discovery, and more.*

## Getting Started

These notebooks are designed for [Google Colab](https://colab.research.google.com/) — no local setup required. Click a notebook above, then open it in Colab.

Each notebook installs its own dependencies and includes configuration, documentation, and export functionality.

## Key Concepts

- **Scholarly endpoint**: Since May 2025, Wikidata splits queries — articles live on `query-scholarly.wikidata.org`, while people and organizations remain on `query.wikidata.org`. Each notebook documents which endpoint it uses.
- **QuickStatements**: Notebooks that modify Wikidata generate [QuickStatements](https://quickstatements.toolforge.org/) commands for batch upload, rather than editing directly.
- **CSV as interchange**: Every notebook exports timestamped CSVs, so you always have a record of what was queried or generated.

## Author

[Matt Artz](https://www.mattartz.me/) | [GitHub](https://github.com/MattArtzAnthro) | [ORCID](https://orcid.org/0000-0002-3822-1429)

## Citation

> Artz, M. (2026). Wikidata Tools. GitHub. https://github.com/MattArtzAnthro/wikidata-tools

*A citable DOI will be available via Zenodo.*

## License

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
