---
layout: about
permalink: /
title: Sean Higgins
description: # <a href="">Affiliations</a>. Address. Contacts. Moto. Etc.

profile:
  align: left
  image: prof_pic.jpg
  address: # >
    # <p>555 your office number</p>
    # <p>123 your address street</p>
    # <p>Your City, State 12345</p>

projects: true
news: false
social: true
---

I'm a Post-Doctoral Fellow at the Center for Effective Global Action at the University of California, Berkeley.

My research combines the fields of development economics and household finance. I primarily study financial inclusion, or the impact of access to financial services for the poor.

I'm grateful to the 
[Bill & Melinda Gates Foundation](https://www.gatesfoundation.org/How-We-Work/Quick-Links/Grants-Database/Grants/2013/11/OPP1097490), 
<<<<<<< HEAD
[CEGA-Visa Financial Inclusion Lab](https://cega.berkeley.edu/assets/cega_programs/8/FIL_RFP_Press_Release.pdf), 
[Development Impact Lab/USAID](https://dil.berkeley.edu/), 
[Digital Credit Observatory](https://www.digitalcreditobservatory.org/2017-grantees.html), 
[Fisher Center for Business Analytics](https://businessanalytics.berkeley.edu/), 
[Fulbright Program](https://us.fulbrightonline.org/), 
[Innovations for Poverty Action](https://www.poverty-action.org/study/leveraging-government-transfers-offer-low-risk-microcredit-dominican-republic), 
=======
[CEGA-Visa Financial Inclusion Lab](http://cega.berkeley.edu/assets/cega_programs/8/FIL_RFP_Press_Release.pdf), 
[Development Impact Lab/USAID](https://dil.berkeley.edu/), 
[Fisher Center for Business Analytics](https://businessanalytics.berkeley.edu/), 
[Digital Credit Observatory](http://www.digitalcreditobservatory.org/2017-grantees.html), 
[Fulbright Program](https://us.fulbrightonline.org/), 
[Innovations for Poverty Action](http://www.poverty-action.org/study/leveraging-government-transfers-offer-low-risk-microcredit-dominican-republic), 
>>>>>>> 3445714e3ed0501154a55070304d28218dbdbcde
[Institute for Business Innovation](https://businessinnovation.berkeley.edu/), 
[J-PAL](https://www.povertyactionlab.org/GPI), 
National Science Foundation 
([doctoral dissertation grant](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1530800&HistoricalAwards=false) 
<<<<<<< HEAD
and [standard grant](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1758837&HistoricalAwards=false)), and 
=======
and [standard grant](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1758837&HistoricalAwards=false), and 
>>>>>>> 3445714e3ed0501154a55070304d28218dbdbcde
[UN Foundation](https://www.data2x.org/big-data-challenge-awards/#credit) for research funding.

{% for project in site.projects %}

{% if project.redirect %}
<div class="project">
    <div class="thumbnail">
        <a href="{{ project.redirect }}" target="_blank">
        {% if project.img %}
        <img class="thumbnail" src="{{ project.img | prepend: site.baseurl | prepend: site.url }}"/>
        {% else %}
        <div class="thumbnail blankbox"></div>
        {% endif %}    
        <span>
            <h1>{{ project.title }}</h1>
            <br/>
            <p>{{ project.description }}</p>
        </span>
        </a>
    </div>
</div>
{% else %}

<div class="project ">
    <div class="thumbnail">
        <a href="{{ project.url | prepend: site.baseurl | prepend: site.url }}">
        {% if project.img %}
        <img class="thumbnail" src="{{ project.img | prepend: site.baseurl | prepend: site.url }}"/>
        {% else %}
        <div class="thumbnail blankbox"></div>
        {% endif %}    
        <span>
            <h1>{{ project.title }}</h1>
            <br/>
            <p>{{ project.description }}</p>
        </span>
        </a>
    </div>
</div>

{% endif %}

{% endfor %}
