# Fairness in Machine Learning

## Challenge

Consider a lending model that predicts whether an applicant will repay a loan. If its training examples contain only previously approved borrowers, they omit people denied credit by an earlier biased process. A postcode feature could also act as a proxy for ethnicity. The model could therefore reject creditworthy applicants from an underserved community, causing an **allocation** harm: unequal access to loans. High overall accuracy would not establish fairness.

Preventative controls should cover the whole lifecycle:

- **Data representation:** Compare the dataset with the intended applicant population, document missing groups and historical selection bias, and gather appropriate evidence for underrepresented applicants. Rebalancing alone cannot reveal repayment outcomes for people who never received loans. Review labels and proxy features as well as group counts.
- **Subgroup evaluation:** Compare approval rates, false rejections of creditworthy applicants, and calibration across relevant groups and intersections. Report sample sizes and uncertainty; agree on acceptable tradeoffs with affected communities and a team with diverse perspectives before deployment.
- **Appeal:** Give applicants understandable reasons for decisions, a way to correct inaccurate records, and access to a trained human reviewer with authority to reconsider a denial. Provide accessible alternatives when the automated system cannot assess an applicant reliably.
- **Monitoring:** Track subgroup outcomes, data drift, complaints, and appeal reversals after deployment. Assign an accountable owner and escalation criteria to pause or revise the model when harms emerge. Protect sensitive audit data and limit access to it.

These are proposed controls for a hypothetical scenario, not measured results. Fairness depends on the decision process and its social context as well as model metrics.

## Assignment — Skipped

Running and reporting on an external Responsible AI notebook is excluded under the approved scope. No RAI dashboard was run, and no notebook findings or execution results are claimed.
