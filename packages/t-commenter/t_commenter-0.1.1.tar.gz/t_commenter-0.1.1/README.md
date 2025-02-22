<a id="readme-top"></a>

<!-- PROJECT SHIELDS --> 
> # <p align="center">**T-COMMENTER**</p>

<div align="center">

![Version][PyPI Version]
![Downloads][PyPI Downloads]
![Versions][Python Versions]
![License][PyPI License]
![Issues][PyPI Created]

[![Stargazers][GitHub Stars]][stars-url]
[![Forks][GitHub Forks]][forks-url]
[![Contributors][GitHub Contributors]][contributors-url]
[![Issues][GitHub Issues]][issues-url]
[![Discussions][GitHub Discussions]][discussions-url]

</div>


<div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/ArtemXYZ/t-commenter/main/docs/images/t-commenter.png" 
    style="width: 900px; height: 300px;" alt="LOGO">
</div> 

## About the project

    The T-COMMENTER library is based on the SQLAlchemy library and is designed to 
    create comments on tables (and other objects) in a database (in the current 
    version of the library, it is only for PostgreSQL) T-COMMENTER - this is a 
    modified abbreviation от "Table Commentator". In this context, the meaning of 
    the word table has a broader meaning than the direct one, and covers objects 
    such as a view, materialized view (other types of objects are ignored in the 
    current implementation). 

    Initially, the library was conceived as a tool for working with metadata in 
    DAGs (DAG - Directed Acyclic Graph, 
    https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html) 
    "Apache Airflow". The need to rewrite the metadata of database objects arises 
    when working with pandas, namely with "pandas.Data Frame.to_sql"
    (
        https://pandas.pydata.org/pandas-docs/stable/reference/api/
        pandas.DataFrame.to_sql.html
    ). 
    If the method has a the if_exists=replace flag, drops the table 
    before inserting new values. In this case, all metadata is they are deleted 
    along with the table. This library was created to solve this kind of problem, 
    as well as to to ensure the convenience of working without using SQL directly.

## Installation

You can install the library using pip:

```sh
   pip install t-commentor
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

#### <p align="center">Creating an instance Сommenter</p>

```python
from tcommenter import Сommenter
from connections import engine  # Your SQLAlchemy Engine:

# Creating an instance of a class to work with a specific entity in the database:
commenter = Сommenter(engine=engine, name_table='dags', schema='audit')
```

[//]: # (- Metadata extraction methods:)

#### <p align="center">Metadata extraction methods</p>

```python

# Getting a comment to the table (only to the entity itself, excluding comments to columns):
comments = commenter.get_table_comments()
print(comments)  # -> 'The table contains data unloading from Airflow.'

```

```python

# Getting comments on all columns of an entity:
comments = commenter.get_column_comments()
print(comments)  # -> {'dag_id': 'pass', 'description': 'pass', 'tags': 'pass', pass}

```

```python

# Getting a comment on a column by column name:
comments = commenter.get_column_comments('tags')
print(comments)  # -> {'tags': 'pass'}'

````

```python

# Getting comments on columns by index (ordinal number in essence):
comments = commenter.get_column_comments(1, 2)
print(comments)  # -> {'dag_id': 'pass', 'description': 'pass'}

````

```python

# Getting all available comments on an entity and its columns:
comments = commenter.get_all_comments()
print(comments)  # -> '{'table': 'pass', 'columns': {'dag_id': 'pass', 'description': 'pass', pass}}'

