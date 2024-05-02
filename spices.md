---
title: Spices
longtitle: 'Spice Blends'
description: 'Spice packet ingredients, for making your own'
navbar: 3
---
This is a list of the contents of the spice blends provided by EveryPlate and HelloFresh, in case you'd
like to make them yourself.

## Help Out

See something missing? Submit [an issue](https://github.com/eslindsey/everyplate/issues) to the repository!

Big shout out to [u/letitburn22](https://www.reddit.com/user/letitburn22/) for compiling this initial list
[on Reddit](https://www.reddit.com/r/hellofresh/comments/bawnby/hello_fresh_diy_spice_blends/)!

## Parts

If the recipe you're looking for only lists "parts," they are specifying the ingredients in terms of each
other. For example, if the recipe is 3 parts salt, 1 part black pepper, you could make that using 3 tsp of
salt and 1 tsp of pepper, or 6 TBSP of salt and 2 TBSP of pepper, or whatever unit is convenient for the
amount you are trying to make.

## Table of Contents

{% for s in site.spices | sort: 'title' %}
  * [{{ s.title }}]({{ s.url | relative_url }})
{% endfor %}

## Notes

1. "hu" is heat unit. Most blends call for a low heat cayenne pepper (7,500 heat units or 7.5k hu) on the Scoville Scale.
