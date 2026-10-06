---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
classes: cv-page ruled-headings
redirect_from:
  - /resume
---

{% include base_path %}

<p class="cv-download"><a class="btn" href="{{ base_path }}/files/cv.pdf"><i class="fas fa-file-pdf" aria-hidden="true"></i> Download CV (PDF)</a></p>

<div class="print-only cv-print-header">
  <div>
    <p class="cv-print-header__name">{{ site.author.name }}</p>
    <p class="cv-print-header__role">{{ site.author.bio }} · {{ site.author.employer }}</p>
    <p class="cv-print-header__contact">{{ site.author.email }} · hansvangorp.github.io · {{ site.author.location }}</p>
  </div>
  <img class="cv-print-header__photo" src="{{ base_path }}/images/profile-print.jpg" alt="{{ site.author.name }}">
</div>

Research areas
-----
* Signal Processing
* Deep learning
* Deep generative models
* Deep learning for inverse problems
* Active Inference
* Automatic sleep staging
* FMCW radar processing
* Ultrasound operator guidance
{: .cv-research-areas}

Education
-----
* PhD (cum laude) on deep generative modeling in sleep diagnostics, Eindhoven University of Technology and Philips Sleep and Respiratory Care, 2026
* MSc in Electrical Engineering, Eindhoven University of Technology, 2020
* BSc in Electrical Engineering, Eindhoven University of Technology, 2018

Work experience
-----
* February 2026 - Present: Postdoctoral researcher
  * Eindhoven University of Technology, Department of Electrical Engineering, [Signal Processing Systems](https://www.tue.nl/en/research/research-groups/signal-processing-systems/)
  * NXP Semiconductors
  * Project: Deep learning in automotive radar

* September 2020 - January 2026: PhD (cum laude)
  * Eindhoven University of Technology, Department of Electrical Engineering, Signal Processing Systems, [BM/d Lab](https://www.tue.nl/en/research/research-groups/signal-processing-systems/biomedical-diagnostics-lab/)
  * Philips Sleep and Respiratory Care, Eindhoven
  * Project: [Deep Generative Modeling in Sleep Diagnostics](https://hansvangorp.github.io/publication/2026-01-22)

* July 2024 - November 2024: PhD Internship
  * Qualcomm AI Research, Amsterdam
  * Project: [Neural Augmented Kalman Filters for Road Network Assisted GNSS Positioning](https://hansvangorp.github.io/publication/2025-06-06)

* August 2019 - October 2019: Research Intern
  * Philips Research, Eindhoven
  * Project: Suppression of pump distortion for inflation-based noninvasive blood pressure measurement

Grants awarded
-----
* 2026: TTT-AI voucher
  * Polaris: Operator Guidance for Carotid Ultrasound

Publications
-----
{% assign cv_pubs = site.publications | sort: "date" | reverse %}
<ul class="cv-pubs">{% for post in cv_pubs %}{% include archive-single-cv.html %}{% endfor %}</ul>

Patents
-----
{% assign cv_patents = site.patents | sort: "date" | reverse %}
<ul class="cv-pubs">{% for post in cv_patents %}{% include archive-single-cv.html %}{% endfor %}</ul>

Teaching
-----
* September 2026 - Present: Responsible lecturer
  * Eindhoven University of Technology
  * Course: [Machine Learning for Signal Processing](https://hansvangorp.github.io/teaching/)

* September 2020 - September 2026: co-lecturer
  * Eindhoven University of Technology
  * Course: [Machine Learning for Signal Processing](https://hansvangorp.github.io/teaching/)

* September 2016 - September 2020: Student Teaching Assistant
  * Eindhoven University of Technology
  * Courses: Computation, Calculus, Applied Physics

Volunteering
-----
* Leader at Scouting Nederland for the 'welpen' (cub scouts), kids aged 7 through 11
