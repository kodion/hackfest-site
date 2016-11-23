---
layout: page
title: Development Environment
permalink: /dev-env/
author: brucellino
octocat: constructocat2.jpg
contributors:
---
<div class="row">
  
</div>
The **development environment** refers to a setup where all of the dependencies and configuration needed to both **develop** and **test** your applicaiton are available. The development environment should be as close as possible to the **deployment** environment. The tools described here are the **bare minimum** needed to complete the warmup exercises.

## General description

You will need :

### OS libraries

<ul>
{% for tool in site.data.hackfest.dev_env_generic %}
<li>
  <span class="devicons devicons-{{ tool.icon }}" style="font-size: 2em;"></span><strong>{{ tool.name }}</strong>: {{ tool.more }}.
  <a href="{{ tool.link.url }}" class="btn btn-small">More</a>
</li>
{% endfor %}
</ul>

### Language-specific stacks

**Suggested applications and libraries**

We expect you to know your application stack well and use whichever tools make sense to you. It is very useful to have a REST inspector in your browser for testing, and we suggest using [Postman](https://www.getpostman.com/) for testing how your code uses the APIs of the various components of the platform.



Here are a few suggestions for language-specific stacks:


  * <span class="devicons devicons-python"></span>**Python** : [Python Requests](http://docs.python-requests.org/en/master/)
  * <span class="devicons devicons-ruby"></span>**Ruby** : [HTTParty](http://johnnunemaker.com/httparty/)



# Set up your own

<span class="text-info">Coming soon</span>

# Use Docker

<span class="text-info">Coming soon</span>

# Use a machine provided for you

<span class="text-info">Coming soon</span>
