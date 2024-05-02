---
title: About
permalink: /
navbar: 1
---
# About

This is a repository of information about the EveryPlate (and HelloFresh) meal
kits and their recipes.

## Help Out

You are welcomed (and encouraged) to submit
[issues](https://github.com/eslindsey/everyplate/issues) or
[pull requests](https://github.com/eslindsey/everyplate/) to add or update
missing/out-of-date information.

## Pages

<dl>
  {% assign nav_pages = site.pages | where_exp: 'p', 'p.navbar > 1' | sort: 'navbar' %}
  {% for p in nav_pages %}
    <dt><a href="{{ p.url | relative_url }}">{{ p.longtitle }}</a></dt>
    <dd>{{ p.description }}</dd>
  {% endfor %}
</dl>
