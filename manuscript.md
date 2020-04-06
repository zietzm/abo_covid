---
author-meta:
- Michael Zietz
bibliography:
- content/manual-references.json
date-meta: '2020-04-06'
header-includes: '<!--

  Manubot generated metadata rendered from header-includes-template.html.

  Suggest improvements at https://github.com/manubot/manubot/blob/master/manubot/process/header-includes-template.html

  -->

  <meta name="dc.format" content="text/html" />

  <meta name="dc.title" content="Testing the association between blood type and COVID-19 infection, intubation, and death" />

  <meta name="citation_title" content="Testing the association between blood type and COVID-19 infection, intubation, and death" />

  <meta property="og:title" content="Testing the association between blood type and COVID-19 infection, intubation, and death" />

  <meta property="twitter:title" content="Testing the association between blood type and COVID-19 infection, intubation, and death" />

  <meta name="dc.date" content="2020-04-06" />

  <meta name="citation_publication_date" content="2020-04-06" />

  <meta name="dc.language" content="en-US" />

  <meta name="citation_language" content="en-US" />

  <meta name="dc.relation.ispartof" content="Manubot" />

  <meta name="dc.publisher" content="Manubot" />

  <meta name="citation_journal_title" content="Manubot" />

  <meta name="citation_technical_report_institution" content="Manubot" />

  <meta name="citation_author" content="Michael Zietz" />

  <meta name="citation_author_institution" content="Department of Biomedical Informatics, Columbia University" />

  <meta name="citation_author_orcid" content="0000-0003-0539-630X" />

  <meta name="twitter:creator" content="@ZietzMichael" />

  <link rel="canonical" href="https://zietzm.github.io/abo_covid/" />

  <meta property="og:url" content="https://zietzm.github.io/abo_covid/" />

  <meta property="twitter:url" content="https://zietzm.github.io/abo_covid/" />

  <meta name="citation_fulltext_html_url" content="https://zietzm.github.io/abo_covid/" />

  <meta name="citation_pdf_url" content="https://zietzm.github.io/abo_covid/manuscript.pdf" />

  <link rel="alternate" type="application/pdf" href="https://zietzm.github.io/abo_covid/manuscript.pdf" />

  <link rel="alternate" type="text/html" href="https://zietzm.github.io/abo_covid/v/82c9fbc89799845b97081e701b01539b4ac696a3/" />

  <meta name="manubot_html_url_versioned" content="https://zietzm.github.io/abo_covid/v/82c9fbc89799845b97081e701b01539b4ac696a3/" />

  <meta name="manubot_pdf_url_versioned" content="https://zietzm.github.io/abo_covid/v/82c9fbc89799845b97081e701b01539b4ac696a3/manuscript.pdf" />

  <meta property="og:type" content="article" />

  <meta property="twitter:card" content="summary_large_image" />

  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />

  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />

  <meta name="theme-color" content="#ad1457" />

  <!-- end Manubot generated metadata -->'
keywords:
- covid-19
- coronavirus
- blood type
- observational data
- biomedical informatics
lang: en-US
manubot-clear-requests-cache: false
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
title: Testing the association between blood type and COVID-19 infection, intubation, and death
...






