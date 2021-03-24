---
layout: about
permalink: /
title: Sean Higgins
description: # <a href="">Affiliations</a>. Address. Contacts. Moto. Etc.

profile:
  align: left
  image: Higgins-Sean-250x304_cropped.jpg
  address: # >
    # <p>555 your office number</p>
    # <p>123 your address street</p>
    # <p>Your City, State 12345</p>

projects: true
news: false
social: true
---

I'm an Assistant Professor of Finance at the [Kellogg School of Management](https://www.kellogg.northwestern.edu/) at Northwestern University.

<!---
:loudspeaker: JOB OPPORTUNITY :loudspeaker:
*I am currently hiring full-time empirical research associates*. More details and the link to apply are [here](https://kellogg.qualtrics.com/jfe/form/SV_ebXOK87Gy0wneZL); some additional details in this [thread](https://twitter.com/SeanKHiggins/status/1321925125399302145).
--->

My [research](research/) studies how technology reduces barriers to financial inclusion, and the effect of reducing these barriers on households and small businesses. For example, in [one paper](assets/pdf/higgins_FinancialTechnologyAdoption.pdf) I find that when the Mexican government distributed debit cards to poor households, this led small retailers to adopt technology to accept card payments and generated spillovers to both small retailers and richer households. 
My other papers and projects study FinTech, household finance, and small businesses in developing countries.

I teach Entrepreneurial Finance and Venture Capital to MBA students.

<!---
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
--->

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
