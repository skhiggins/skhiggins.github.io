---
layout: about
permalink: /
title: Sean Higgins
description: # <a href="">Affiliations</a>. Address. Contacts. Moto. Etc.

profile:
  align: left
  image: Higgins_Sean-5X7-2023_cropped2.jpg
  address: # >
    # <p>555 your office number</p>
    # <p>123 your address street</p>
    # <p>Your City, State 12345</p>

projects: true
news: false
social: true
---

I'm an Associate Professor of Finance (without tenure) at the [Kellogg School of Management](https://www.kellogg.northwestern.edu/) at Northwestern University. I am also an Associate Editor at the [Review of Finance](https://revfin.org/) and an Affiliated Professor at the [MIT Jameel Poverty Action Lab (J-PAL)](https://www.povertyactionlab.org/). 

<!---
:loudspeaker: JOB OPPORTUNITY :loudspeaker:
*I am currently hiring full-time empirical research associates*. More details and the link to apply are [here](https://kellogg.qualtrics.com/jfe/form/SV_ebXOK87Gy0wneZL); some additional details in this [thread](https://twitter.com/SeanKHiggins/status/1321925125399302145).
--->

My [research](research/) studies how technology reduces frictions in payments markets and consumer financial markets, and the effects of reducing these frictions on households and small firms in emerging economies. 
<!---
For example, in [one paper](assets/pdf/higgins_FinancialTechnologyAdoption.pdf) I find that when the Mexican government distributed debit cards to poor households, this led small retailers to adopt technology to accept card payments and generated spillovers to both small retailers and richer households. 
My other papers and projects study FinTech, household finance, and small firms in emerging markets.
--->
Within consumer financial markets, I have a set of papers on frictions that prevent households from saving, and a second set of papers and projects on credit market frictions. My papers employ natural experiments or randomized controlled trials (RCTs) for identification, and generally use a combination of confidential (often transaction-level) administrative data and survey data.

I teach Entrepreneurial Finance and Venture Capital to MBA students, and I won the Sidney J. Levy Teaching Award. I was named a [Poets&Quants 2024 Best 40-Under-40 MBA Professor](https://poetsandquants.com/2024/05/18/2024-best-40-under-40-mba-professors-sean-higgins-kellogg-school-of-management-northwestern-university/). <!--- for 2022-2023. I also co-teach a PhD-level independent study on Household Finance. --->

I also co-founded and co-organize the [Webinar in Finance and Development (WEFIDEV)](https://www.wefidev.com/), which hosts webinars and an annual in-person conference to enable junior researchers to share both early-stage and more-polished research on finance and development. The [__2025 WEFIDEV-RFS-CEPR Conference on Finance and Development__](/assets/pdf/WEFIDEV_call_for_papers_2025.pdf) features a dual-submission option with the Review of Financial Studies.

__Job Opportunity:__ [Dean Karlan](http://deankarlan.com/), [Jacopo Ponticelli](https://www.kellogg.northwestern.edu/faculty/ponticelli/index.html), and I are looking to hire two predocs in Finance and Development. We will review applications on a rolling basis, with a target initial review on __September 30, 2024__. Details [here](/assets/pdf/FINC_Fellows_2024-2025.pdf).

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
