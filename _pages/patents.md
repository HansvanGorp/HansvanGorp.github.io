---
layout: archive
title: "Patents"
permalink: /patents/
author_profile: true
classes: ruled-headings
---

You can find all my patents on <a href="https://scholar.google.com/citations?user=S0kwrtQAAAAJ">my Google Scholar profile</a>.

{% include base_path %}

{% assign patents = site.patents | sort: "date" | reverse %}
{% assign patents_by_year = patents | group_by_exp: "pub", "pub.date | date: '%Y'" %}
{% for year in patents_by_year %}
<h2 class="pub-year">{{ year.name }}</h2>
{% for post in year.items %}{% include archive-single-pub.html %}{% endfor %}
{% endfor %}
