---
layout: page
title: Proposed Use Cases
permalink: /use-cases/
---

{% for case in site.data.cases %}

# {{ case.name }}

{{ case.description }}

[Project]({{ case.page }})


{% endfor %}

<a frameborder="0" data-theme="light" data-stack-embed="true" data-layers="1,2,3,4" href="https://embed.stackshare.io/stacks/embed/bee0c6451394287117c1e00c886b17"/></a><script async src="https://cdn1.stackshare.io/javascripts/client-code.js" charset="utf-8"></script>
