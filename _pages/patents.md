---
layout: archive
title: "Patents"
permalink: /patents/
author_profile: true
---

You can also find my patent applications on <a href="https://scholar.google.com/citations?user=S0kwrtQAAAAJ">my Google Scholar profile</a>.

{% include base_path %}

{% for post in site.patents reversed %}
  {% include archive-single.html %}
{% endfor %}