````

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[//]: # (- Metadata recording methods:)

#### <p align="center">Metadata recording methods</p>

```python

# Writing a comment on an entity:
commenter.set_table_comment('The table contains data unloading from Airflow.')
comments = commenter.get_table_comments()
print(comments)  # -> 'The table contains data unloading from Airflow.'

````

*Similarly for methods:*

* set_view_comment()
* set_materialized_view_comment()

```python

# Record comments on an entity by column tag:
commenter.set_column_comment(description='description_test', dag_id='dag_id_test')
comments = commenter.get_column_comments('description', 'dag_id')
print(comments)  # -> {'dag_id': 'dag_id_test', 'description': 'description_test'}

````

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[//]: # (# -------------------------------Service methods:)

#### <p align="center">Service methods</p>

```python

# Method for determining the type of entity ('table', 'view', 'mview', ...)
type_entity = commenter.get_type_entity()
print(type_entity)  # -> 'table'

````

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[//]: # (# ------------------------------- Examples of metadata overload:)

#### <p align="center">Examples of metadata overload</p>

Getting comments of a special kind compatible with the "save_comments()" method.
If it is necessary to overload all available comments (first to receive, and
after your intermediate logic) immediately save to the same or another entity
(with the same structure), there is a method  _"save_comments()"_.

A universal method for saving comments of any type (to entities or their columns):

- _commenter.save_comments(comments)_

It takes a special kind of data that allows you to explicitly indicate the
affiliation of comments from all methods to receive comments:
_"get_table_comments()", "get_column_comments()", "get_all_comments()"_.
However, for the first two it is necessary to set the flag: "service_mode=True"
(by default service_mode=False).
There is no "service_mode" in _"get_all_comments()"_, but the output corresponds
to this flag. The universal _"save_comments()"_ method allows you to save all
metadata for both columns and entities at once, limited to just one line of code.

```python

# We receive comments in "service_mode" mode before overloading:
comments = commenter.get_table_comments(service_mode=True)
print(comments)  # -> {'table': 'The table contains data unloading from Airflow.'}
commenter.save_comments(comments)

````

````python

# We receive comments in "service_mode" mode before overloading:
comments = commenter.get_column_comments(2, 3, service_mode=True)
print(comments)  # -> {'columns': {'description': 'pass', 'tags': 'pass'}}
commenter.save_comments(comments)

````

````python

# We receive all available comments:
comments = commenter.get_all_comments()
print(comments)  # -> {'table': 'pass', 'columns': {pass}}
commenter.save_comments(comments)

````

## Examples

- Download the examples file: [`examples/example_usage.py`][examples-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

- Distributed under the MIT License. See [`LICENSE`][license-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Clone the repo

````
git clone https://github.com/ArtemXYZ/t-commentor.git
````

<!-- CONTACT -->

## Contact

- GitHub - [ArtemXYZ](https://github.com/ArtemXYZ)
- Telegram - [ArtemP_khv](https://t.me/ArtemP_khv)

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS -------------------------------------------->
[PyPI Version]: https://img.shields.io/pypi/v/t-commenter?label=Version
[PyPI Downloads]: https://img.shields.io/pypi/dm/t-commenter?label=Downloads
[Python Versions]: https://img.shields.io/pypi/pyversions/t-commenter?label=Python
[PyPI License]: https://img.shields.io/pypi/l/t-commenter?label=License
[PyPI Created]: https://img.shields.io/github/created-at/ArtemXYZ/t-commenter


[GitHub Stars]: https://img.shields.io/github/stars/ArtemXYZ/t-commenter?style
[GitHub Forks]: https://img.shields.io/github/forks/ArtemXYZ/t-commenter?style
[GitHub Contributors]: https://img.shields.io/github/contributors/ArtemXYZ/t-commenter 
[GitHub Issues]:  https://img.shields.io/github/issues/ArtemXYZ/t-commenter
[GitHub Discussions]: https://img.shields.io/github/discussions/ArtemXYZ/t-commenter

[stars-url]:  https://github.com/ArtemXYZ/t-commenter/stargazers
[forks-url]:   https://github.com/ArtemXYZ/t-commenter/network/members
[contributors-url]: https://github.com/ArtemXYZ/t-commenter/contributors
[issues-url]:  https://github.com/ArtemXYZ/t-commenter/issues
[discussions-url]:  https://github.com/ArtemXYZ/t-commenter/discussions


[license-url]: https://github.com/ArtemXYZ/t-commenter/blob/main/LICENSE
[examples-url]: https://github.com/ArtemXYZ/t-commenter/blob/main/examples/example_usage.py
<!-- MARKDOWN LINKS ----------------------------------------------------->




