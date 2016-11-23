---
layout: page
title: Background reading and preparation
permalink: /before-prep/
author: brucellino
octocat: Professortocat_v2.png
contributors:
---
<div class="row">
</div>
[The first Sci-GaIA hackfest](http://www.sci-gaia.eu/summer-hackfest) was held during July and August 2016. It brought together researchers, service- and platform developers from several projects, including [Sci-GaIA](http://www.sci-gaia.eu) and [Indigo DataCloud](http://www.indigo-datacloud.eu). These two projects have worked on developing platforms for Open Science, bringing together widely-used tools and making them usable by researchers and research communities in whichever way they see fit.

The scope of these platforms is very wide, ranging from identity management, to data stoarge, movement and analysis, to high-performance high-throughput computing, as well as cloud and container-compute deployment.

## Introductions and warm-ups

As with any challenge, it's best to practice and come prepared.

{% for item in site.data.hackfest.checklists.before_prep %}
<h3>{{ item.name }}</h3>
{{ item.description }}
{% if item.url %}
<a href="{{ item.url }}" class="btn">Read More</a>
{% else %}
<span class="text-info">Coming Soon</span>
{% endif %}
{% endfor %}
