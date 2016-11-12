---
layout: page
title: Team
permalink: /team/
author: brucellino
contributors:
---

This event wouldn't have happened without the support of the organisers, facilitators and all those who participated.


<ul class="nav nav-tabs">
  <li role="presentation" class="active"><a data-toggle="tab" href="#organisers">Organsing Team</a></li>
  <li role="presentation"><a data-toggle="tab"  href="#facilitators">Facilitators</a></li>
  <!-- <li role="presentation"><a href="#special">Special Mention</a></li> -->
</ul>


<div class="tab-content clearfix">
  <div class="tab-pane fade-in active" id="organisers">
    <div class="col-sm-4">
    {% for dude in site.data.team.organisers %}
      <img class="img img-responsive img-circle" src="images/{{ site.data.team[dude].image }}">
      {{ site.data.team[dude].name }}
    {% endfor %}
  </div>
  </div>
  <div class="tab-pane fade-in" id="facilitators">
    {% for dude in site.data.team.facilitators %}
    {{ dude }}
      {{ site.data.team[dude].name }}
      <img class="team-image" src="images/{{ dude.image }}">
    {% endfor %}
  </div>
</div>
