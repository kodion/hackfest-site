---
layout: page
title: Team
permalink: /team/
author: brucellino
contributors:
---
This event wouldn't have happened without the support of the organisers, facilitators and all those who participated.
{% assign nOrganisers = site.data.team.organisers | size %}
{% comment %} We need to calculate the number of rows for nOrgs and 3 cols - ceil(nOrgs/3){% endcomment %}
{% assign nrows = nOrganisers | divided_by: 3. | ceil %}
{% assign row_offset = nrows | minus: 1 %}
<h3>Organisers</h3>
{% for row in (1..{{nrows}}) %}
<div class="row">
  {% for dude in site.data.team.organisers | offset: row_offset | limit: 3 %}
  <div class="col-sm-4">
    <div class="thumbnail">
      <img class="img img-circle" style="max-width: 90%;" src="{{ site.url }}/images/{{ site.data.team.members[dude].photo }}">
      <div class="caption text-center">
        {% if site.site.data.team.members[dude].homepage %}
        <a href="{{ site.data.team.members[dude].homepage }}">{{ site.data.team.members[dude].name }}</a>
        {% else %}
        {{ site.data.team.members[dude].name }}
        {% endif  %}
      </div> <!-- now the buttons -->
      {% if site.data.team.members[dude].orcid %}
      <a href="https://orcid.org/{{ site.data.team.members[dude].orcid }}"><img class="img-thumbnail" src="{{ site.url }}/images/ID_symbol_B-W_16x16.png" alt="{{ site.data.team.members[dude].name }}'s  ORCID" /></a>
      {% endif %}
      {% if site.data.team.members[dude].twitter %}
      <a href="https://twitter.com/{{ site.data.team.members[dude].twitter }}"><i class="fa fa-twitter-o"></i></a>
      {% endif %}
    </div>
  </div>  {% endfor %} <!-- columns -->
  {% assign row_offset = row_offset | plus: 3 %}
</div> {% endfor %} <!-- rows -->

<!-- facilitators -->
{% assign nFacilitators = site.data.team.facilitators | size %}
{% comment %} We need to calculate the number of rows for nOrgs and 3 cols - ceil(nOrgs/3){% endcomment %}
{% assign nrowsF = nFacilitators | divided_by: 3. | ceil %}
{% assign row_offset = nrows | minus: 1 %}
<h3>Facilitators</h3>
{% for row in (1..{{nrowsF}}) %}
<div class="row">
  {% for dude in site.data.team.facilitators | offset: row_offset | limit: 3 %}
  <div class="col-sm-4">
    <div class="thumbnail">
      <img class="img img-circle" style="max-width: 90%;" src="{{ site.url }}/images/{{ site.data.team.members[dude].photo }}">
      <div class="caption text-center">
        {% if site.site.data.team.members[dude].homepage %}
        <a href="site.site.data.team.members[dude].homepage">{{ site.data.team.members[dude].name }}</a>
        {% else %}
        {{ site.data.team.members[dude].name }}
        {% endif  %}
      <!-- now the buttons -->
      {% if site.data.team.members[dude].orcid %}
      <a href="https://orcid.org/{{ site.data.team.members[dude].orcid }}"><img class="img-circle" src="{{ site.url }}/images/ID_symbol_B-W_16x16.png" alt="{{ site.data.team.members[dude].name }}'s  ORCID" /></a>
      {% endif %}
      {% if site.data.team.members[dude].twitter %}
      <a href="https://twitter.com/{{ site.data.team.members[dude].twitter }}"><i class="fa fa-twitter-o"></i></a>
      {% endif %}
    </div> <!-- caption -->
  </div> <!-- thumbnail -->
  </div>  {% endfor %} <!-- columns -->
  {% assign row_offset = row_offset | plus: 3 %}
</div> {% endfor %} <!-- rows -->

<!-- presenters -->

{% assign nPresenters = site.data.team.presenters | size %}
{% comment %} We need to calculate the number of rows for nOrgs and 3 cols - ceil(nOrgs/3){% endcomment %}
{% assign nrowsF = nPresenters | divided_by: 3. | ceil %}
{% assign row_offset = nrows | minus: 1 %}
<h3>Presenters</h3>
{% for row in (1..{{nrowsF}}) %}
<div class="row">
  {% for dude in site.data.team.presenters | offset: row_offset | limit: 3 %}
  <div class="col-sm-4">
    <div class="thumbnail">
      <img class="img img-circle" style="max-width: 90%;" src="{{ site.url }}/images/{{ site.data.team.members[dude].photo }}">
      <div class="caption text-center">
        {% if site.site.data.team.members[dude].homepage %}
        <a href="site.site.data.team.members[dude].homepage">{{ site.data.team.members[dude].name }}</a>
        {% else %}
        {{ site.data.team.members[dude].name }}
        {% endif  %}
      <!-- now the buttons -->
      {% if site.data.team.members[dude].orcid %}
      <a href="https://orcid.org/{{ site.data.team.members[dude].orcid }}"><img class="img-circle" src="{{ site.url }}/images/ID_symbol_B-W_16x16.png" alt="{{ site.data.team.members[dude].name }}'s  ORCID" /></a>
      {% endif %}
      {% if site.data.team.members[dude].twitter %}
      <a href="https://twitter.com/{{ site.data.team.members[dude].twitter }}"><i class="fa fa-twitter-o"></i></a>
      {% endif %}
    </div> <!-- caption -->
  </div> <!-- thumbnail -->
  </div>  {% endfor %} <!-- columns -->
  {% assign row_offset = row_offset | plus: 3 %}
</div> {% endfor %} <!-- rows -->
