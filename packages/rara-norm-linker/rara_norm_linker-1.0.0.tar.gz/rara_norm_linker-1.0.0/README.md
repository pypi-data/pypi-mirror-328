# RaRa Linker

![Py3.10](https://img.shields.io/badge/python-3.10-green.svg)
![Py3.11](https://img.shields.io/badge/python-3.11-green.svg)
![Py3.12](https://img.shields.io/badge/python-3.12-green.svg)

**`rara-norm-linker`** is a  Python library for linking **personal names, organizations, geographical names** and **keywords** with taxonomy entries.

**NB!** Requires access to an **Elasticsearch>=8.0** instance.

---

## ✨ Features  

- Link **personal names, organizations, geographical names**, and **keywords** with taxonomy entries.
- Use **fuzzy matching** for linking.
- Use **vector search** for filtering results.
- Use [**VIAF**](https://viaf.org/en) queries for enrichment.
---


## ⚡ Quick Start  

Get started with `rara-norm-linker` in just a few steps:

1. **Install the Package**  
   Ensure you're using Python 3.10 or above, then run:  
   ```bash
   pip install rara-norm-linker
   ```

2. **Import and Use**  
   Example usage to link entries with default configuration:  

   ```python
   from rara_linker.linkers.linker import Linker
   from pprint import pprint
   import logging
   
   # Disables logging, feel free to comment this out
   logging.disable(logging.CRITICAL) 

   # Initialize Linker instance
   linker = Linker(add_viaf_info=True, vectorizer_data_path="./vectorizer_data")
   entity = "Lennart Mere"

   linked_info = linker.link(entity)
   pprint(linked_info.to_dict())
   ```

---



## ⚙️ Installation Guide

Follow the steps below to install the `rara-norm-linker` package, either via `pip` or locally.

---

### Installation via `pip`

<details><summary>Click to expand</summary>

1. **Set Up Your Python Environment**  
   Create or activate a Python environment using Python **3.10** or above.

2. **Install the Package**  
   Run the following command:  
   ```bash
   pip install rara-norm-linker
   ```
</details>

---

### Local Installation

Follow these steps to install the `rara-norm-linker` package locally:  

<details><summary>Click to expand</summary>


1. **Clone the Repository**  
   Clone the repository and navigate into it:  
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up Python Environment**  
   Create or activate a Python environment using Python 3.10 or above. E.g:
   ```bash
   conda create -n py310 python==3.10
   conda activate py310
   ```

3. **Install Build Package**  
   Install the `build` package to enable local builds:  
   ```bash
   pip install build
   ```

4. **Build the Package**  
   Run the following command inside the repository:  
   ```bash
   python -m build
   ```

5. **Install the Package**  
   Install the built package locally:  
   ```bash
   pip install .
   ```

</details>

---

## 🚀 Testing Guide

Follow these steps to test the `rara-norm-linker` package.


### How to Test

<details><summary>Click to expand</summary>

1. **Clone the Repository**  
   Clone the repository and navigate into it:  
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up Python Environment**  
   Create or activate a Python environment using Python 3.10 or above.

3. **Install Build Package**  
   Install the `build` package:  
   ```bash
   pip install build
   ```

4. **Build the Package**  
   Build the package inside the repository:  
   ```bash
   python -m build
   ```

5. **Install with Testing Dependencies**  
   Install the package along with its testing dependencies:  
   ```bash
   pip install .[testing]
   ```

6. **Run Tests**  
   Run the test suite from the repository root:  
   ```bash
   python -m pytest -v tests
   ```

---

</details>


## 📝 Documentation

Documentation can be found [here](DOCUMENTATION.md).


## 🔍 Usage Examples

The following function is used to help formatting output:

<details><summary>Click to expand</summary>

```python
from rara_linker.linkers.linking_result import LinkingResult
from typing import NoReturn

def format_output(linked: LinkingResult) -> NoReturn:
   print(f"Original entity: {linked.original_entity}")
   print(f"Entity type: {linked.entity_type}")
   print(f"Number of matches: {linked.n_linked}")
   print(f"Similarity: {linked.similarity_score}")

   for entity_info in linked.linked_info:
      print()
      print(f"Linked entity: {entity_info.linked_entity}")
      description = entity_info.elastic.get("description", "")
      if description:
         print(f"Description: {description}")
      print()

```
</details>

### Example 1: Simple linking

```python
from rara_linker.linkers.linker import Linker
import logging

logging.disable(logging.CRITICAL) 

linker = Linker(add_viaf_info=True, vectorizer_data_path="./vectorizer_data")

entity = "Damon Albarn"
linked = linker.link(entity)

format_output(linked)
```

**Output:**

```
Original entity: Damon Albarn
Entity type: PER
Number of matches: 1
Similarity: 1.0

Linked entity: Albarn, Damon
Description: Inglise muusik ja laulukirjutaja
```

```python
from pprint import pprint
# Code for displaying the raw output of the same linking result:
pprint(linked.to_dict())
```

<details><summary>Raw output</summary>

```
{'entity_type': 'PER',
 'linked_info': [{'elastic': {'birth_year': 1968,
                              'death_year': None,
                              'description': 'Inglise muusik ja laulukirjutaja',
                              'identifier': 'a12660826',
                              'identifier_source': 'ErRR',
                              'life_year': '1968-',
                              'link_variations': ['albran, damon',
                                                  'damon albran',
                                                  'damon albarn',
                                                  'albarn, damon'],
                              'name': 'Albarn, Damon',
                              'name_in_cyrillic': False,
                              'name_specification': '',
                              'name_variations': ['Albran, Damon'],
                              'source': 'Vikipeedia'},
                  'json': {'fields': [{'001': 'a12660826'},
                                      {'003': 'ErRR'},
                                      {'008': '240418|||aznnnaabn          || '
                                              '|||      '},
                                      {'040': {'ind1': ' ',
                                               'ind2': ' ',
                                               'subfields': [{'a': 'ErRR'},
                                                             {'b': 'est'},
                                                             {'c': 'ErRR'},
                                                             {'e': 'rda'}]}},
                                      {'043': {'ind1': ' ',
                                               'ind2': ' ',
                                               'subfields': [{'c': 'uk'}]}},
                                      {'046': {'ind1': ' ',
                                               'ind2': ' ',
                                               'subfields': [{'f': '1968'}]}},
                                      {'075': {'ind1': ' ',
                                               'ind2': ' ',
                                               'subfields': [{'a': 'persoon'}]}},
                                      {'100': {'ind1': '1',
                                               'ind2': ' ',
                                               'subfields': [{'a': 'Albarn, '
                                                                   'Damon,'},
                                                             {'d': '1968-'}]}},
                                      {'372': {'ind1': ' ',
                                               'ind2': ' ',
                                               'subfields': [{'a': 'rockmuusika'},
                                                             {'a': 'elektronmuusika'},
                                                             {'a': 'hip hop'},
                                                             {'a': 'Britpop.'}]}},
                                      {'374': {'ind1': ' ',
                                               'ind2': ' ',
                                               'subfields': [{'a': 'laulukirjutaja'},
                                                             {'a': 'laulja'},
                                                             {'a': 'muusik.'}]}},
                                      {'400': {'ind1': '1',
                                               'ind2': ' ',
                                               'subfields': [{'a': 'Albran, '
                                                                   'Damon,'},
                                                             {'d': '1968-'}]}},
                                      {'670': {'ind1': ' ',
                                               'ind2': ' ',
                                               'subfields': [{'a': 'Vikipeedia'},
                                                             {'u': 'https://en.wikipedia.org/wiki/Damon_Albarn.'}]}},
                                      {'680': {'ind1': ' ',
                                               'ind2': ' ',
                                               'subfields': [{'i': 'Inglise '
                                                                   'muusik ja '
                                                                   'laulukirjutaja.'}]}}],
                           'leader': '00529nz  a2200181n  4500'},
                  'linked_entity': 'Albarn, Damon',
                  'marc': '=LDR  00529nz  a2200181n  4500\n'
                          '=001  a12660826\n'
                          '=003  ErRR\n'
                          '=008  '
                          '240418|||aznnnaabn\\\\\\\\\\\\\\\\\\\\||\\|||\\\\\\\\\\\\\n'
                          '=040  \\\\$aErRR$best$cErRR$erda\n'
                          '=043  \\\\$cuk\n'
                          '=046  \\\\$f1968\n'
                          '=075  \\\\$apersoon\n'
                          '=100  1\\$aAlbarn, Damon,$d1968-\n'
                          '=372  \\\\$arockmuusika$aelektronmuusika$ahip '
                          'hop$aBritpop.\n'
                          '=374  \\\\$alaulukirjutaja$alaulja$amuusik.\n'
                          '=400  1\\$aAlbran, Damon,$d1968-\n'
                          '=670  '
                          '\\\\$aVikipeedia$uhttps://en.wikipedia.org/wiki/Damon_Albarn.\n'
                          '=680  \\\\$iInglise muusik ja laulukirjutaja.\n',
                  'similarity_score': 1.0,
                  'viaf': {'message': '/api/search Successfully reached!',
                           'queryResult': {'echoedSearchRetrieveRequest': {'maximumRecords': {'type': 'xsd:nonNegativeInteger',
                                                                                              'value': 50},
                                                                           'query': {'type': 'xsd:string',
                                                                                     'value': 'local.personalNames '
                                                                                              'all '
                                                                                              '"a12660826"'},
                                                                           'recordPacking': {'type': 'xsd:string',
                                                                                             'value': 'xml'},
                                                                           'recordSchema': {'type': 'xsd:string',
                                                                                            'value': 'BriefVIAF'},
                                                                           'sortKeys': {'type': 'xsd:string',
                                                                                        'value': 'holdingscount'},
                                                                           'startRecord': {'type': 'xsd:positiveInteger',
                                                                                           'value': 1},
                                                                           'type': 'ns2:echoedSearchRetrieveRequestType',
                                                                           'version': {'type': 'xsd:string',
                                                                                       'value': 1.1},
                                                                           'xQuery': {'searchClause': {'index': {'type': 'xsd:string',
                                                                                                                 'value': 'local.personalNames'},
                                                                                                       'relation': {'type': 'ns3:relationType',
                                                                                                                    'value': [{'value': 'all'}]},
                                                                                                       'term': {'type': 'xsd:string',
                                                                                                                'value': 'a12660826'},
                                                                                                       'type': 'ns3:searchClauseType'}}},
                                           'extraResponseData': {'extraData': {'databaseTitle': 'VIAF: '
                                                                                                'The '
                                                                                                'Virtual '
                                                                                                'International '
                                                                                                'Authority '
                                                                                                'File'},
                                                                 'type': 'ns4:extraDataType'},
                                           'numberOfRecords': {'type': 'xsd:nonNegativeInteger',
                                                               'value': 1},
                                           'records': {'record': [{'recordData': {'VIAFCluster': {'mainHeadings': {'data': [{'sources': {'s': ['DNB',
                                                                                                                                               'KRNLK',
                                                                                                                                               'PLWABN',
                                                                                                                                               'LIH',
                                                                                                                                               'BNF',
                                                                                                                                               'BNE',
                                                                                                                                               'NKC',
                                                                                                                                               'BIBSYS',
                                                                                                                                               'NUKAT',
                                                                                                                                               'ERRR',
                                                                                                                                               'SUDOC'],
                                                                                                                                         'sid': ['DNB|135275245',
                                                                                                                                                 'KRNLK|KAC2020M4718',
                                                                                                                                                 'PLWABN|9810618563005606',
                                                                                                                                                 'LIH|LNB:B2HO;=_u_Y',
                                                                                                                                                 'BNF|14025704',
                                                                                                                                                 'BNE|XX1502205',
                                                                                                                                                 'NKC|xx0042289',
                                                                                                                                                 'BIBSYS|6096767',
                                                                                                                                                 'NUKAT|n '
                                                                                                                                                 '2009143303',
                                                                                                                                                 'ERRR|a12660826',
                                                                                                                                                 'SUDOC|168995603']},
                                                                                                                             'text': 'Albarn, '
                                                                                                                                     'Damon, '
                                                                                                                                     '1968-....'},
                                                                                                                            {'sources': {'s': ['NLA',
                                                                                                                                               'ISNI',
                                                                                                                                               'LC',
                                                                                                                                               'SIMACOB',
                                                                                                                                               'RERO',
                                                                                                                                               'NSK',
                                                                                                                                               'DBC',
                                                                                                                                               'J9U'],
                                                                                                                                         'sid': ['NLA|000041317329',
                                                                                                                                                 'ISNI|0000000108754251',
                                                                                                                                                 'LC|n  '
                                                                                                                                                 '97085620',
                                                                                                                                                 'SIMACOB|213734755',
                                                                                                                                                 'RERO|A002915097',
                                                                                                                                                 'NSK|000760001',
                                                                                                                                                 'DBC|87097969360297',
                                                                                                                                                 'J9U|987011827765305171']},
                                                                                                                             'text': 'Albarn, '
                                                                                                                                     'Damon'},
                                                                                                                            {'sources': {'s': ['WKP'],
                                                                                                                                         'sid': ['WKP|Q272069']},
                                                                                                                             'text': 'Damon '
                                                                                                                                     'Albarn '
                                                                                                                                     'English '
                                                                                                                                     'musician, '
                                                                                                                                     'singer-songwriter, '
                                                                                                                                     'and '
                                                                                                                                     'record '
                                                                                                                                     'producer'}]},
                                                                                                  'nameType': 'Personal',
                                                                                                  'titles': {'work': [{'sources': {'s': ['DNB',
                                                                                                                                         'WKP',
                                                                                                                                         'RERO',
                                                                                                                                         'SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['DNB|135275245',
                                                                                                                                           'WKP|Q272069',
                                                                                                                                           'RERO|A002915097',
                                                                                                                                           'SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': '101 '
                                                                                                                                'Reykjav&#xED;k'},
                                                                                                                      {'sources': {'s': ['NUKAT'],
                                                                                                                                   'sid': ['NUKAT|n '
                                                                                                                                           '2009143303']},
                                                                                                                       'title': 'Anna '
                                                                                                                                'and '
                                                                                                                                'the '
                                                                                                                                'moods'},
                                                                                                                      {'sources': {'s': ['BIBSYS'],
                                                                                                                                   'sid': ['BIBSYS|6096767']},
                                                                                                                       'title': 'Anna '
                                                                                                                                'g&#xE5;r '
                                                                                                                                'i '
                                                                                                                                'svart'},
                                                                                                                      {'sources': {'s': ['NUKAT'],
                                                                                                                                   'sid': ['NUKAT|n '
                                                                                                                                           '2009143303']},
                                                                                                                       'title': 'Anna '
                                                                                                                                'i '
                                                                                                                                'humorki'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Apple '
                                                                                                                                'carts '
                                                                                                                                '(2 '
                                                                                                                                'min '
                                                                                                                                '36 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['DBC'],
                                                                                                                                   'sid': ['DBC|87097969360297']},
                                                                                                                       'title': 'Arbejdsnarkoman '
                                                                                                                                'uden '
                                                                                                                                'en '
                                                                                                                                'plan'},
                                                                                                                      {'sources': {'s': ['DNB'],
                                                                                                                                   'sid': ['DNB|135275245']},
                                                                                                                       'title': 'ballad '
                                                                                                                                'of '
                                                                                                                                'Darren'},
                                                                                                                      {'sources': {'s': ['DBC',
                                                                                                                                         'SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['DBC|87097969360297',
                                                                                                                                           'SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Bananaz'},
                                                                                                                      {'sources': {'s': ['RERO'],
                                                                                                                                   'sid': ['RERO|A002915097']},
                                                                                                                       'title': 'Broken'},
                                                                                                                      {'sources': {'s': ['SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Call '
                                                                                                                                'me '
                                                                                                                                'up'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Cathedrals '
                                                                                                                                '(3 '
                                                                                                                                'min)'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Coffee '
                                                                                                                                '& '
                                                                                                                                'TV'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'com&#xE9;die'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Coronation '
                                                                                                                                '(1 '
                                                                                                                                'min '
                                                                                                                                '10 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['SIMACOB'],
                                                                                                                                   'sid': ['SIMACOB|213734755']},
                                                                                                                       'title': 'Cracker '
                                                                                                                                'Island'},
                                                                                                                      {'sources': {'s': ['SUDOC'],
                                                                                                                                   'sid': ['SUDOC|168995603']},
                                                                                                                       'title': 'Damon '
                                                                                                                                'Albarn '
                                                                                                                                ': '
                                                                                                                                'Blur, '
                                                                                                                                'Gorillaz '
                                                                                                                                'and '
                                                                                                                                'other '
                                                                                                                                'fables'},
                                                                                                                      {'sources': {'s': ['PLWABN'],
                                                                                                                                   'sid': ['PLWABN|9810618563005606']},
                                                                                                                       'title': 'Damoniczny '
                                                                                                                                '&#x15B;wiat'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'dancing '
                                                                                                                                'king '
                                                                                                                                '(3 '
                                                                                                                                'min '
                                                                                                                                '21 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Dare'},
                                                                                                                      {'sources': {'s': ['SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Democrazy'},
                                                                                                                      {'sources': {'s': ['LC',
                                                                                                                                         'DNB'],
                                                                                                                                   'sid': ['LC|n  '
                                                                                                                                           '97085620',
                                                                                                                                           'DNB|135275245']},
                                                                                                                       'title': 'Doctor '
                                                                                                                                'Dee'},
                                                                                                                      {'id': 'VIAF|7806173669165707660003',
                                                                                                                       'sources': {'s': ['DNB',
                                                                                                                                         'RERO',
                                                                                                                                         'SUDOC',
                                                                                                                                         'BNF',
                                                                                                                                         'LC',
                                                                                                                                         'NYNYRILM'],
                                                                                                                                   'sid': ['DNB|135275245',
                                                                                                                                           'RERO|A002915097',
                                                                                                                                           'SUDOC|168995603',
                                                                                                                                           'BNF|14025704',
                                                                                                                                           'LC|n  '
                                                                                                                                           '97085620',
                                                                                                                                           'NYNYRILM|95370']},
                                                                                                                       'title': 'Dr '
                                                                                                                                'Dee: '
                                                                                                                                'An '
                                                                                                                                'English '
                                                                                                                                'opera'},
                                                                                                                      {'sources': {'s': ['PLWABN'],
                                                                                                                                   'sid': ['PLWABN|9810618563005606']},
                                                                                                                       'title': 'Drapie&#x17C;cy'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Dude, '
                                                                                                                                'Where&#x2019;s '
                                                                                                                                'My '
                                                                                                                                'Car?'},
                                                                                                                      {'sources': {'s': ['ERRR'],
                                                                                                                                   'sid': ['ERRR|a12660826']},
                                                                                                                       'title': 'Euro '
                                                                                                                                'dance '
                                                                                                                                '1999'},
                                                                                                                      {'sources': {'s': ['DNB',
                                                                                                                                         'SIMACOB',
                                                                                                                                         'RERO',
                                                                                                                                         'SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['DNB|135275245',
                                                                                                                                           'SIMACOB|213734755',
                                                                                                                                           'RERO|A002915097',
                                                                                                                                           'SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Everyday '
                                                                                                                                'robots'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Fatti, '
                                                                                                                                'strafatti '
                                                                                                                                'e '
                                                                                                                                'strafighe'},
                                                                                                                      {'sources': {'s': ['LC',
                                                                                                                                         'SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['LC|n  '
                                                                                                                                           '97085620',
                                                                                                                                           'SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Film '
                                                                                                                                'of '
                                                                                                                                'life'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Girls '
                                                                                                                                '& '
                                                                                                                                'Boys'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Give '
                                                                                                                                'it '
                                                                                                                                'to '
                                                                                                                                'the '
                                                                                                                                'people'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Give '
                                                                                                                                'me'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'golden '
                                                                                                                                'dawn'},
                                                                                                                      {'sources': {'s': ['SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'good, '
                                                                                                                                'the '
                                                                                                                                'bad '
                                                                                                                                '&the '
                                                                                                                                'queen '
                                                                                                                                'Herculean'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Heavy '
                                                                                                                                'seas '
                                                                                                                                'of '
                                                                                                                                'love '
                                                                                                                                '(3 '
                                                                                                                                'min '
                                                                                                                                '44 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'history '
                                                                                                                                'of '
                                                                                                                                'a '
                                                                                                                                'cheating '
                                                                                                                                'heart '
                                                                                                                                '(4 '
                                                                                                                                'min)'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Hollow '
                                                                                                                                'ponds '
                                                                                                                                '(4 '
                                                                                                                                'min '
                                                                                                                                '59 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Honest '
                                                                                                                                'Jons '
                                                                                                                                'sampler'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Hostiles '
                                                                                                                                '(4 '
                                                                                                                                'min '
                                                                                                                                '09 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['LC'],
                                                                                                                                   'sid': ['LC|n  '
                                                                                                                                           '97085620']},
                                                                                                                       'title': 'The '
                                                                                                                                'isle '
                                                                                                                                'of '
                                                                                                                                'view'},
                                                                                                                      {'sources': {'s': ['SIMACOB'],
                                                                                                                                   'sid': ['SIMACOB|213734755']},
                                                                                                                       'title': 'Live '
                                                                                                                                'forever  '
                                                                                                                                'the '
                                                                                                                                'rise '
                                                                                                                                'and '
                                                                                                                                'fall '
                                                                                                                                'of '
                                                                                                                                'Brit '
                                                                                                                                'pop'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Lonely '
                                                                                                                                'press '
                                                                                                                                'play '
                                                                                                                                '(3 '
                                                                                                                                'min '
                                                                                                                                '42 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['DNB',
                                                                                                                                         'RERO',
                                                                                                                                         'SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['DNB|135275245',
                                                                                                                                           'RERO|A002915097',
                                                                                                                                           'SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Mali '
                                                                                                                                'music'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'man '
                                                                                                                                'of '
                                                                                                                                'England '
                                                                                                                                '(3 '
                                                                                                                                'min '
                                                                                                                                '17 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'marvelous '
                                                                                                                                'dream'},
                                                                                                                      {'sources': {'s': ['BIBSYS'],
                                                                                                                                   'sid': ['BIBSYS|6096767']},
                                                                                                                       'title': 'Me '
                                                                                                                                'and '
                                                                                                                                'the '
                                                                                                                                'devil'},
                                                                                                                      {'sources': {'s': ['DNB'],
                                                                                                                                   'sid': ['DNB|135275245']},
                                                                                                                       'title': 'Merrie '
                                                                                                                                'land'},
                                                                                                                      {'id': 'VIAF|210959931',
                                                                                                                       'sources': {'s': ['LC',
                                                                                                                                         'DNB',
                                                                                                                                         'WKP'],
                                                                                                                                   'sid': ['LC|n  '
                                                                                                                                           '97085620',
                                                                                                                                           'DNB|135275245',
                                                                                                                                           'WKP|Q272069',
                                                                                                                                           'DNB|300912528']},
                                                                                                                       'title': 'Monkey'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Moon'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Mr '
                                                                                                                                'Tembo '
                                                                                                                                '(3 '
                                                                                                                                'min '
                                                                                                                                '43 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['DBC'],
                                                                                                                                   'sid': ['DBC|87097969360297']},
                                                                                                                       'title': 'No '
                                                                                                                                'distance '
                                                                                                                                'left '
                                                                                                                                'to '
                                                                                                                                'run'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'One '
                                                                                                                                'day'},
                                                                                                                      {'sources': {'s': ['BNE',
                                                                                                                                         'WKP',
                                                                                                                                         'NUKAT',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['BNE|XX1502205',
                                                                                                                                           'WKP|Q272069',
                                                                                                                                           'NUKAT|n '
                                                                                                                                           '2009143303',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Ordinary '
                                                                                                                                'Decent '
                                                                                                                                'Criminal'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Parakeet '
                                                                                                                                '(43 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Parklife '
                                                                                                                                '(canci&#xF3;n)'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Perdu'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Un '
                                                                                                                                'perfetto '
                                                                                                                                'criminale'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Photographs'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Point '
                                                                                                                                'star'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Preparation'},
                                                                                                                      {'sources': {'s': ['WKP',
                                                                                                                                         'NUKAT'],
                                                                                                                                   'sid': ['WKP|Q272069',
                                                                                                                                           'NUKAT|n '
                                                                                                                                           '2009143303']},
                                                                                                                       'title': 'Przyzwoity '
                                                                                                                                'przest&#x119;pca'},
                                                                                                                      {'sources': {'s': ['PLWABN',
                                                                                                                                         'BNE',
                                                                                                                                         'SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['PLWABN|9810618563005606',
                                                                                                                                           'BNE|XX1502205',
                                                                                                                                           'SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Ravenous'},
                                                                                                                      {'sources': {'s': ['BNE'],
                                                                                                                                   'sid': ['BNE|XX1502205']},
                                                                                                                       'title': 'Scott '
                                                                                                                                'Walker, '
                                                                                                                                '30 '
                                                                                                                                'Century '
                                                                                                                                'Man'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'selfish '
                                                                                                                                'giant '
                                                                                                                                '(4 '
                                                                                                                                'min '
                                                                                                                                '47 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Seven '
                                                                                                                                'high '
                                                                                                                                '(1 '
                                                                                                                                'min)'},
                                                                                                                      {'id': 'VIAF|7146522416032391727',
                                                                                                                       'sources': {'s': ['DNB',
                                                                                                                                         'SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['DNB|135275245',
                                                                                                                                           'DNB|1102560960',
                                                                                                                                           'SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Songs '
                                                                                                                                'from '
                                                                                                                                'Wonder.land'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Stary, '
                                                                                                                                'gdzie '
                                                                                                                                'moja '
                                                                                                                                'bryka?'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Swim '
                                                                                                                                'The '
                                                                                                                                'Channel'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Tavaline '
                                                                                                                                'kurjategija'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Tavallisen '
                                                                                                                                'rehti '
                                                                                                                                'rikollinen'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Temptation '
                                                                                                                                'comes '
                                                                                                                                'in '
                                                                                                                                'the '
                                                                                                                                'afternoon '
                                                                                                                                '(2 '
                                                                                                                                'min '
                                                                                                                                '05 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'To '
                                                                                                                                'the '
                                                                                                                                'end'},
                                                                                                                      {'sources': {'s': ['NLA',
                                                                                                                                         'PLWABN',
                                                                                                                                         'WKP',
                                                                                                                                         'BNE',
                                                                                                                                         'LC',
                                                                                                                                         'BNF',
                                                                                                                                         'RERO',
                                                                                                                                         'SUDOC'],
                                                                                                                                   'sid': ['NLA|000041317329',
                                                                                                                                           'PLWABN|9810618563005606',
                                                                                                                                           'WKP|Q272069',
                                                                                                                                           'BNE|XX1502205',
                                                                                                                                           'LC|n  '
                                                                                                                                           '97085620',
                                                                                                                                           'BNF|14025704',
                                                                                                                                           'RERO|A002915097',
                                                                                                                                           'SUDOC|168995603']},
                                                                                                                       'title': 'Trainspotting'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': 'Traukini&#x173; '
                                                                                                                                '&#x17E;ym&#x117;jimas'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Tree '
                                                                                                                                'of '
                                                                                                                                'beauty '
                                                                                                                                '(2 '
                                                                                                                                'min)'},
                                                                                                                      {'sources': {'s': ['PLWABN'],
                                                                                                                                   'sid': ['PLWABN|9810618563005606']},
                                                                                                                       'title': 'Twarz'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Twentieth '
                                                                                                                                'century '
                                                                                                                                'blues '
                                                                                                                                'the '
                                                                                                                                'songs '
                                                                                                                                'of '
                                                                                                                                'No&#xEB;l '
                                                                                                                                'Coward'},
                                                                                                                      {'sources': {'s': ['RERO',
                                                                                                                                         'SUDOC',
                                                                                                                                         'BNF'],
                                                                                                                                   'sid': ['RERO|A002915097',
                                                                                                                                           'SUDOC|168995603',
                                                                                                                                           'BNF|14025704']},
                                                                                                                       'title': 'Vorace'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Warrior'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'Watching '
                                                                                                                                'the '
                                                                                                                                'fire '
                                                                                                                                'that '
                                                                                                                                'waltzed '
                                                                                                                                'away '
                                                                                                                                '(2 '
                                                                                                                                'min '
                                                                                                                                '37 '
                                                                                                                                's)'},
                                                                                                                      {'id': 'VIAF|22146522418032391851',
                                                                                                                       'sources': {'s': ['DNB'],
                                                                                                                                   'sid': ['DNB|1102560677']},
                                                                                                                       'title': 'Wonder.land'},
                                                                                                                      {'sources': {'s': ['BNF'],
                                                                                                                                   'sid': ['BNF|14025704']},
                                                                                                                       'title': 'You '
                                                                                                                                '& '
                                                                                                                                'me '
                                                                                                                                '(7 '
                                                                                                                                'min '
                                                                                                                                '05 '
                                                                                                                                's)'},
                                                                                                                      {'sources': {'s': ['NSK'],
                                                                                                                                   'sid': ['NSK|000760001']},
                                                                                                                       'title': '&#x17D;ivio '
                                                                                                                                'album!'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#x414;&#x435; '
                                                                                                                                '&#x43C;&#x43E;&#x44F; '
                                                                                                                                '&#x442;&#x430;&#x447;&#x43A;&#x430;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#x41E;&#x431;&#x44B;&#x43A;&#x43D;&#x43E;&#x432;&#x435;&#x43D;&#x43D;&#x44B;&#x439; '
                                                                                                                                '&#x43F;&#x440;&#x435;&#x441;&#x442;&#x443;&#x43F;&#x43D;&#x438;&#x43A;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#x422;&#x440;&#x435;&#x439;&#x43D;&#x441;&#x43F;&#x43E;&#x442;&#x438;&#x43D;&#x433;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#x5D4;&#x5D0;&#x5E8;&#x5D9; '
                                                                                                                                '&#x5D4;&#x5DE;&#x5D6;&#x5D5;&#x5D4;&#x5DD;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#x645;&#x62C;&#x631;&#x645; '
                                                                                                                                '&#x646;&#x62C;&#x6CC;&#x628; '
                                                                                                                                '&#x639;&#x627;&#x62F;&#x6CC;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#x99F;&#x9CD;&#x9B0;&#x9C7;&#x9A8;&#x9B8;&#x9CD;&#x9AA;&#x99F;&#x9BF;&#x982;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#xE0B;&#xE2D;&#xE07;&#xE17;&#xE39;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#xB0B4; '
                                                                                                                                '&#xCC28; '
                                                                                                                                '&#xBD24;&#xB0D0;?'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#xD2B8;&#xB808;&#xC778;&#xC2A4;&#xD3EC;&#xD305;'},
                                                                                                                      {'sources': {'s': ['KRNLK'],
                                                                                                                                   'sid': ['KRNLK|KAC2020M4718']},
                                                                                                                       'title': '&#xD398;&#xC774;&#xC2A4;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#x79C1;&#x304C;&#x611B;&#x3057;&#x305F;&#x30AE;&#x30E3;&#x30F3;&#x30B0;&#x30B9;&#x30BF;&#x30FC;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#x731C;&#x706B;&#x8ECA;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#x8C6C;&#x982D;&#xFF0C;&#x6211;&#x7684;&#x8ECA;&#x54A7;&#xFF1F;'},
                                                                                                                      {'sources': {'s': ['WKP'],
                                                                                                                                   'sid': ['WKP|Q272069']},
                                                                                                                       'title': '&#x738B;&#x724C;&#x7F6A;&#x72AF;'}]},
                                                                                                  'viafID': 17421456},
                                                                                  'type': 'ns1:stringOrXmlFragment'},
                                                                   'recordPacking': {'type': 'xsd:string',
                                                                                     'value': 'xml'},
                                                                   'recordPosition': {'type': 'xsd:positiveInteger',
                                                                                      'value': 1},
                                                                   'recordSchema': {'type': 'xsd:string',
                                                                                    'value': 'http://viaf.org/BriefVIAFCluster'},
                                                                   'type': 'ns1:recordType'}],
                                                       'type': 'ns1:recordsType'},
                                           'resultSetIdleTime': {'type': 'xsd:positiveInteger',
                                                                 'value': 1},
                                           'schemaLocation': 'http://www.loc.gov/zing/srw/ '
                                                             'http://www.loc.gov/standards/sru/sru1-1archive/xml-files/srw-types.xsd',
                                           'version': {'type': 'xsd:string',
                                                       'value': 1.1}}}}],
 'linking_config': {'add_viaf_info': True,
                    'context': None,
                    'entity': 'Damon Albarn',
                    'fuzziness': 0,
                    'min_similarity': 0.9,
                    'prefix_length': 1},
 'n_linked': 1,
 'original_entity': 'Damon Albarn',
 'similarity_score': 1.0}

```
</details>

### Example 2: Multiple matches are returned

```python
from rara_linker.linkers.linker import Linker
import logging

logging.disable(logging.CRITICAL) 

linker = Linker(add_viaf_info=True, vectorizer_data_path="./vectorizer_data")

# The input contains some typos, 
# we are actually trying to find
# Paul Keres, the chess grandmaster
entity = "Paul Keers"
linked = linker.link(entity)

format_output(linked)
```

**Output:**

```
Original entity: Paul Keers
Entity type: PER
Number of matches: 3
Similarity: 0.98

Linked entity: Kees, Paul
Description: Eesti pedagoogikateadlane ja tõlkija

Linked entity: Keres, Paul
Description: Eesti maletaja ja maleteoreetik

Linked entity: Keres, Paul
Description: Eesti advokaat
```

### Example 3: Using vector search for additional filtering

```python
from rara_linker.linkers.linker import Linker
import logging

logging.disable(logging.CRITICAL) 

linker = Linker(add_viaf_info=True, vectorizer_data_path="./vectorizer_data")

# The input contains some typos, 
# we are actually trying to find
# Paul Keres, the chess grandmaster
entity = "Paul Keers"

# The context can be any short text that
# might bare some contextual resemblance to 
# the entity. In practice, it will most likely
# be a title or a short paragraph,
# where the name was mentioned, let's try
# something similar:
context = "Viljandis selgusid 56. maleturniiri võitjad"
linked = linker.link(entity, context=context)

format_output(linked)
```

**Output:**

```
Original entity: Paul Keers
Entity type: PER
Number of matches: 1
Similarity: 0.98

Linked entity: Keres, Paul
Description: Eesti maletaja ja maleteoreetik
```

### Example 4: Link a keyword / subject index

```python
from rara_linker.linkers.linker import Linker
import logging

logging.disable(logging.CRITICAL) 

linker = Linker(add_viaf_info=True, vectorizer_data_path="./vectorizer_data")

entity = "alajahtumine"
linked = linker.link(entity)

format_output(linked)
```

**Output:**

```
Original entity: alajahtumine
Entity type: EMS_KEYWORD
Number of matches: 1
Similarity: 1.0

Linked entity: hüpotermia
```
More examples can be found from [Documentation](DOCUMENTATION.md).