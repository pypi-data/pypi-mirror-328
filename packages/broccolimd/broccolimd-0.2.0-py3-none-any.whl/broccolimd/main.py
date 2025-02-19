#!/usr/bin/env python

"""broccolimd - convert Broccoli backups to markdown with attachments."""

import json
import os
import tempfile
from pathlib import Path
from typing import Any
from zipfile import ZipFile

import click

from broccolimd import __version__

# Add `-h` as alias to `--help`
CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


class Recipe:
    """Helper for all things recipe."""

    def __init__(self):
        """Set defaults."""
        self._title: str = "Untitled"
        self._filename: Path = Path("untitled.md")
        self._attachments: list[str] = []
        self._ingredients: list[str] = []
        self._directions: list[str] = []

    @property
    def title(self):
        """Sanitized title of the recipe."""
        return self._title

    @property
    def filename(self):
        """Sanitized filename for the recipe."""
        return self._filename

    @title.setter
    def title(self, value: str):
        self._title = value

    @filename.setter
    def filename(self, value: str):
        self._filename = Path(value).with_suffix(".md")

    @property
    def attachments(self):
        """List of all attachments."""
        return self._attachments

    @attachments.setter
    def attachments(self, attachments: list[str]):
        self._attachments = attachments

    def add_attachment(self, attachment: str):
        """Add a single attachment."""
        self._attachments.append(attachment)

    def add_ingredients(self, ingredients: list[str]):
        """Add list of ingredients."""
        self._ingredients.extend(ingredients)

    def add_directions(self, directions: list[str]):
        """Add list of directions."""
        self._directions.extend(directions)

    @property
    def md_ingredients(self):
        """List of ingredients in Markdown format."""
        return ["## Ingredients\n\n"] + [f"- {ingredient}" for ingredient in self._ingredients]

    @property
    def md_directions(self):
        """Numbered list of directions in Markdown format."""
        return ["## Directions\n\n"] + [f"{nr}. {step}" for nr, step in enumerate(self._directions, 1)]


def _extract_recipe_data(zipfile: ZipFile, json_path_string: str) -> dict[str, Any]:
    with zipfile.open(json_path_string) as jsonfile:
        data = json.load(jsonfile)

        return data


def _write_markdown(output_markdown_dir: Path, output_media_dir: Path, recipe: Recipe):
    with Path.open(output_markdown_dir / recipe.filename, "w+") as markdownfile:
        markdownfile.writelines([f"# {recipe.title}\n\n"])
        if recipe.attachments:
            markdownfile.writelines(
                [f"![{attachment}]({output_media_dir}/{attachment})\n" for attachment in recipe.attachments] + ["\n"]
            )
        markdownfile.writelines(recipe.md_ingredients + ["\n\n"] + recipe.md_directions)


def _extract_recipe(input_file: Path, output_markdown_dir: Path, output_media_dir: Path):
    recipe = Recipe()
    with ZipFile(input_file, "r") as zipfile:
        for name in zipfile.namelist():
            if name.endswith(".json"):
                click.echo(f"Converting {name} to markdown")
                data = _extract_recipe_data(zipfile, name)
                recipe.title = data["title"]
                recipe.filename = name
                recipe.add_ingredients(data["ingredients"].splitlines(keepends=True))
                recipe.add_directions(data["directions"].splitlines(keepends=True))
            else:
                click.echo(f"Adding attachment {name}")
                zipfile.extract(name, output_media_dir)
                recipe.add_attachment(name)

    _write_markdown(output_markdown_dir, output_media_dir, recipe)


def _extract_recipes(zipfile: ZipFile, output_markdown_dir: Path, output_media_dir: Path):
    """
    Extract recipes from the backup file.

    Broccoli backups are basically just nested ZIP archives with some metadata. Each recipe is a ZIP archive
    containing one JSON file and optionally attachments. The JSON file stores all the recipe information like
    ingredients, directions, and assigned categories. These recipe ZIP archives are contained within the backup
    file that can be exported from Broccoli. The backup file itself is also a ZIP archive. In addition to the
    recipes, available categories can be found in the backup in form of a JSON file:

    BACKUP.broccoli-archive
      ↳ categories.json
      ↳ RECIPE-A.broccoli
        ↳ recipe-a.json
        ↳ recipe-a.jpg
      ↳ RECIPE-B.broccoli
        ↳ recipe-b.json
    """
    # Extract the outermost archive in a temporary directory, it can be thrown away once all recipes have been extracted
    with tempfile.TemporaryDirectory() as tempdirname:
        for name in zipfile.namelist():
            if name.endswith(".broccoli"):
                zipfile.extract(name, tempdirname)
        click.echo(f"temp dir: {os.listdir(tempdirname)}")
        for recipe in os.listdir(tempdirname):
            _extract_recipe(Path(tempdirname) / Path(recipe), output_markdown_dir, output_media_dir)


@click.version_option(__version__)
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--output-markdown-dir",
    type=click.Path(file_okay=False, resolve_path=True, path_type=Path),
    default=Path("recipes"),
)
@click.option(
    "--output-media-dir",
    type=click.Path(file_okay=False, resolve_path=True, path_type=Path),
    default=Path("recipes/media"),
)
@click.argument("input-file", type=click.Path(dir_okay=False, resolve_path=True, path_type=Path))
def cli(input_file: Path, output_media_dir: Path, output_markdown_dir: Path):
    """Run broccolimd."""
    try:
        output_markdown_dir.mkdir(exist_ok=True)
    except PermissionError as err:
        message = f"Permission denied: {output_markdown_dir}"
        raise click.ClickException(message) from err
    except Exception as err:
        raise click.ClickException(str(err)) from err

    try:
        output_media_dir.mkdir(exist_ok=True)
    except PermissionError as err:
        message = f"Permission denied: {output_media_dir}"
        raise click.ClickException(message) from err
    except Exception as err:
        raise click.ClickException(str(err)) from err

    with ZipFile(input_file, "r") as zipfile:
        _extract_recipes(zipfile, output_markdown_dir, output_media_dir)


if __name__ == "__main__":
    cli()
