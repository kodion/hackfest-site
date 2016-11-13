---
layout: page
title: Team
permalink: /team/
author: brucellino
contributors:
---
This event wouldn't have happened without the support of the organisers, facilitators and all those who participated.

<div container>
{% assign nOrganisers = site.data.team.organisers | size %}
{% comment %} We need to calculate the number of rows for nOrgs and 3 cols - ceil(nOrgs/3){% endcomment %}
{% assign nrows = nOrganisers | divided_by: 3 | ceil %}

{% assign row_offset = nrows | minus: 1 %}
{% for row in (1..nrows) %}
<div class="row">
  {% for dude in site.data.team.organisers | offset: row_offset | limit: 3 %}
  <div class="col-sm-4">
    <div class="thumbnail">
      {% if site.site.data.team[dude].homepage %}
      <a href="{{ site.data.team[dude].homepage }}">
      <img class="img img-circle" style="max-width: 90%;" src="{{ site.url }}/images/{{ site.data.team[dude].photo }}">
      <div class="caption text-center">
        {{ site.data.team[dude].name }}</a>
        {% else %}
        <img class="img img-circle" style="height: 3em;" src="{{ site.url }}/images/{{ site.data.team[dude].photo }}" alt="{{ site.data.team[dude].name }}'s mug">
        <div class="caption text-center">
          {{ site.data.team[dude].name }}
        {% endif  %}
      </div> <!-- now the buttons -->
      {% if site.data.team[dude].orcid %}
      <a href="https://orcid.org/{{ site.data.team[dude].orcid }}"><img class="img-thumbnail" src="{{ site.url }}/images/ID_symbol_B-W_16x16.png" alt="{{ site.data.team[dude].name }}'s  ORCID" /></a>
      {% endif %}
    </div>
  </div>  {% endfor %} <!-- columns -->
  {% assign row_offset = row_offset | plus: 3 %}
</div>
{% endfor %} <!-- rows -->

</div> <!-- container -->
