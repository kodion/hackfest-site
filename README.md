[![StackShare](https://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/sci-gaia-e-research-hackfest/dev-and-integration-platform) [![The MIT License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![Travis CI](https://img.shields.io/travis/AAROC/hackfest-site.svg?style=flat-square)](https://travis-ci.org/AAROC/hackfest-site)

# Hackfest Site

A responsive website for Summer Hackfest events.
  This theme requires ruby and rubygems installed

This provides an "event pack" for the participants and organisers, provide a unique place to host all of the information, and tie together planning. The website can be forked and hosted (on Github Pages or locally) in order to theme and tweak the event.

# Metadata

Events are described by metadata in files in `_data/`.

##  Event (Hackfest)

Metadata about the specific event are kept in the top-level `_config.yml` file. Some variables should be set for the specific event :

  1. `title`: The title of the hackfest, _e.g._ "Area Awesome Hackfest". This appears as the main title on the front page
  1. `description`: A short description of the event. _e.g._ "Bring your science to the web and the web to your science". This appears as a quote beneath the main title.
  1. `url`: The url where the pages for your event willm be hosted, _e.g._ http://www.africa-grid.org/hackfest-site/. Jekyll will build the pages for this url.
url: '/'
# google_analytics: 'UA-XXXXXX-X'
# disqus_shortname: 'your-disqus-name'

intro: 'The Sci-GaIA Hackfest brings together e-Science platform developers and scientists, to build tools for scientific discovery. Bring your science to the web and the web to your science. These pages contain everything you need to get going and get it built'

organiser:
  name: 'Sci-GaIA Project'
  email: info@sci-gaia.eu
  twitter_username: ei4africa
  facebook_username:
  github_username: Sci-GaIA
  linkedin_username:
infrastructure:
  jenkins_url: 'https://ci.sagrid.ac.za'

# Assets

There are some static files and scripts in `assets` which are useful for seeding the event. 

## What this is for

This is a generic template website which can be forked for further iterations of the [Sci-GaIA Summer Hackfest](http://www.sci-gaia.eu/summer-hackfest).

## What this is not for

  1. This is not a substitute for
    * **The Sci-GaIA summer hackfest page**. That describes an event, along with subsequent champions and activities, including all links to relevant material. This is a more tactical set of pages in order to support the organisers and facilitators.
    * **The agenda**. Indico should be used for planning the timetable.
    * **Presentation and video material**. That content should remain citable and so hosted on an Open Access repository.
    * **The online classroom and assessment**. This is just a static website to publicise the event and prepare. Classroom and assessment activities should be done with an appropriate tool, such as an online learning platform or Github Classroom.

### Install and Test

1. Download or clone repo `git clone https://github.com/AAROC/hackfest-site`
2. Enter the folder: `cd hackfest-site/`
3. If you don't have bundler installed: `gem install bundler`
3. Install Ruby gems: `bundle install`
4. Start Jekyll server: `bundle exec jekyll serve --watch`

Access via: [http://localhost:4000/](http://localhost:4000/)

---
