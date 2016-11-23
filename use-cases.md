---
layout: page
title: Proposed Use Cases
permalink: /use-cases/
---

Use cases will be described here, as we gather information on them. See the [checklist]({{ site.url}}checklist/) for information on how to prepare your use case.
{% for case in site.data.cases %}

## The Open Science Platform services

Most of the [Open Science Platform](http://www.sci-gaia.eu/osp) stack is summarised below. 

<a frameborder="0" data-theme="light" data-stack-embed="true" data-layers="1,2,3,4" href="https://embed.stackshare.io/stacks/embed/863388deec358f970fb96178a43ec1"/><script async src="https://cdn1.stackshare.io/javascripts/client-code.js" charset="utf-8"></script>

### {{ case.name }}

{{ case.description }}

[Project]({{ case.page }})


{% endfor %}
