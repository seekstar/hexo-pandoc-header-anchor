# hexo-pandoc-header-anchor

Add anchors to each header like [markdown-it](https://github.com/hexojs/hexo-renderer-markdown-it).

## Getting started

### Prerequisites

[hexo-renderer-pandoc](https://github.com/hexojs/hexo-renderer-pandoc) should be used as the renderer of hexo.

`pandoc` and [panflute](https://github.com/sergiocorreia/panflute) should be installed. Note that the version of `panflute` should match the version of `pandoc`: <https://github.com/sergiocorreia/panflute#supported-pandoc-versions>.

### Install

```shell
npm install hexo-pandoc-header-anchor --save
```

Add the following configurations to `_config.yml`:

```yaml
pandoc:
  filters:
    - node_modules/hexo-pandoc-header-anchor/header-anchor.py
```

Then `hexo clean && hexo s -g` to preview effects. `¶` is the anchor of the corresponding header. Example: <https://seekstar.github.io/2022/03/10/a-collection-of-matrix-groups/>

## Options

```yaml
pandoc:
  meta:
    - header_anchor_str: '¶'
    # 'left' | 'right'
    - header_anchor_side: 'left'
```

The above values are default. You may change them to customize.

## LICENSE

This project is licensed under the ISC License.

## Credits

This project is inspired by [hexo-pandoc-tippy](https://github.com/Ritsuka314/hexo-pandoc-tippy) and [leonfancy.github.io](https://github.com/leonfancy/leonfancy.github.io)/pandocfilters/header_link.py.
