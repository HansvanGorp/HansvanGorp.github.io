---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am currently a doctoral candidate affiliated with both the Signal Processing Systems group in the Electrical Engineering department at Eindhoven University of Technology (TU/e) and Philips Sleep and Respiratory Care. My primary areas of expertise encompass automatic sleep stage analysis, signal processing, and deep generative models. My Ph.D. research focuses on the intersection of those three fields, but I also enjoy going on `excursions' to explore one of these sub-fields in depth with my colleagues. Beyond my research pursuits, I have a passion for both presenting and teaching. As part of this commitment, I serve as a co-lecturer for the course "Machine Learning for Signal Processing" at TU/e. I am excited to keep growing my research expertise as well as my soft skills and hope to make a meaningful impact on the lives of those around me.

Latest Publication
==================
{% include base_path %}
{% assign latestPublication = site.publications | first %}
{% include archive-single.html post=latestPublication %}