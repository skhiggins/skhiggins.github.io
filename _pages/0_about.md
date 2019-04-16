---
layout: about
permalink: /
title: Sean Higgins
description: # <a href="">Affiliations</a>. Address. Contacts. Moto. Etc.

profile:
  align: left
  image: pic2.JPG
  address: # >
    # <p>555 your office number</p>
    # <p>123 your address street</p>
    # <p>Your City, State 12345</p>

projects: true
news: false
social: true
---

I'm a Post-Doctoral Fellow at the [Center for Effective Global Action](http://cega.berkeley.edu) and [Haas School of Business](https://haas.berkeley.edu/) at the University of California, Berkeley. 

I'll be an Assistant Professor of Finance at the [Kellogg School of Management](https://www.kellogg.northwestern.edu/) at Northwestern University starting in July 2020, after a one-year Post-Doctoral Fellowship in Household Finance at the [National Bureau of Economic Research](https://www.nber.org/).

My [research](research/) studies how technology reduces frictions in financial markets, and the effect of reducing these frictions on households and small firms.
My [job market paper](assets/pdf/higgins_jmp.pdf) studies financial technology adoption: I study the spillovers of consumers' adoption of a particular financial technology—debit cards—on both the supply and demand sides of the market. 
My other working papers and projects study FinTech and the impact of access to entrepreneurial and household finance.

I'm grateful to the 
[Bill & Melinda Gates Foundation](https://www.gatesfoundation.org/How-We-Work/Quick-Links/Grants-Database/Grants/2013/11/OPP1097490), 
[CEGA-Visa Financial Inclusion Lab](http://cega.berkeley.edu/assets/cega_programs/8/FIL_RFP_Press_Release.pdf), 
[Digital Credit Observatory](http://www.digitalcreditobservatory.org/2017-grantees.html), 
[Fulbright Program](https://us.fulbrightonline.org/), 
[Innovations for Poverty Action](http://www.poverty-action.org/study/leveraging-government-transfers-offer-low-risk-microcredit-dominican-republic), 
National Science Foundation 
([doctoral dissertation grant](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1530800&HistoricalAwards=false) 
and [standard grant](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1758837&HistoricalAwards=false)), and 
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
