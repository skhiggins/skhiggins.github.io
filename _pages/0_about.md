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

I'm an Assistant Professor of Finance at the [Kellogg School of Management](https://www.kellogg.northwestern.edu/) at Northwestern University.

My [research](research/) studies how technology reduces frictions in financial markets, and the effect of reducing these frictions on households and small firms. For example, in [one paper](assets/pdf/higgins_jmp.pdf) I study financial technology adoption and quantify the spillovers of consumers' adoption of a particular financial technology—debit cards—on both the supply and demand sides of the market. 
My other papers and projects study FinTech, household finance, and small firms in developing countries.

I'm grateful to the 
[Bill & Melinda Gates Foundation](https://www.gatesfoundation.org/How-We-Work/Quick-Links/Grants-Database/Grants/2013/11/OPP1097490), 
[CEGA-Visa Financial Inclusion Lab](http://cega.berkeley.edu/assets/cega_programs/8/FIL_RFP_Press_Release.pdf), 
[Digital Credit Observatory](http://www.digitalcreditobservatory.org/2017-grantees.html), 
[Facebook](https://research.fb.com/blog/2020/08/announcing-the-winners-of-the-economic-impact-of-digital-technologies-request-for-proposals/),
[Fulbright Program](https://us.fulbrightonline.org/), 
Guthrie Center for Real Estate Research,
[Innovations for Poverty Action](http://www.poverty-action.org/study/leveraging-government-transfers-offer-low-risk-microcredit-dominican-republic), 
Inter-American Development Bank,
J-PAL,
National Science Foundation 
([doctoral dissertation grant](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1530800&HistoricalAwards=false) 
and [standard grant](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1758837&HistoricalAwards=false)), 
[Think Forward Initiative](https://www.thinkforwardinitiative.com/stories/the-impact-of-price-comparison-tools-in-consumer-credit-markets-on-financial-decision-making),
[UN Foundation](https://www.data2x.org/big-data-challenge-awards/#credit) 
and [USAID](https://www.usaid.gov/sites/default/files/documents/15396/ClosingGenderDigitalDivide_Round1.pdf)
for research funding.

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
