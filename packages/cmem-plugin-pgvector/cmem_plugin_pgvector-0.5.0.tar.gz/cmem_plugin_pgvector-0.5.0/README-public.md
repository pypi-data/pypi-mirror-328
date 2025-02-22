# cmem-plugin-pgvector

[![poetry][poetry-shield]][poetry-link] [![ruff][ruff-shield]][ruff-link] [![mypy][mypy-shield]][mypy-link] [![copier][copier-shield]][copier] 

Store embedding vectors into a Postgres vector store.

This plugin consumes the costumable entity's paths ```embedding```, ```text``` and ```metadata``` as following:

  - The text path contain the text used to generate the embeddings, default ```text```.
  - The embedding path contain the embedding representation of the text, default ```embedding```.
  - The metadata path contain the information that will be associated with the embedding, default all paths.

[![eccenca Corporate Memory][cmem-shield]][cmem-link]

## Use

Interact with Large Language Models.

This is a plugin for [eccenca](https://eccenca.com) [Corporate Memory](https://documentation.eccenca.com).

You can install it with the [cmemc](https://eccenca.com/go/cmemc) command line
clients like this:

```
cmemc admin workspace python install cmem-plugin-llm
```

### Parameters

- ```collection_name```: The name of the collection where the embeddings are going to be stored, default ```my_collection```
- ```user```:the database user
- ```password```: the database password
- ```host```: the databse host, i.e. locahost
- ```port```: the database port, default ```5432```
- ```database```: the name of the database
- ```pre_delete_collection```: boolean parameter indicating if the collection should be cleanse before insertion, default ```false```
- ```embedding_path```: output path that will contain the generated embedding, default ```embedding```
- ```text_path```: path containing the text used for genereting the embedding, default ```text```
- ```metadata_paths```: paths from the entity that will be stored along with the embedding, default all paths

[cmem-link]: https://documentation.eccenca.com
[cmem-shield]: https://img.shields.io/endpoint?url=https://dev.documentation.eccenca.com/badge.json
[poetry-link]: https://python-poetry.org/
[poetry-shield]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json
[ruff-link]: https://docs.astral.sh/ruff/
[ruff-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&label=Code%20Style
[mypy-link]: https://mypy-lang.org/
[mypy-shield]: https://www.mypy-lang.org/static/mypy_badge.svg
[copier]: https://copier.readthedocs.io/
[copier-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json

