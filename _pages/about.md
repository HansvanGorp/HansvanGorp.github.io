---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am currently a doctoral candidate affiliated with both the Signal Processing Systems group in the Electrical Engineering department at Eindhoven University of Technology (TU/e) and Philips Sleep and Respiratory Care. The expected end date of my PhD is the end of 2025. My primary areas of expertise encompass signal processing, automatic sleep stage analysis, and deep generative models. My Ph.D. research focuses on the intersection of those three fields, but I also enjoy going on `excursions' to explore different topics, such as inverse problems and active inference. Moreover, I successfully completed a summer internship at Qualcomm AI research on the topic of geopositioning with deep Kalman filters. Beyond my research pursuits, I have a passion for both presenting and teaching. As part of this commitment, I serve as a co-lecturer for the course "Machine Learning for Signal Processing" at TU/e. I am excited to keep growing my research expertise in the broad domain of signal processing.

Latest Publication
==================
{% include base_path %}

{% for post in site.publications %}
  {% if forloop.last %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}