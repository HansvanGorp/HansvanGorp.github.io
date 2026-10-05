---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a postdoctoral researcher at the Eindhoven University of Technology (TU/e), working in close collaboration with NXP Semiconductors on advancing deep learning methods for automotive radar. My expertise lies at the intersection of signal processing and deep learning.

I obtained my PhD (cum laude) from the Signal Processing Systems group in the Department of Electrical Engineering at TU/e, with research conducted in partnership with Philips Sleep and Respiratory Care. During my doctoral research, I explored how deep generative models can be leveraged to improve objective sleep monitoring, while also venturing into other signal processing areas such as inverse problems and active inference. I previously completed a summer internship at Qualcomm AI Research, where I worked on geopositioning using deep Kalman filtering techniques.

Beyond research, I greatly enjoy presenting and teaching. I am the responsible lecturer for the TU/e course Machine Learning for Signal Processing, where I shape both its content and delivery. I am excited to continue expanding my expertise in the broad domain of signal processing and applied deep learning.

Latest Publication
==================
{% include base_path %}

{% assign latest = site.publications | sort: "date" | last %}
{% assign post = latest %}{% include archive-single-pub.html %}