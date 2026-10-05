---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
classes: ruled-headings
---

You can also find these articles on <a href="https://scholar.google.com/citations?user=S0kwrtQAAAAJ">my Google Scholar profile</a>.

{% include base_path %}

{% assign pubs = site.publications | sort: "date" | reverse %}
{% assign pubs_by_year = pubs | group_by_exp: "pub", "pub.date | date: '%Y'" %}
{% for year in pubs_by_year %}
<h2 class="pub-year">{{ year.name }}</h2>
{% for post in year.items %}{% include archive-single-pub.html %}{% endfor %}
{% endfor %}
