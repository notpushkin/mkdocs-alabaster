# User guide

## Installation

First, install the `mkdocs-alabaster` package from PyPI:

```
$ pip install mkdocs-alabaster
```

(If you used [`pipsi`][pipsi] to install MkDocs, you should install the theme into that virtualenv as well:)

```
$ ~/.local/venvs/mkdocs/bin/pip install mkdocs-alabaster
```

Then enable the `alabaster` theme in your `mkdocs.yml`:

```
theme: alabaster
```

That's it! You now have the standard Alabaster theme set up. Read on for more configuration options/concerns.

### Permalinks

Set `markdown_extensions.toc.permalink` to `"¶"` to add permalinks to the headers (visible on hover). “¶” is the default symbol used by Sphinx, you can use something else if you want.

### Theme options


#### `extra.logo`

Relative path (from `$PROJECT/docs/`) to a logo image, which will appear in the upper left corner above the name of the project.

> If logo is not set, your project name setting (from the MkDocs config) will be used in a text header instead. This preserves a link back to your homepage from inner doc pages.

#### `extra.logo_name`

Set to `true` to insert your site's `project` name under the logo image as text. Useful if your logo doesn't include the project name itself. Defaults to `false`.

#### `extra.logo_title`

Logo's title attribute. Default: your `site_name`.

#### `extra.include_toc`

Boolean, whether to include TOC in sidebar navigation or not. Default: false.

#### `extra.extra_nav_links`

A dict of navigation links. Example:

```yaml
extra:
  extra_nav_links:
    Fork me on GitHub: https://github.com/iamale/rock-cli
```

### `extra.show_powered_by`

Show “Powered by” message, mentioning MkDocs and this theme. Default: true.

### Example

```yaml
site_name: rock-cli
theme: alabaster
copyright: 2016 Alexander Pushkov

markdown_extensions:
  - toc:
      permalink: "¶"

extra:
  logo: logo.png
  logo_title: "Rocketbank logo"
  include_toc: yes
  extra_nav_links:
    Fork me on GitHub: https://github.com/iamale/rock-cli
```
