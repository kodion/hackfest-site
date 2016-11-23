---
layout: page
title: Warmup Checklist
permalink: /before-checklist/
octocat: dodgetocat_v2.png
author: brucellino
contributors:
---

We have only a few days to learn something new and use it to move mountains. The more you do before the hackfest, the more you will get out of it.

### You must
<ol>
{% for item in site.data.hackfest.checklists.before %}
<li> <strong>{{ item.name }}</strong> : {{ item.more }}
{% if item.link %}
  {% if item.link.external == false %}
  <a href="{{ site.url }}{{ item.link.url }}" class="btn btn-small">More</a>
  {% else %}
  <a href="{{ item.link.url }}" class="btn btn-small">More</a>
  {% endif %}
  {% endif %}
</li>
{% endfor %}
</ol>

If you have issues on any of these issues, drop the organisers an email <a href="mailto:{{ site.organiser.email }}" class="btn btn-small"><i class="fa fa-envelope-o"></i></a>

## All done ? Prove it !

In order to show that you've finished this checklist tell us :

  * **That your dev environment is set up** (Self-asserted)
  * **Your github user name** _e.g._ `brucellino`
  * **Your project's repository url** _e.g._ `https://github.com/AAROC/rasr-app`
  * **Your project's StackShare url** _e.g._ `http://stackshare.io/sci-gaia-e-research-hackfest/dev-and-integration-platform`

 <a href="{{ site.data.hackfest.start_topic }}" class="btn">reply to the introduction topic</a>.

### Next

If you're all squared away, why not take a look at the <a href="{{ site.url }}/prerequisites">course prerequisites</a>.
