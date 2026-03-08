# Wikidata Tools

A collection of notebooks for building, enriching, and maintaining scholarly records in [Wikidata](https://www.wikidata.org/). Originally developed for anthropology journals, but applicable to any discipline.

## What's Here

### Query & Coverage

| Notebook | Colab | Description |
|----------|:-----:|-------------|
| [Wikidata Anthropologist List](notebooks/Wikidata_Anthropologist_List.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_Anthropologist_List.ipynb) | Query all anthropologists in Wikidata with metadata (birth/death, gender, citizenship, ORCID). |
| [Wikidata Journal Article Counter](notebooks/Wikidata_Journal_Article_Counter.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_Journal_Article_Counter.ipynb) | Count scholarly articles per journal on the Wikidata scholarly endpoint. Built-in AAA journal list or custom CSV input. |
| [Wikidata Anthropology Main Subject Counter](notebooks/Wikidata_Anthropology_Main_Subject_Counter.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_Anthropology_Main_Subject_Counter.ipynb) | Count articles tagged with "anthropology" (P921=Q23404) per journal. Identifies journals lacking subject tags. |
| [Wikidata Prominent Anthropologists](notebooks/Wikidata_Prominent_Anthropologists.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_Prominent_Anthropologists.ipynb) | Rank ~13K anthropologists by composite prominence score (sitelinks, doctoral students, links, awards, authored works). |

### Import & Verification

| Notebook | Colab | Description |
|----------|:-----:|-------------|
| [Wikidata Article Importer](notebooks/Wikidata_Article_Importer.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_Article_Importer.ipynb) | Transform bibliographic CSV data into QuickStatements for batch importing scholarly articles. Checks for existing DOIs via the scholarly endpoint. |
| [Post-Import Verification and Repair](notebooks/Post_Import_Verification_and_Repair.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Post_Import_Verification_and_Repair.ipynb) | Verify QuickStatements imports against source CSV. Identify missing articles and incomplete records, generate targeted repair statements. |

### Duplicate Detection & Cleanup

| Notebook | Colab | Description |
|----------|:-----:|-------------|
| [Wikidata Duplicate Detector](notebooks/Wikidata_Duplicate_Detector.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_Duplicate_Detector.ipynb) | Detect duplicate scholarly articles by DOI matching and normalized title comparison. Journal-scoped with inspection tools. |
| [Wikidata Non-Article Cleanup](notebooks/Wikidata_NonArticle_Cleanup.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_NonArticle_Cleanup.ipynb) | Identify non-articles in CrossRef CSV exports, look up their Wikidata QIDs, and generate deletion commands. |

### Author Enrichment & Reconciliation

| Notebook | Colab | Description |
|----------|:-----:|-------------|
| [Wikidata Author Name String Enrichment](notebooks/Wikidata_Author_Name_String_Enrichment.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_Author_Name_String_Enrichment.ipynb) | Add qualifiers (series ordinal, affiliation) and CrossRef references to existing P2093 author name string statements. |
| [Wikidata ORCID Author Reconciliation](notebooks/Wikidata_ORCID_Author_Reconciliation.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_ORCID_Author_Reconciliation.ipynb) | Match P2093 author name strings to P50 person items using ORCID. Generate QuickStatements to add P50 and remove P2093. |

### Metadata Enrichment

| Notebook | Colab | Description |
|----------|:-----:|-------------|
| [Wikidata Citation Enrichment](notebooks/Wikidata_Citation_Enrichment.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_Citation_Enrichment.ipynb) | Enrich articles with P2860 (cites work) statements using Semantic Scholar API. Batch processing with checkpoint/resume. |
| [Wikidata Article Identifier Enrichment](notebooks/Wikidata_Article_Identifier_Enrichment.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_Article_Identifier_Enrichment.ipynb) | Add external identifiers (OpenAlex, Semantic Scholar, Fatcat, PubMed) to scholarly articles. No API keys required. |

### ORCID & Person Data

| Notebook | Colab | Description |
|----------|:-----:|-------------|
| [ORCID Author Data Query](notebooks/ORCID_Author_Data_Query.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/ORCID_Author_Data_Query.ipynb) | Query the ORCID Public API for comprehensive author data (names, affiliations, education, employment, external IDs). |
| [ORCID Works Query](notebooks/ORCID_Works_Query.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/ORCID_Works_Query.ipynb) | Retrieve complete publications from ORCID profiles, including non-CrossRef sources. Multiple identifier support. |
| [CrossRef Author Works Query](notebooks/CrossRef_Author_Works_Query.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/CrossRef_Author_Works_Query.ipynb) | Query CrossRef API for all works by an author via ORCID or DOI list. Full metadata extraction. |
| [ORCID Anthropologist Discovery](notebooks/ORCID_Anthropologist_Discovery.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/ORCID_Anthropologist_Discovery.ipynb) | Search ORCID to identify anthropologists using multi-signal detection (education, employment, keywords, works). Confidence scoring. |
| [Wikidata ORCID Person Backfill](notebooks/Wikidata_ORCID_Person_Backfill.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_ORCID_Person_Backfill.ipynb) | Enrich existing Wikidata person items with ORCID data. Gap analysis and QuickStatements generation for missing identifiers, education, and employment. |
| [Wikidata Person Identifier Discovery](notebooks/Wikidata_Person_Identifier_Discovery.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MattArtzAnthro/wikidata-tools/blob/main/notebooks/Wikidata_Person_Identifier_Discovery.ipynb) | Discover missing external identifiers across 40+ platforms and national library authority systems. |

## Getting Started

These notebooks are designed for [Google Colab](https://colab.research.google.com/) — no local setup required. Click the **Open in Colab** badge next to any notebook to launch it directly.

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