<small><em>
This manuscript
([permalink](https://zietzm.github.io/abo_covid/v/82c9fbc89799845b97081e701b01539b4ac696a3/))
was automatically generated
from [zietzm/abo_covid@82c9fbc](https://github.com/zietzm/abo_covid/tree/82c9fbc89799845b97081e701b01539b4ac696a3)
on April 6, 2020.
</em></small>

## Authors



+ **Michael Zietz**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon}
    [0000-0003-0539-630X](https://orcid.org/0000-0003-0539-630X)
    · ![GitHub icon](images/github.svg){.inline_icon}
    [zietzm](https://github.com/zietzm)
    · ![Twitter icon](images/twitter.svg){.inline_icon}
    [ZietzMichael](https://twitter.com/ZietzMichael)<br>
  <small>
     Department of Biomedical Informatics, Columbia University
     · Funded by NIH T15 LM007079
  </small>



## Abstract {.page_break_before}

The rapid global spread of the novel coronavirus SARS-CoV-2 has strained existing healthcare and testing resources, making the identification and prioritization of individuals most at-risk a critical challenge.
A recent study of patients in China discovered an association between ABO blood type and SARS-CoV-2 infection status by comparing COVID-19 patients with the general population.
Whether blood type is associated with increased COVID-19 morbidity or mortality remains unknown.
We used observational healthcare data on 1559 COVID-tested individuals (682 COV+) with known blood type in the New York Presbyterian (NYP) hospital system to assess the association between ABO+Rh blood type and SARS-CoV-2 infection status, intubation, and death.
A higher proportion of blood group A and a lower proportion of blood group O were found among COVID-19 patients compared to those testing negative for the virus, though in both cases the result is significant only in Rh positive blood types.
A meta-analysis of NYP data with previously reported data from China uncovered significantly increased A and B and significantly decreased O blood groups among COVID-19 patients.
Our data do not provide strong evidence of associations between blood group and intubation or death among COVID-19 patients.
While our results are based on preliminary observational data collected during the care of patients and should not be used to guide clinical practice, we find further evidence of recently-discovered associations between blood group and SARS-CoV-2 infection status and new evidence of associations between B and Rh blood groups and COVID-19.


## Background

The novel Coronavirus disease (COVID-19) has rapidly spread across the globe and has caused over 1,130,000 confirmed infections and over 62,000 deaths worldwide as of April 5, 2020 [@url:who_sit_rep].
A number of risk factors for COVID-19 infection, morbidity, and mortality are known, including age, sex, and a number of chronic conditions and laboratory findings [@doi:10/ggnxb3].
Recently, a study on COVID-19 patients in Whuhan and Shenzhen, China discovered associations between ABO blood types and infection [@doi:10.1101/2020.03.11.20031096].
Their analysis compared blood groups between hospitalized COVID-19 patients and the general populations of Wuhan and Shenzhen City, as assessed by previously-published samples of healthy individuals.
They found that the odds of testing positive for COVID-19 among A blood groups was increased and among O blood groups was decreased relative to the general population.
Similarly, previous work has identified associations between ABO blood groups and a number of different infections or disease severity following infections, including SARS-CoV-1 [@doi:10.1001/jama.293.12.1450-c], _P. falciparum_ [@doi:10/db42m2], _H. pylori_ [@doi:10.1126/science.8018146], Norwalk virus [@doi:10.1038/nm860], hepatitis B virus [@doi:10.1002/ijc.26376], and _N. gonorrhoeae_ [@doi:10.1093/infdis/133.3.329].

Within the United States, New York City has become a major center of the pandemic, with over 64,000 cases and over 2,400 deaths as of April 5, 2020 [@url:https://www1.nyc.gov/site/doh/covid/covid-19-data.page].
We sought to replicate and extend the previous investigation into the association between COVID-19 and blood type using electronic health record data from the New York Presbyterian (NYP) hospital system in New York, USA.
We compared both ABO and ABO+Rh blood types, and we investigated three COVID-19 outcomes: infection status, intubation, and death.


## Methods

We compared several combinations of blood group definitions (ABO vs ABO+Rh) and COVID-19 outcomes.
Outcomes were compared between four pairs of populations: COV+ vs COV-, COV+ vs general population (excluding those tested for COVID-19), COV+/Intubated vs COV+/Not intubated, and COV+/Deceased vs COV+/Alive.
For each of the eight test conditions (2 blood group definitions and 4 outcome comparison population pairs), we performed a Pearson's Chi-squared test to test whether blood group distributions differ between the compared populations.
Additionally, we compared each blood group against all others using a 2x2 contingency table to determine effect sizes for each blood group itself.
For the one-vs-rest blood group comparisons, we report odds ratios (OR), p-values from Fisher's exact test (two-sided), and odds ratio confidence intervals.

We also performed a meta-analysis using our data in combination with data from Wuhan and Shenzhen reported by Zhao et al. [@doi:10.1101/2020.03.11.20031096].
These analyses used a random effects model to create pooled estimates of odds ratios for each ABO blood group in comparisons between COV+ individuals and the general populations of New York, Wuhan, and Shenzhen.

Individuals with a single positive COVID-19 test were considered COVID+, even if they had previous or subsequent negative COVID tests.
Blood group was identified using either a measurement of LOINC code 34474-7, "ABO and Rh group \[Type\] in Cord blood," or the results of a procedure identified by one of the names listed in Table @tbl:blood_group_names.
We excluded individuals with multiple contradictory blood group measurements.
The distribution of blood groups in the general population was estimated using blood group lab results on 108,929 individuals recorded in the NYP electronic health record (EHR) system between May 2011 and June 2019, excluding results for any individuals later tested for COVID-19 (regardless of result).

We considered EHR data up to April 5, 2020.
Our analyses were conducted using the R language, and we used the `meta` package [@doi:10/drbb] for meta-analysis.
While our data from NYP are protected by HIPAA and cannot be released, we have made all code used for our analysis available at <https://github.com/zietzm/abo_covid_analysis>.
The manuscript was written [openly on GitHub](https://github.com/zietzm/abo_covid) using the Manubot software [@doi:10.1371/journal.pcbi.1007128].


## Results

We first determined blood groups for COVID-tested individuals using laboratory measurements recorded in the NYP EHR system.
One individual with multiple contradictory blood group measurements was excluded, resulting in 1,559 individuals with known blood groups who received a COVID-19 test (either positive or negative result).
Of these, 682 were COV+ (positive in at least one COVID-19 test) and 877 were COV- (negative in all COVID-19 tests administered).
Among the COV+ individuals, 179 were intubated and 80 had died, while the remaining individuals had not been intubated and remained alive as of April 5, 2020.
We found that 354 tested COV- individuals were intubated during the same time, though we did not include them in any analysis.

For each comparison cohort pair, we performed chi-squared tests using both ABO and ABO+Rh blood types (Tables @tbl:combined_chisq, @tbl:combined_counts).
Since there were no AB-negative individuals testing positive for COVID-19 and only 5 individuals testing negative, we excluded AB-negative from all ABO+Rh analyses.
Finally, we conducted individual tests of each blood type against all others (within the same ABO vs ABO+Rh system) for each of the COVID-19 outcomes we considered (Full data in Table @tbl:combined_fisher).

We found associations between COVID-19 status and both ABO (p=0.006) and ABO+Rh (p=0.031) blood groups in a comparison between individuals testing positive vs testing negative (Tables @tbl:combined_chisq, @tbl:pos_neg_fisher).
Blood groups A were associated with increased odds of testing positive for COVID-19 (OR 1.338, p=0.009), while O blood groups were associated with decreased odds of testing positive (OR 0.790, p=0.036).
While few individuals with AB blood groups were included (21 COV+, 47 COV-), we also found AB blood groups to be associated with decreased odds of testing positive (OR 0.561, p=0.033).
When we tested individual ABO+Rh blood groups against all others, we discovered that strong associations are only found in Rh positive blood groups (Tables @tbl:pos_neg_fisher, @tbl:combined_fisher).
Finally, we compared the blood group distributions between all individuals tested for COVID-19 with the general population at NYP, finding insufficient evidence to conclude that tested individuals are not drawn from the general population at random (Chi-squared 3.8896, p=0.2736).


|Blood group type |Comparison groups                    | Chi-squared |df |p-value |
|:----------------|:------------------------------------|:----------|:--|:-------|
|ABO              |COV+ vs general population           |5.288      |3  |0.152   |
|ABO+Rh           |COV+ vs general population           |9.129      |6  |0.166   |
|ABO              |COV+ vs COV-                         |12.295     |3  |**0.006**   |
|ABO+Rh           |COV+ vs COV-                         |13.882     |6  |**0.031**   |
|ABO              |COV+/Intubated vs COV+/Not intubated |3.493      |3  |0.322   |
|ABO+Rh           |COV+/Intubated vs COV+/Not intubated |5.844      |6  |0.441   |
|ABO              |COV+/Died vs COV+/Alive              |3.190      |3  |0.363   |
|ABO+Rh           |COV+/Died vs COV+/Alive              |7.431      |6  |0.283   |

Table: Summary of chi-squared tests for association between blood type and COVID-19 outcomes. "df" indicates the degrees of freedom; ABO used a 4x2 table for each test, while ABO+Rh used a 6x2 table for each test, resulting in 3 and 5 degrees of freedom, respectively. {#tbl:combined_chisq}


|Blood group |Blood group type |OR    |95% CI        |p-value |
|:----------|:----------|:-----|:---------------|:-----------|
|A             |ABO           |1.338 |1.072 - 1.672   |**0.009**   |
|A-negative    |ABO+Rh        |0.832 |0.42 - 1.608    |0.641   |
|A-positive    |ABO+Rh        |1.382 |1.099 - 1.737   |**0.004**   |
|AB            |ABO           |0.561 |0.315 - 0.969   |**0.033**   |
|AB-positive   |ABO+Rh        |0.628 |0.35 - 1.097    |0.093   |
|B             |ABO           |1.117 |0.843 - 1.477   |0.446   |
|B-negative    |ABO+Rh        |0.636 |0.216 - 1.695   |0.381   |
|B-positive    |ABO+Rh        |1.169 |0.874 - 1.563   |0.282   |
|O             |ABO           |0.804 |0.654 - 0.987   |**0.036**   |
|O-negative    |ABO+Rh        |1.034 |0.548 - 1.93    |1.000   |
|O-positive    |ABO+Rh        |0.790 |0.642 - 0.971   |**0.024**   |

Table: Summary of one-vs-rest analysis for a comparison of COV+ vs COV- individuals. Each test compares the listed blood group to all other blood groups (combined) between the COV+ and COV- individuals. OR means odds ratio (COV+ vs COV-), and the 95% CI is a confidence interval on the OR. P-values computed using Fisher's exact test. {#tbl:pos_neg_fisher}

### Meta-analysis

Finally, we compared our data from New York City to the data from Wuhan and Shenzhen presented by Zhao et al. [@doi:10.1101/2020.03.11.20031096] and conducted a meta-analysis using the data they report in combination with our NYP data.
Zhao et al. used a random effects model to meta-analyze data between three different hospitals (Wuhan Jinyintan, Renmin Hospital in Wuhan, and Shenzhen Third People's Hospital), comparing each hospital's COV+ blood group distribution to the general population distribution for each city.
We performed a similar analysis---including NYP data---to assess the effect of blood type in the combined data from all four sources (full counts in Table @tbl:abo_nyc_vs_china).

We found that the distribution of blood groups in the general population at NYP differs significantly from both the distributions in Shenzhen (Chi-squared = 2056, p-value < 2.2e-16) and Wuhan (Chi-squared = 583.29, p-value < 2.2e-16) (Table @tbl:abo_nyc_vs_china).
The difference in distributions is reflected in tests of heterogeneity between sites, where we find more heterogeneity between sites in our meta-analysis than Zhao et al.'s meta-analysis (Table @tbl:meta_heterogeneity).

We fit a random effects model for each ABO blood type using data from NYP and the three sources for which Zhao et al. report data.
The overall associations between ABO blood groups and COVID-19 status that Zhao et al. identified (significantly increased COV+ odds for blood group A and decreased COV+ odds for blood group O) are replicated in our meta-analysis (Table @tbl:meta_odds).
Using the additional data from NYP, the pooled association between blood group B becomes larger in effect size and significant at the 5% level (original: OR 1.09, p=0.121; with NYP data: OR 1.25, p=0.0361).

| Blood group | OR | 95% CI | p-value |
|:----- |:------ |:---------- |:--------|
| A | 1.1636 | 1.0155 - 1.3333 | **0.0291** |
| B | 1.1101 | 1.0068 - 1.2240 | **0.0361** |
| AB | 1.2519 | 0.8384 - 1.8694 | 0.2721 |
| O | 0.7252 | 0.5971 - 0.8807 | **0.0012** |

Table: Meta-analysis associations for individual ABO blood groups in comparisons of COV+ vs general population using a random effects model. Each blood group was compared against all others using data from NYP, and Zhao et al. (Wuhan Jinyintan, Renmin Hospital in Wuhan, and Shenzhen Third People's Hospital). OR refers to the pooled odds ratio (COV+ vs general population), and the 95% CI is a confidence interval on the OR. P-values are for the pooled association from the random effects model. {#tbl:meta_odds}


## Discussion

We stratified by ABO+Rh blood groups in a comparison of COV+ vs COV- individuals and found that A and O associations were only supported by evidence among those with Rh positive blood groups.
Negative Rh blood groups are less common in our data, representing only 9.25% of individuals, so the lack of evidence for association with negative blood types could be due to lower sample sizes.
However, odds ratios for ABO groups A and O are less extreme than the associated ABO+Rh blood groups (A+, O+), and the corresponding negative blood groups (A-, O-) have (insignificant) odds in the opposite directions as their positive counterparts.
Further work is needed to better understand the associations between Rh negative blood groups and COVID-19.

Our meta-analysis found large heterogeneity in blood group distributions between Wuhan, Shenzhen, and New York City, consistent with previous work indicating large differences in blood group distributions between the United States and China [@doi:10.1136/bmjopen-2017-018476; @doi:10.1111/j.1537-2995.2004.03338.x].
Overall blood group differences introducted heterogeneity in our meta-analysis comparisons of blood group between COV+ individuals and the general population.
Larger sample sizes of COVID-19 patients will allow afford a more detailed picture of the effects of blood type on COVID-19 susceptibility.

The significant associations we found for blood type between COV+ and COV- individuals were far from significant in a comparison between COV+ and the general population at NYP.
A possible explanation for this finding is that individuals tested for infection at NYP represent a more homogeneous sub-population of patients at NYP.
Increased homogeneity would strengthen the blood-group-COVID-19 association signal as it would reduce the influence of overall population differences in blood-type distribution.
We did not find sufficient evidence to conclude that COVID-19-tested individuals have a significantly different blood group distribution than the general population at NYP, though we cannot rule out other differences between tested and general populations that could explain the difference in associations.
Moreover, our meta-analysis using COV+ vs general population found significant associations between A, B, and O blood groups, and the NYP data received 20-30 percent weight for each comparison, indicating a large contribution to the pooled associations.
Further work is needed to understand how the population of COVID-tested patients differs from the general population.

We did not identify any significant relationships between blood group and intubation or death due to COVID-19.
However, intubation and death due to COVID-19 continue in New York as of April 5, 2020, and individuals currently alive, not intubated, or COV- may reach these outcomes in the future.
Our data is preliminary and represents a snapshot of the pandemic in a New York hospital system.
When more patients are tested, intubated, and recover, we will be better able to assess the relationship between blood group and eventual COVID-19 outcomes that may not have occurred at the time of our analysis.

Our study was conducted on EHR data collected during the care of patients, not necessarily with research intent.
Our sample sizes were relatively small, making stratifications by age, sex, comorbidities, or other risk factors challenging.
As an observational study without rigorous corrections for possible confounding, our results should be considered preliminary and should not be taken to inform clinical practice or policy.


## Conclusion

In this study we found further evidence for the association between blood group and COVID-19.
Using data from NYP, we found the odds of COVID-19 positive vs negative test results were increased in blood groups A and decreased in blood group O, consistent with previous results from Wuhan and Shenzhen [@doi:10.1101/2020.03.11.20031096].
While few individuals were included in our cohort, we discovered a new significant odds decrease for AB blood group.
In a meta-analysis of our data with data from Wuhan and Shenzhen reported by Zhao et al., we found significant associations between A, B, and O blood groups and COVID-19.
Specifically, we found that A and B blood groups are associated with increased odds and O is associated with decreased odds in a comparison between COV+ and the general population.
Our meta-analysis extended previous work using additional data and allowed us to declare significant at the 5% level an association between B blood group and COVID-19 (OR 1.11) that was weaker in the previous study (OR 1.09, p=0.121).


## Supplemental information

| Procedure name |
| ------- |
| TYPE AND SCREEN |
| BLOOD TYPE ABO AND RH |
| TYPE (ABO CONFIRMATION ONLY) |
| NEWBORN PANEL (ABO/RH PLUS DAT PLUS AB SCREEN) |
| CORD BLOOD PANEL (ABO/RH PLUS DAT) |
| NEWBORN BLOOD TYPE |

Table: Procedures used by name to identify individual blood group {#tbl:blood_group_names}


|Blood group |COV+ |COV- |COV+/<br>Intubated |COV+/Not<br>intubated |COV+/<br>Died |COV+/<br>Alive |General<br>population |
|:-------------|:--------|:--------|:------------|:------------|:---------|:----------|:--------------|
|**A**           |233  |245  |62             |171                |27        |206        |35643              |
|A-negative  |17   |26   |2              |15                 |1         |16         |3447               |
|A-positive  |216  |219  |60             |156                |26        |190        |32196              |
|**AB**          |21   |47   |8              |13                 |5         |16         |4582               |
|AB-negative[*](#asterisk0) |0    |5    |0              |0                  |0         |0          |394                |
|AB-positive |21   |42   |8              |13                 |5         |16         |4188               |
|**B**           |116  |136  |35             |81                 |12        |104        |16229              |
|B-negative  |7    |14   |2              |5                  |0         |7          |1422               |
|B-positive  |109  |122  |33             |76                 |12        |97         |14807              |
|**O**           |312  |449  |74             |238                |36        |276        |52406              |
|O-negative  |21   |26   |4              |17                 |0         |21         |4808               |
|O-positive  |291  |423  |70             |221                |36        |255        |47598              |
|**Total**       |682  |877  |179            |503                |80        |602        |108860             |

Table: Counts of individuals by blood group and the three COVID-19 outcomes assessed (test result, intubation, death), and blood groups estimated for the general population using data from 108,929 individuals not tested for COVID-19. {#tbl:combined_counts}

<a name="asterisk0">\*</a> AB-negative was not included in the ABO+Rh analyses as no individuals with that blood type recorded tested positive for COVID-19.


|Blood group |Blood group type |Comparison groups                    |OR    |95% CI        |p-value |
|:-------------|:-------------|:-------------------------------|:-----|:---------------|:-----------|
|A           |ABO              |COV+ vs general population           |1.066 |0.906 - 1.252 |0.437   |
|A-negative       |ABO+Rh           |COV+ vs general population           |0.779 |0.45 - 1.258  |0.379   |
|A-positive       |ABO+Rh           |COV+ vs general population           |1.098 |0.93 - 1.294  |0.257   |
|AB          |ABO              |COV+ vs general population           |0.723 |0.444 - 1.116 |0.151   |
|AB-positive      |ABO+Rh           |COV+ vs general population           |0.791 |0.486 - 1.221 |0.368   |
|B           |ABO              |COV+ vs general population           |1.170 |0.949 - 1.432 |0.131   |
|B-negative       |ABO+Rh           |COV+ vs general population           |0.781 |0.312 - 1.622 |0.733   |
|B-positive       |ABO+Rh           |COV+ vs general population           |1.203 |0.971 - 1.48  |0.083   |
|O           |ABO              |COV+ vs general population           |0.908 |0.778 - 1.059 |0.219   |
|O-negative       |ABO+Rh           |COV+ vs general population           |0.685 |0.421 - 1.057 |0.092   |
|O-positive       |ABO+Rh           |COV+ vs general population           |0.952 |0.815 - 1.111 |0.536   |
|A           |ABO              |COV+ vs COV-                         |1.338 |1.072 - 1.672 |**0.009**   |
|A-negative       |ABO+Rh           |COV+ vs COV-                         |0.832 |0.42 - 1.608  |0.641   |
|A-positive       |ABO+Rh           |COV+ vs COV-                         |1.382 |1.099 - 1.737 |**0.004**   |
|AB          |ABO              |COV+ vs COV-                         |0.561 |0.315 - 0.969 |**0.033**   |
|AB-positive      |ABO+Rh           |COV+ vs COV-                         |0.628 |0.35 - 1.097  |0.093   |
|B           |ABO              |COV+ vs COV-                         |1.117 |0.843 - 1.477 |0.446   |
|B-negative       |ABO+Rh           |COV+ vs COV-                         |0.636 |0.216 - 1.695 |0.381   |
|B-positive       |ABO+Rh           |COV+ vs COV-                         |1.169 |0.874 - 1.563 |0.282   |
|O           |ABO              |COV+ vs COV-                         |0.804 |0.654 - 0.987 |**0.036**   |
|O-negative       |ABO+Rh           |COV+ vs COV-                         |1.034 |0.548 - 1.93  |1.000   |
|O-positive       |ABO+Rh           |COV+ vs COV-                         |0.790 |0.642 - 0.971 |**0.024**   |
|A           |ABO              |COV+/Intubated vs COV+/Not intubated |1.029 |0.705 - 1.493 |0.927   |
|A-negative       |ABO+Rh           |COV+/Intubated vs COV+/Not intubated |0.368 |0.04 - 1.608  |0.263   |
|A-positive       |ABO+Rh           |COV+/Intubated vs COV+/Not intubated |1.121 |0.765 - 1.635 |0.575   |
|AB          |ABO              |COV+/Intubated vs COV+/Not intubated |1.762 |0.622 - 4.678 |0.214   |
|AB-positive      |ABO+Rh           |COV+/Intubated vs COV+/Not intubated |1.762 |0.622 - 4.678 |0.214   |
|B           |ABO              |COV+/Intubated vs COV+/Not intubated |1.266 |0.79 - 1.999  |0.298   |
|B-negative       |ABO+Rh           |COV+/Intubated vs COV+/Not intubated |1.125 |0.106 - 6.948 |1.000   |
|B-positive       |ABO+Rh           |COV+/Intubated vs COV+/Not intubated |1.269 |0.783 - 2.027 |0.342   |
|O           |ABO              |COV+/Intubated vs COV+/Not intubated |0.785 |0.547 - 1.124 |0.190   |
|O-negative       |ABO+Rh           |COV+/Intubated vs COV+/Not intubated |0.654 |0.158 - 2.042 |0.616   |
|O-positive       |ABO+Rh           |COV+/Intubated vs COV+/Not intubated |0.820 |0.569 - 1.177 |0.291   |
|A           |ABO              |COV+/Died vs COV+/Alive              |0.979 |0.574 - 1.639 |1.000   |
|A-negative       |ABO+Rh           |COV+/Died vs COV+/Alive              |0.464 |0.011 - 3.067 |0.708   |
|A-positive       |ABO+Rh           |COV+/Died vs COV+/Alive              |1.044 |0.608 - 1.757 |0.898   |
|AB          |ABO              |COV+/Died vs COV+/Alive              |2.437 |0.679 - 7.226 |0.088   |
|AB-positive      |ABO+Rh           |COV+/Died vs COV+/Alive              |2.437 |0.679 - 7.226 |0.088   |
|B           |ABO              |COV+/Died vs COV+/Alive              |0.845 |0.402 - 1.646 |0.751   |
|B-negative       |ABO+Rh           |COV+/Died vs COV+/Alive              |0.000 |0 - 5.26      |1.000   |
|B-positive       |ABO+Rh           |COV+/Died vs COV+/Alive              |0.919 |0.436 - 1.794 |0.872   |
|O           |ABO              |COV+/Died vs COV+/Alive              |0.966 |0.586 - 1.585 |0.906   |
|O-negative       |ABO+Rh           |COV+/Died vs COV+/Alive              |0.000 |0 - 1.429     |0.158   |
|O-positive       |ABO+Rh           |COV+/Died vs COV+/Alive              |1.113 |0.675 - 1.827 |0.718   |

Table: Summary of all one-vs-rest analyses conducted. Each individual test compared the listed blood group with all other blood groups between the listed comparison groups. Shown are comparisons between each blood type and all three COVID-19 outcomes investigated. {#tbl:combined_fisher}


|Blood group |NYP general population |NYP COV+    |Shenzhen general population |Shenzhen COV+ |Wuhan general population |Wuhan Jinyintan COV+ |Wuhan Renmin COV+ |
|:-----------|:----------------------|:-----------|:---------------------------|:-------------|:------------------------|:--------------------|:-----------------|
|A           |32.7% (35643)          |34.2% (233) |28.8% (6728)                |28.8% (82)    |32.2% (1188)             |37.7% (670)          |39.8% (45)        |
|AB          |4.2% (4582)            |3.1% (21)   |7.3% (1712)                 |13.7% (39)    |9.1% (336)               |10% (178)            |13.3% (15)        |
|B           |14.9% (16229)          |17% (116)   |25.1% (5880)                |29.1% (83)    |24.9% (920)              |26.4% (469)          |22.1% (25)        |
|O           |48.1% (52406)          |45.7% (312) |38.8% (9066)                |28.4% (81)    |33.8% (1250)             |25.8% (458)          |24.8% (28)        |

Table: Distributions of blood groups between New York City data from the NYP EHR system and individuals from Shenzhen (cases from Shenzhen
Third People's Hospital, controls from Shenzhen general population) and Wuhan (cases from Wuhan Jinyintan Hospital and Renmin Hospital of Wuhan University, controls from Wuhan general population). Shenzhen and Wuhan data reported by Zhao et al. [@doi:10.1101/2020.03.11.20031096]. {#tbl:abo_nyc_vs_china}


| Blood group | Site | OR | 95% CI | %Weight |
|:---------- |:----- |:----- |:----------- |:------- |
| A | NYP              | 1.0660 | 0.9095 - 1.2494 | 31.8 |
| A | Wuhan Jinyintan | 1.2790 | 1.1364 - 1.4395 | 39.3 |
| A | Wuhan Renmin     | 1.3959 | 0.9519 - 2.0472 | 10.3 |
| A | Shenzhen         | 1.0001 | 0.7727 - 1.2945 | 18.6 |
| B | NYP              | 1.1698 | 0.9573 - 1.4294 | 23.7 |
| B | Wuhan Jinyintan | 1.0828 | 0.9516 - 1.2321 | 57.1 |
| B | Wuhan Renmin     | 0.8566 | 0.5460 - 1.3440 |  4.7 |
| B | Shenzhen         | 1.2233 | 0.9458 - 1.5822 | 14.4 |
| AB | NYP              | 0.7230 | 0.4678 - 1.1176 | 23.5 |
| AB | Wuhan Jinyintan | 1.1139 | 0.9201 - 1.3487 | 30.2 |
| AB | Wuhan Renmin     | 1.5297 | 0.8783 - 2.6643 | 20.0 |
| AB | Shenzhen         | 2.0071 | 1.4266 - 2.8237 | 26.3 |
| O | NYP              | 0.9084 | 0.7810 - 1.0566 | 31.1 |
| O | Wuhan Jinyintan | 0.6799 | 0.5993 - 0.7715 | 32.9 |
| O | Wuhan Renmin     | 0.6441 | 0.4179 - 0.9925 | 13.2 |
| O | Shenzhen         | 0.6272 | 0.4842 - 0.8124 | 22.8 |

Table: Weights for sites in random-effects meta-analyses conducted for each ABO blood group. Each blood group was compared against all others using data from NYP, and Zhao et al. (Wuhan Jinyintan, Renmin Hospital in Wuhan, and Shenzhen Third People's Hospital). {#tbl:meta_weights}


| Blood group | I-squared | I-squared 95% CI | Q | Q d.f. | Q p-value |
|:----- |:------ |:---------- |:--------|:-------|
| A | 47.1% | 0.0 - 82.4 | 5.67 | 3 | 0.1287 |
| B | 0.0% | 0.0 - 79.4 |  2.23 | 3 | 0.5268 |
| AB | 80.6% | 48.9 - 92.6 | 15.43 | 3 | 0.0015 |
| O | 72.1% | 21.0 - 90.2 | 10.76 | 3 | 0.0131 |

Table: Heterogeneity across meta-analysis sites. {#tbl:meta_heterogeneity}


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
